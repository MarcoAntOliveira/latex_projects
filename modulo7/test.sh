#!/bin/bash

# Verifica se o ambiente virtual já existe
if [ -d "venv" ]; then
    echo "O ambiente virtual já existe. Saindo..."
    exit 1
fi

# Cria o ambiente virtual
python3 -m venv venv

# Ativa o ambiente virtual no shell atual
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
else
    echo "Não foi possível encontrar o script de ativação do ambiente virtual."
    exit 1
fi

# Instala as dependências
pip install -r requirements.txt

echo "Ambiente virtual criado e ativado com sucesso."
