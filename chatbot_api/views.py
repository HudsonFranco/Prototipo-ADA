from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re
import asyncio 
from django.utils import timezone
from asgiref.sync import sync_to_async

from .utils import scrape_jovemprogramador_playwright
from .services import get_openai_response
from .models import Message
from asgiref.sync import sync_to_async
from datetime import timedelta
from .models import ScrapedContent

from .utils import scrape_jovemprogramador_playwright
from .services import get_openai_response
from .models import Message

def home(request):
    return render(request, 'chatbot_app/index.html')

def oque(request):
    return render(request, 'chatbot_app/oque.html')

def como_funciona(request):
    return render(request, 'chatbot_app/como_funciona.html')

def componentes_chaves(request):
    return render(request, 'chatbot_app/componentes_chaves.html')

def sobre_nos(request):
    return render(request, 'chatbot_app/sobre_nos.html')

def arquivos(request):
    return render(request, 'chatbot_app/Arquivos.html')

def consideracoes(request):
    return render(request, 'chatbot_app/Consideracoes.html')

@csrf_exempt
async def chatbot_view(request):
    session_id = request.session.session_key 
    if not session_id:
        await sync_to_async(request.session.save)()
        session_id = request.session.session_key

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message_text = data.get('message', '').lower()

            await sync_to_async(Message.objects.create)(
                session_id=session_id,
                sender='user',
                text=user_message_text
            )
            print(f"Mensagem do usuário salva: {user_message_text}")

            # Obter histórico de mensagens
            messages_history = await sync_to_async(list)(
                Message.objects.filter(session_id=session_id).order_by('timestamp')
            )
            
            # Formatar histórico para a API
            history_for_api = []
            for msg in messages_history:
                role = "assistant" if msg.sender == "bot" else "user"
                history_for_api.append({"role": role, "content": msg.text})


            bot_response_text = ""

            # --- Lógica para determinar o system_prompt com base na pergunta ---

            # 1. Prioridade: Perguntas sobre a criação/hackaton (resposta fixa)
            hackaton_keywords = ['quem está te desenvolvendo?']
            hackaton_keywords0 = ['qual a sua idade?']
            hackaton_keywords1 = ['quais os patrocinadores?' ]
            hackaton_keywords2 = ['quais os parceiros?']
            hackaton_keywords3 = ['quais os apoiadores?']
            hackaton_keywords4 = ['em que linguagem você foi desenvolvida?']
            


            if any(keyword in user_message_text for keyword in hackaton_keywords):
                bot_response_text = (
                    "Estou em fase de desenvolvimento pela equipe Python Rangers como projeto para o Hackaton do Senac Palhoça. "
                    "A equipe é formada pelos alunos do curso Jovem Programador: "
                    "Renato Teodoro, Matheus Moraes, Hudson Franco, Gustavo Lohn e Vinícius Costa. "
                    "Professora: Karina Fernandes. Coordenador: Vladmir Machado. Gestor de Núcleo: Cleber Rodrigues. Diretora: Renata Scheidt"
                )

            elif any(keyword in user_message_text for keyword in hackaton_keywords0):
                bot_response_text = (
                    "Ainda não saí do forno! Mas quando sair, lá por novembro de 2025, prometo que serei deliciosa e trarei muitas surpresas!"
                    "😜"
                )

            if any(keyword in user_message_text for keyword in hackaton_keywords4):
                bot_response_text = (
                    
                    "Na linguagem Python, utilizando o framework Django para futuras ampliações! Para a parte de IA, estou usando o OpenAI gpt-4o (ChatGPT). Para que eu possa ler o site Jovem Programador, estou raspando o conteúdo com Playwright. Para armazenar as mensagens e raspagens, estou usando o banco de dados SQLite."
                )

            

            #Perguntas sobre a identidade geral da ADA (nome, quem é, propósito)
            # Nestes casos, a ADA DEVE usar conhecimento geral, não o site.
            elif any(keyword in user_message_text for keyword in ['porque ADA?']):
                system_prompt_ada_identity = (
                    
                    "responda com um paragrafo curto que seu nome é uma homenagem da equipe Python Rangers em memória de Ada Lovelace, a primeira programadora do mundo."
                    "Seja sempre prestativa, clara e educada nas respostas."
                    "Resumir para retornar um texto com no maximo 200 caracteres."
                )
                # Não precisamos raspar o site para estas perguntas, então a chamada à raspagem é pulada.
                bot_response_text = get_openai_response(user_message_text, history=history_for_api, system_prompt_override=system_prompt_ada_identity)

            #Prioridade: Perguntas sobre a idade (resposta fixa)
            elif any(keyword in user_message_text for keyword in hackaton_keywords1):
                bot_response_text = (
                    "Olá! Confira abaixo os patrocinadores do nosso evento:\n\n"

                    "🎯 *Patrocinadores:*\n"
                    "- Clubes Associados Software by Limber\n"
                    "- DataRunk\n"
                    "- Tecnológica\n"
                    "- Senior\n"
                    "- Radek\n"
                    "- ADM Sistemas\n"
                    "- DataInfo\n"
                    "- Ap.Controle\n"
                    "- Buss Construção\n"
                    "- Grupo Softplan\n"
                    "- KLab\n"
                    "- NDD\n"
                    "- CB Sistemas\n"
                    "- WK\n"
                    "- Loqquei\n"
                    "- HartSystem Sistemas\n"
                    "- Exímio\n"
                    "- Dev10\n"
                    "- CloudPark\n"
                    "- DGSYS\n"
                    "- Grupo BST Sistemas\n\n"
                )
                 #Prioridade: Perguntas sobre a idade (resposta fixa)
            elif any(keyword in user_message_text for keyword in hackaton_keywords2):
                bot_response_text = (
                    "Olá! Confira abaixo os parceiros do nosso evento:\n\n"

                    "🤝 *Parceiros:*\n"
                    "- Senac\n"
                    "- Seprosc\n\n"
                )

             #Prioridade: Perguntas sobre a idade (resposta fixa)
            elif any(keyword in user_message_text for keyword in hackaton_keywords3):
                bot_response_text = (
                    "Olá! Confira abaixo os apoiadores do nosso evento:\n\n"

                    "💡 *Apoiadores:*\n"
                    "- Communitech\n"
                    "- Somar\n"
                    "- Orion\n"
                    "- CIB – Centro de Inovação Blumenau\n"
                    "- Novela Hub\n"
                    "- Collabtech\n"
                    "- Gene Conecta\n"
                    "- CITeB\n"
                    "- Inovale\n"
                    "- Acate\n"
                    "- Amureltec"
                )



            # 3. Última prioridade: Todas as outras perguntas (raspar o site)
            else:
                scraped_content = ""
                alert_message = ""
                
                # Lógica de cache
                cache_duration = timedelta(hours=24)
                url_to_scrape = "http://jovemprogramador.org.br/"
                
                try:
                    cached_content = await sync_to_async(ScrapedContent.objects.get)(
                        url=url_to_scrape,
                        last_scraped__gte=timezone.now() - cache_duration
                    )
                    scraped_content = cached_content.content
                    print("Conteúdo encontrado no cache.")
                except ScrapedContent.DoesNotExist:
                    print(f"Tentando raspar {url_to_scrape} com Playwright.")
                    scraped_result = await scrape_jovemprogramador_playwright()

                    if scraped_result != "CONTEUDO_NAO_ENCONTRADO_SITE":
                        scraped_content = scraped_result
                        await sync_to_async(ScrapedContent.objects.update_or_create)(
                            url=url_to_scrape,
                            defaults={'content': scraped_content, 'last_scraped': timezone.now()}
                        )
                        print(f"Conteúdo raspado e salvo no cache ({len(scraped_content)} chars).")
                    else:
                        alert_message = "Apesar de ter acessado o site Jovem Programador, não encontrei informações relevantes ou específicas sobre sua pergunta no conteúdo que pude raspar. Tente refinar sua pergunta ou verificar o site diretamente."
                        scraped_content = ""

                # System prompt para perguntas baseadas no site
                system_prompt_site = (
                    "Você é ADA, uma assistente virtual criada para responder dúvidas com base em informações confiáveis do site Jovem Programador. "
                    "Não use conhecimento geral da internet para responder a perguntas que se referem ao site. Se não se referir ao site avise e responda com base na internet de forma coerente. "
                    "Seja sempre prestativa, clara e educada nas respostas."
                )

                if scraped_content and scraped_content != "CONTEUDO_NAO_ENCONTRADO_SITE": # Verificação dupla
                    system_prompt_site += f" As seguintes informações foram raspadas do site Jovem Programador: {scraped_content}. Responda à pergunta do usuário usando APENAS essas informações. Se a resposta para a pergunta do usuário não estiver clara e diretamente no texto fornecido, diga claramente que a informação não foi encontrada no site Jovem Programador."
                else:
                    system_prompt_site += f" {alert_message} Portanto, não posso responder a essa pergunta com informações do site Jovem Programador. Não tente inventar uma resposta com base em conhecimento generalizado."

                bot_response_text = get_openai_response(user_message_text, history=history_for_api, system_prompt_override=system_prompt_site)

            # Salvar mensagem do bot
            await sync_to_async(Message.objects.create)(
                session_id=session_id,
                sender='bot',
                text=bot_response_text
            )
            print(f"Mensagem do bot salva: {bot_response_text[:50]}...")

            return JsonResponse({'response': bot_response_text})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Requisição inválida (JSON).'}, status=400)
        except Exception as e:
            print(f"Erro geral na chatbot_view: {e}")
            error_response_text = f'Ocorreu um erro interno: {e}'
            await sync_to_async(Message.objects.create)(
                session_id=session_id,
                sender='bot',
                text=error_response_text
            )
            return JsonResponse({'error': error_response_text}, status=500)

    return render(request, 'chatbot_app/index.html')