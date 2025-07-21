# Chatbot Inteligente para o Jovem Programador

## Visão Geral

Este repositório contém a API backend para o chatbot inteligente do curso Jovem Programador. Ele é responsável por:
* Realizar web scraping no site oficial (`https://www.jovemprogramador.com.br`) para coletar informações sobre o curso.
* Utilizar Inteligência Artificial (PLN) para interpretar perguntas dos usuários.
* Gerar respostas automáticas com base nas informações extraídas do site.
* Fornecer uma mensagem padrão caso a informação não seja encontrada.

## Módulo do Projeto (1º PI - Back-end)

Este módulo foca na criação da API, estruturação da coleta e interpretação de informações do site, e resposta via IA.

## Tecnologias Utilizadas

* **Python 3.x**
* **Django**: Framework web para o backend.
* **Django REST Framework**: Para construção da API RESTful.
* **requests**: Para requisições HTTP (web scraping).
* **BeautifulSoup4**: Para parsear HTML e extrair dados (web scraping).
* **spaCy / NLTK**: Para Processamento de Linguagem Natural (PLN) e busca inteligente.
* **scikit-learn**: Para cálculo de similaridade e outras técnicas de ML.

## Como Configurar o Ambiente de Desenvolvimento

Siga estes passos para configurar seu ambiente local e começar a desenvolver:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/MatheusAntonioo/ChatBot_Hackathon_Jovem_Programador_Senac2025](https://github.com/MatheusAntonioo/ChatBot_Hackathon_Jovem_Programador_Senac2025)
    cd ChatBot_Hackathon_Jovem_Programador_Senac2025
    ```

2.  **Crie e ative o Ambiente Virtual (`venv`):**
    É altamente recomendado usar um ambiente virtual para gerenciar as dependências do projeto.

    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure sua Chave da API da OpenAI:**
    * Obtenha sua chave da API da OpenAI no [site da OpenAI](https://platform.openai.com/account/api-keys).
    * Na **raiz do projeto** (ao lado do arquivo `manage.py`), crie um novo arquivo chamado `.env`.
    * Dentro do arquivo `.env`, adicione a seguinte linha, substituindo `SUA_CHAVE_DA_OPENAI` pela sua chave real:
        ```
        OPENAI_API_KEY="SUA_CHAVE_DA_OPENAI"
        ```
    * **Atenção:** O arquivo `.env` é ignorado pelo Git (não será versionado) por motivos de segurança. Nunca compartilhe sua chave de API publicamente!

5.  **Execute as Migrações do Django:**
    ```bash
    python manage.py migrate
    ```

6.  **Crie um Superusuário (Opcional, para acessar o Admin do Django):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Inicie o Servidor de Desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
    O servidor estará disponível em `http://127.0.0.1:8000/`.

## Estrutura do Projeto