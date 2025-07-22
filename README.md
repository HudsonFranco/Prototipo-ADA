
# 🤖 Chatbot Inteligente – Jovem Programador 2025

Este projeto é um chatbot com Inteligência Artificial, desenvolvido para responder dúvidas sobre o curso **Jovem Programador**, interpretando dados reais do site oficial:  
🔗 https://www.jovemprogramador.com.br

---

## 📁 Estrutura do Projeto

```
CHATBOT_HACKATHON_JOVEM_PROGRAMADOR_SENAC2025/
├── App/                 # Diretório principal de aplicação (views, urls, etc.)
├── chatbot_api/         # Lógica de IA, scraping e integração com OpenAI
├── venv/                # Ambiente virtual (não versionado)
├── db.sqlite3           # Banco de dados local
├── .gitignore           # Arquivos/ pastas ignorados no Git
├── .gitattributes       # Configuração do GitHub para linguagens
├── LICENSE              # Licença do projeto
├── manage.py            # Utilitário principal do Django
├── README.md            # Documentação principal do projeto
└── requirements.txt     # Dependências Python do projeto
```

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/chatbot-hackathon-2025.git
cd chatbot-hackathon-2025
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o ambiente (se necessário)
Crie um `.env` ou defina variáveis diretamente no `settings.py`, como:
- `OPENAI_API_KEY`
- `DEBUG`
- `SECRET_KEY`

### 5. Execute as migrações e inicie o servidor
```bash
python manage.py migrate
python manage.py runserver
```

Acesse em: `http://127.0.0.1:8000/`

---

## ✅ Funcionalidades

- Recebe perguntas dos usuários por meio de uma API.
- Interpreta perguntas com base em conteúdo real do site oficial.
- Utiliza IA (OpenAI/ChatGPT) para formular respostas automáticas.
- Retorna mensagens padrão caso a informação não seja localizada.
- Interface web (em desenvolvimento ou separada, se for o caso).

---

## 🧪 Testes

Para rodar os testes (se existirem ou forem implementados):
```bash
python manage.py test
```

---

## 🧠 Requisitos Não Funcionais

- Código limpo, modular e documentado.
- Tempo de resposta médio inferior a 2 segundos.
- Layout e estrutura responsiva (para a interface).
- Segurança de dados sensíveis (uso de `.env` ou variáveis externas).
- Preparado para deploy em nuvem (Heroku, Render, etc.).

---

## 👥 Equipe

**Python Rangers** – Projeto Integrador | Jovem Programador 2025  
- Renato Teodoro  
- Matheus Moraes  
- Hudson Franco  
- Gustavo Lohn  
- Vinícius Seeling

---

## 📄 Licença

Este projeto é de uso educacional e colaborativo, voltado ao Hackathon do SENAC 2025.  
Licença: MIT/GPL
