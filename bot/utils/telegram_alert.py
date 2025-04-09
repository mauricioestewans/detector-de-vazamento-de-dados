from telegram import Bot

def enviar_alerta_telegram(token, chat_id, mensagem):
    try:
        bot = Bot(token=token)
        bot.send_message(chat_id=chat_id, text=mensagem)
        print(f"[✔] Alerta enviado para Telegram ID {chat_id}")
    except Exception as e:
        print(f"[!] Falha ao enviar alerta: {e}")

