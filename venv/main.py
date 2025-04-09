print("[+] Buscando pastes recentes...")
links = get_recent_pastes(limit=3)

all_results = []
for link in links:
    print(f"\n[+] Analisando {link}")
    resultado = extract_data_from_paste(link)
    if resultado and (resultado['emails'] or resultado['cpfs']):
        all_results.append(resultado)

if all_results:
    save_to_json(all_results)
else:
    print("[!] Nenhum dado sensível encontrado.")

from crawler.pastebin_scraper import get_recent_pastes, extract_data_from_paste
from crawler.github_gist_scraper import get_recent_gists, extract_data_from_gist
from utils.storage import save_to_json

all_results = []

# Pastebin
print("\n[+] Buscando no Pastebin...")
for link in get_recent_pastes(limit=3):
    res = extract_data_from_paste(link)
    if res and (res["emails"] or res["cpfs"]):
        all_results.append(res)

# GitHub Gists
print("\n[+] Buscando no GitHub Gists...")
for link in get_recent_gists(limit=3):
    res = extract_data_from_gist(link)
    if res and (res["emails"] or res["cpfs"]):
        all_results.append(res)

# Salvar resultados
if all_results:
    save_to_json(all_results)
else:
    print("[!] Nenhum dado sensível encontrado.")

from crawler.darkweb_scraper import scrape_dark_forum

print("\n[+] Buscando em fórum da Dark Web...")
darkweb_results = scrape_dark_forum("http://duskgytldkxiuqc6.onion", limit_pages=1)
all_results.extend(darkweb_results)
from utils.keywords import carregar_palavras_chave

palavras = carregar_palavras_chave()
for palavra in palavras:
    if palavra in dados_texto.lower():
        salvar_resultado(vazamento)
from utils.pdf_report import gerar_pdf_relatorio

if all_results:
    save_to_json(all_results)
    gerar_pdf_relatorio(all_results, empresa="Minha Empresa LTDA")
else:
    print("[!] Nenhum dado sensível encontrado.")
from utils.telegram_alert import enviar_alerta_telegram

TELEGRAM_TOKEN = "SEU_TOKEN_AQUI"
TELEGRAM_CHAT_ID = "SEU_CHAT_ID_AQUI"

if all_results:
    save_to_json(all_results)
    gerar_pdf_relatorio(all_results, empresa="Minha Empresa LTDA")

    # Mensagem resumida
    resumo = f"🚨 {len(all_results)} vazamentos encontrados!\n"
    for item in all_results[:3]:  # mostra só os 3 primeiros
        resumo += f"\n🔗 {item['url']}\n📧 {len(item['emails'])} emails | CPF: {len(item['cpfs'])}"

    enviar_alerta_telegram(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, resumo)
else:
    print("[!] Nenhum dado sensível encontrado.")
