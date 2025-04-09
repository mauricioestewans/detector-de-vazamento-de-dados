from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from datetime import datetime
import os

def gerar_pdf_relatorio(resultados, empresa="Cliente Exemplo"):
    os.makedirs("relatorios", exist_ok=True)
    env = Environment(loader=FileSystemLoader("app/templates"))
    template = env.get_template("report.html")

    html_content = template.render(
        empresa=empresa,
        data=datetime.now().strftime("%d/%m/%Y %H:%M"),
        resultados=resultados
    )

    filename = f"relatorios/relatorio_{empresa}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    HTML(string=html_content).write_pdf(filename)
    print(f"[✔] Relatório salvo em: {filename}")
    return filename
