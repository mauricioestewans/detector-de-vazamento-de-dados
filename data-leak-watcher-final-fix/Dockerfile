FROM python:3.13.2-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
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

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "run.py"]