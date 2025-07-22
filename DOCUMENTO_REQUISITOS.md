
# 📄 Documento de Requisitos  
**Projeto Integrador – Chatbot Inteligente para o Jovem Programador**  
**Equipe:** Python Rangers  
**Ano:** 2025

---

## 🧠 Visão Geral

Este projeto tem como objetivo desenvolver um chatbot inteligente, utilizando Inteligência Artificial para responder dúvidas sobre o curso **Jovem Programador**, com base no conteúdo do site oficial:  
🔗 https://www.jovemprogramador.com.br

O sistema será dividido em duas etapas:

- **1º PI – Back-end:** API, scraping, processamento de perguntas e respostas via IA.  
- **2º PI – Front-end:** Interface web conectada à API, com boa experiência de usuário.

---

## ✅ Requisitos Funcionais

### 🔧 1º PI – Back-end

- [ ] API para envio de perguntas e recebimento de respostas.
- [ ] Módulo de leitura do conteúdo do site (crawler ou leitura de arquivo salvo).
- [ ] Módulo de interpretação das perguntas (análise inteligente do conteúdo).
- [ ] Módulo de resposta automática usando IA (sem cadastro manual de perguntas).
- [ ] Mensagem padrão amigável caso a informação não seja encontrada.
- [ ] Código limpo, documentado e versionado.

#### 📦 Entregáveis – Back-end
- Documento de requisitos (este).
- Código-fonte da API e módulos de IA.
- Scripts de uso da API.
- Relatório de testes realizados.
- Demonstração prática da API em funcionamento.

---

### 🖥️ 2º PI – Front-end

- [ ] Página web com campo de perguntas.
- [ ] Conexão com a API desenvolvida no 1º PI.
- [ ] Exibição das respostas do chatbot de forma clara e organizada.
- [ ] Aplicação de boas práticas de UX/UI.
- [ ] Layout responsivo (acessível em celulares, tablets e PCs).

#### 📦 Entregáveis – Front-end
- Documento de requisitos (este).
- Código-fonte da interface conectada à API.
- Protótipo de interface.
- Relatório de testes (funcionalidade e responsividade).
- Demonstração prática da aplicação web.

---

## 🚫 Requisitos Não Funcionais

- O sistema deve responder em até **2 segundos** em condições normais.
- As senhas e chaves devem ser armazenadas de forma segura (variáveis de ambiente).
- A API e o front-end devem ser documentados e seguir boas práticas de desenvolvimento.
- O projeto deve ser versionado no GitHub com histórico de contribuições da equipe.
- O código deve ser modular e reutilizável, facilitando manutenção e evolução.
- A interface deve ser clara, responsiva e acessível.
- O sistema deve funcionar em ambiente local e estar pronto para deploy em nuvem (Heroku, Render, etc.).
- Deve haver testes básicos automatizados e manuais (ex.: `python manage.py test`).

---

## 🔁 Fluxo Geral do Sistema

1. Usuário acessa a página web.
2. Digita uma pergunta.
3. A interface envia a pergunta para a API (`/chat/`).
4. A API interpreta a pergunta, decide se usa scraping, IA ou uma resposta padrão.
5. A resposta é enviada de volta à interface.
6. O usuário visualiza a resposta em tempo real.

---

## 🧩 Tecnologias Previstas

- Python 3.x + Django
- Biblioteca de scraping (ex: BeautifulSoup, requests)
- OpenAI API (ChatGPT)
- HTML, CSS, JavaScript (ou framework como React/Vue, se aplicável)
- Git + GitHub
- Deploy em nuvem (opcional)

---

## ✨ Equipe Responsável

**Python Rangers** – Jovem Programador 2025  
- Renato Teodoro  
- Matheus Moraes  
- Hudson Franco  
- Gustavo Lohn  
- Vinícius Costa
