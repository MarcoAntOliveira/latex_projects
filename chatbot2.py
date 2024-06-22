import openai
import os
import json
import time

# Inicializa o cliente OpenAI com a chave de API
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion_with_retry(prompt, model='gpt-3.5-turbo', max_tokens=100, retries=5):
    for i in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Você é um assistente útil."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens
            )
            return response
        except openai.error.RateLimitError as e:
            print(f"RateLimitError: {e}")
            if i < retries - 1:
                wait_time = 2 ** i  # Exponential backoff
                print(f"Aguardando {wait_time} segundos antes de tentar novamente...")
                time.sleep(wait_time)
            else:
                print("Atingido o número máximo de tentativas.")
                raise

prompt = "Escreva uma introdução sobre a importância da inteligência artificial."

response = get_completion_with_retry(prompt)

if response:
    # Imprime o texto da primeira escolha
    print(response['choices'][0]['message']['content'].strip())

    # Imprime o uso da solicitação
    print(response['usage'])

    # Imprime a resposta em formato JSON com indentação
    print(json.dumps(response, indent=2))
