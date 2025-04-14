# Data Leak Watcher

Sistema de monitoramento de vazamentos de dados com painel web, alertas por Telegram, exportação de relatórios PDF e dashboard interativo.

## Como rodar localmente

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## Como rodar via Docker

```bash
docker build -t data-leak-watcher .
docker run -d -p 5000:5000 --name dlw data-leak-watcher
```