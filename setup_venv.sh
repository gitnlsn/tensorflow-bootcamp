#!/bin/bash

# Nome do ambiente virtual (ajuste se necessário)
VENV_NAME="tfdeeplearning"
PYTHON_VERSION="3.12.3"  # Altere se precisar de outra versão

# Verifica se o Python 3.8 está instalado
if ! command -v python3.12 &>/dev/null; then
    echo "[ERRO] Python 3.8 não está instalado. Instale-o primeiro."
    exit 1
fi

# Cria o ambiente virtual
echo "Criando ambiente virtual '$VENV_NAME' com Python $PYTHON_VERSION..."
python3.12 -m venv "$VENV_NAME"

# Ativa o ambiente
echo "Ativando ambiente virtual..."
source "$VENV_NAME/bin/activate"

# Atualiza o pip
echo "Atualizando pip..."
pip install --upgrade pip

# Instala pacotes via pip (baseados no seu YAML)
echo "Instalando pacotes..."
pip install numpy pandas matplotlib scipy scikit-learn jupyter notebook ipython ipykernel ipywidgets requests jinja2 markupsafe tornado pyzmq traitlets tensorflow tensorboard protobuf markdown

# Verifica a instalação do TensorFlow
echo "Verificando TensorFlow..."
python -c "import tensorflow as tf; print(f'TensorFlow versão: {tf.__version__}')"

# Mensagem final
echo "Ambiente configurado com sucesso!"
echo "Para ativar manualmente:"
echo "source $VENV_NAME/bin/activate"