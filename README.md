# 🕵️‍♂️ Data Leak Watcher

O **Data Leak Watcher** é uma aplicação de cibersegurança desenvolvida para monitorar e detectar **vazamentos de dados sensíveis** na internet, surface web e dark web. Ideal para pequenas e médias empresas (PMEs), auditores de segurança e profissionais de TI preocupados com a exposição de seus dados.

---

## 🚨 Funcionalidades

- 🔍 Varredura automatizada de sites como:
  - Pastebin
  - GitHub Gists
  - Fóruns da dark web
- 📌 Detecção de:
  - E-mails
  - CPFs
  - Palavras-chave definidas pelo usuário
- 📤 Geração automática de **relatórios em PDF**
- 🔔 Alerta em tempo real via **Telegram Bot**
- 📊 Dashboard com gráficos de vazamentos detectados
- 🕘 Agendamento automático de verificações diárias
- 🔒 Interface web com login protegido

---

## 🖼️ Demonstração

<img src="https://i.imgur.com/xxxxxxx.png" width="600" alt="Dashboard">

---

## ⚙️ Tecnologias Utilizadas

- Python 3.10
- Flask
- WeasyPrint
- BeautifulSoup
- Chart.js (dashboard)
- Telegram API
- Docker (deploy opcional)

---

## 📦 Instalação

### 🔧 Requisitos
- Python 3.10+
- pip
- (Opcional) Docker

### 🧪 Instalação local (modo desenvolvedor)

```bash
git clone https://github.com/seuusuario/data-leak-watcher.git
cd data-leak-watcher
python -m venv venv
venv\\Scripts\\activate  # Windows
source venv/bin/activate # Linux/macOS
pip install -r requirements.txt
python run.py
