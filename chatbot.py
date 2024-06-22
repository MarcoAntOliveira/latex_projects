from openai import OpenAI
import os
import json


client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))



# Inicializa o cliente OpenAI com a chave de API

# Faz uma solicitação de conclusão usando o modelo 'gpt-3.5-turbo' (um exemplo de modelo compatível)
response = client.chat.completions.create(model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user", "content": "Escreva uma introdução sobre a importância da inteligência artificial."}
    ],
    max_tokens=100)

# Imprime o texto da primeira escolha
print(response.choices[0].message.content.strip())

# Imprime o uso da solicitação
print(response.usage)

# Imprime a resposta em formato JSON com indentação
print(json.dumps(response, indent=2))
