import smtplib
from email.message import EmailMessage

def send_email_alert(subject, body, to_email, smtp_config):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = smtp_config["from"]
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL(smtp_config["host"], smtp_config["port"]) as smtp:
        smtp.login(smtp_config["from"], smtp_config["password"])
        smtp.send_message(msg)
        print(f"[✔] Alerta enviado para {to_email}")
