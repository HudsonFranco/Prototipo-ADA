# chatbot_app/services.py

import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def get_openai_response(prompt_text, history=None, system_prompt_override=None):
    """
    Envia um prompt para a API da OpenAI e retorna a resposta do modelo.
    Permite sobrescrever o system_prompt e incluir um histórico de conversa.
    """
    try:
        initial_system_prompt = system_prompt_override if system_prompt_override else "Você é uma assistente prestativa, jovem, muito educada e amigável."

        messages = [{"role": "system", "content": initial_system_prompt}]

        if history:
            messages.extend(history)
        
        messages.append({"role": "user", "content": prompt_text})

        chat_completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=500,  
            temperature=0.7,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Erro ao chamar a API da OpenAI: {e}")
        return "Desculpe, não consegui processar sua solicitação no momento."