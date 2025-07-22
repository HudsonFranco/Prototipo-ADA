import re
import asyncio
from datetime import timedelta
from django.utils import timezone
from playwright.async_api import async_playwright
from asgiref.sync import sync_to_async
from .models import ScrapedContent

async def scrape_jovemprogramador_playwright():
    base_url = "https://www.jovemprogramador.com.br"
    
    target_urls = [
        f"{base_url}/index.php",
        f"{base_url}/sobre.php",
        f"{base_url}/patrocinadores.php",
        f"{base_url}/duvidas.php",
        f"{base_url}/duvidas.php#cadastro",
        f"{base_url}/hackathon/",
        f"{base_url}/sobre.php#noticias",
        f"{base_url}/apoiadores.php",
    ]

    all_scraped_text_parts = []
    
    CACHE_EXPIRATION_HOURS = 24 

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        for url in target_urls:
            try:
                # Recuperar do cache - use await sync_to_async
                cached_content = await sync_to_async(
                    ScrapedContent.objects.filter(url=url).first
                )() # O .first() precisa ser chamado após o sync_to_async

                if cached_content and (cached_content.next_scrape_due is None or cached_content.next_scrape_due > timezone.now()):
                    print(f"Conteúdo para {url} recuperado do cache.")
                    all_scraped_text_parts.append(cached_content.content)
                    continue
                elif cached_content:
                    print(f"Cache para {url} expirado. Re-raspando...")
                else:
                    print(f"Nenhum cache encontrado para {url}. Raspando...")

            except Exception as e:
                print(f"Erro ao acessar cache para {url}: {e}. Tentando raspar.")

            page = await browser.new_page()
            try:
                print(f"Navegando para: {url} com Playwright.")
                await page.goto(url, wait_until='networkidle', timeout=30000) 
                await page.wait_for_timeout(2000)
                
                content_selector = 'div.post-content p, article.post-text p, main#content p, h1, h2, h3, li, body, span.description, div.page-content p' 
                
                elements = await page.query_selector_all(content_selector)
                
                current_page_text_parts = []
                for element in elements:
                    text_content = await element.inner_text()
                    text = text_content.strip()
                    if text and len(text) > 20:
                        current_page_text_parts.append(text)
                
                if current_page_text_parts:
                    page_full_content = " ".join(current_page_text_parts)
                    all_scraped_text_parts.append(page_full_content)
                    print(f"Scraping da URL {url} concluído e conteúdo obtido.")

                    # Salvar/Atualizar no cache - use await sync_to_async
                    next_scrape_time = timezone.now() + timedelta(hours=CACHE_EXPIRATION_HOURS)
                    await sync_to_async(ScrapedContent.objects.update_or_create)( # <--- Modificado
                        url=url,
                        defaults={
                            'content': page_full_content,
                            'last_scraped': timezone.now(),
                            'next_scrape_due': next_scrape_time
                        }
                    )
                    print(f"Conteúdo de {url} salvo/atualizado no cache. Próxima raspagem em: {next_scrape_time}")
                else:
                    print(f"Nenhum conteúdo significativo encontrado para {url}. Não salvando no cache.")

            except Exception as e:
                print(f"Erro no scraping Playwright da URL {url}: {e}")
                try:
                    # Tentar fallback para cache antigo - use await sync_to_async
                    cached_content = await sync_to_async(
                        ScrapedContent.objects.filter(url=url).first
                    )()
                    if cached_content:
                        print(f"Erro ao raspar {url}, usando conteúdo antigo do cache.")
                        all_scraped_text_parts.append(cached_content.content)
                except Exception as cache_e:
                    print(f"Erro adicional ao tentar fallback para cache: {cache_e}")
            finally:
                await page.close()
        
        await browser.close()

    if not all_scraped_text_parts:
        print("Nenhum conteúdo significativo foi obtido, seja por raspagem ou cache.")
        return "CONTEUDO_NAO_ENCONTRADO_SITE"

    full_content = " ".join(all_scraped_text_parts)
    max_openai_context_chars = 12000 
            
    print(f"Conteúdo agregado total para OpenAI (tamanho: {len(full_content)} chars).")
    return full_content[:max_openai_context_chars]