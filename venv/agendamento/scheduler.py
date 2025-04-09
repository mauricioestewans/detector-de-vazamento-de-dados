import schedule
import time
import subprocess

def rodar_script():
    print("[⏱] Executando verificação automática...")
    subprocess.run(["python", "main.py"])

# Agendar para rodar diariamente às 08:00
schedule.every().day.at("08:00").do(rodar_script)

print("[✔] Agendador iniciado. Aguardando horário programado...")
while True:
    schedule.run_pending()
    time.sleep(60)
