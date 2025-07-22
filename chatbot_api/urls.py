# chatbot_app/urls.py

from django.urls import path
from . import views

app_name = 'chatbot_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('oque/', views.oque, name='oque'),
    path('como-funciona/', views.como_funciona, name='como_funciona'),
    path('componentes-chaves/', views.componentes_chaves, name='componentes_chaves'),
    path('chat/', views.chatbot_view, name='chatbot_view'),
    path('sobre-nos/', views.sobre_nos, name='sobre_nos'),
    path('arquivos/', views.arquivos, name='arquivos'),
    path('consideracoes/', views.consideracoes, name='consideracoes'),
    path('readme/', views.readme, name='readme'),
    path('doc/', views.readme, name='doc'),
]