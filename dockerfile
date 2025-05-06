# Base Python
FROM python:3.13.3-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libpq-dev \
    libssl-dev \
    libxml2 \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    shared-mime-info \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    && apt-get clean

# Copiar o projeto
WORKDIR /app
COPY . /app

# Instalar dependências Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expor a porta
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "run.py"]
