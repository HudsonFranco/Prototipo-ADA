from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone # Para timestamps

class Message(models.Model):
    # ID do usuário (pode ser o ID de sessão, ID de um usuário logado, ou algo genérico)
    # Por simplicidade, usaremos um campo de texto que você pode preencher
    # com um ID de sessão ou 'anonimo' por enquanto.
    session_id = models.CharField(max_length=255, default='anonymous_session')
    
    sender = models.CharField(max_length=50) # 'user' ou 'bot'
    text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.sender} ({self.session_id}) at {self.timestamp}: {self.text[:50]}...'

    class Meta:
        ordering = ['timestamp'] # Garante que as mensagens são ordenadas por tempo

class ScrapedContent(models.Model):
    url = models.URLField(unique=True) # A URL da qual o conteúdo foi raspado
    content = models.TextField() # O conteúdo raspado
    # last_scraped: Quando foi a última vez que o conteúdo foi atualizado
    last_scraped = models.DateTimeField(default=timezone.now) 
    # next_scrape_due: Quando o conteúdo deve ser raspado novamente (para cache)
    next_scrape_due = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return f'Scraped: {self.url} (Last update: {self.last_scraped.strftime("%Y-%m-%d %H:%M")})'

    class Meta:
        verbose_name_plural = "Scraped Contents"