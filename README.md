# 🕵️‍♂️ Data Leak Watcher

O **Data Leak Watcher** é uma aplicação de cibersegurança para monitoramento de **vazamentos de dados sensíveis** na internet, surface web e dark web.

---

## 📸 Capturas de Tela

### 🔐 Login
![Login](https://i.imgur.com/QOtzSef.png)

### 📊 Dashboard
![Dashboard](https://i.imgur.com/vwCmE7F.png)

---

## 🚨 Funcionalidades

- 🔍 Busca em Pastebin, GitHub Gists e fóruns da dark web
- 📌 Detecção de e-mails, CPFs e palavras-chave
- 📤 Geração de **relatórios PDF**
- 🔔 Alerta via Telegram em tempo real
- 📊 Dashboard interativo com gráficos
- 🕘 Execução agendada automaticamente
- 🔐 Interface com autenticação protegida

---

## 🚀 Deploy Imediato

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/your-template-url)

---

## ⚙️ Tecnologias

- Python 3.10
- Flask
- WeasyPrint
- BeautifulSoup
- Chart.js
- Telegram Bot API
- Docker

---

## 📦 Instalação

### 💻 Local

```bash
git clone https://github.com/seuusuario/data-leak-watcher.git
cd data-leak-watcher
python -m venv venv
venv\\Scripts\\activate  # Windows
pip install -r requirements.txt
python run.py
