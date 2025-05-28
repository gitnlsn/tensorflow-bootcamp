#!/bin/bash

VENV_NAME="tfdeeplearning"

if [ ! -d "$VENV_NAME" ]; then
    echo "[ERRO] Ambiente virtual '$VENV_NAME' não encontrado."
    echo "Execute primeiro: bash setup_venv.sh"
    exit 1
fi

if [ $# -eq 0 ]; then
    echo "[ERRO] Nenhum script Python especificado."
    echo "Uso: $0 <script.py> [argumentos...]"
    exit 1
fi

echo "Ativando ambiente virtual '$VENV_NAME'..."
source "$VENV_NAME/bin/activate"

if [ $? -ne 0 ]; then
    echo "[ERRO] Falha ao ativar o ambiente virtual."
    exit 1
fi

echo "Executando: python $@"
python "$@"
exit_code=$?

echo "Desativando ambiente virtual..."
deactivate

exit $exit_code 