from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
import os, json
from collections import defaultdict

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
@login_required
def index():
    search = request.args.get("q", "")
    resultados = []

    for arquivo in sorted(os.listdir("output"), reverse=True):
        if arquivo.endswith(".json"):
            with open(f"output/{arquivo}", "r", encoding="utf-8") as f:
                dados = json.load(f)
                for item in dados:
                    if search.lower() in json.dumps(item).lower():
                        resultados.append(item)

    return render_template("index.html", resultados=resultados, search=search)

@main.route("/upload", methods=["GET", "POST"])
@login_required
def upload_keywords():
    if request.method == "POST":
        file = request.files.get("file")
        if file and file.filename.endswith((".txt", ".csv")):
            os.makedirs("keywords", exist_ok=True)
            file.save("keywords/palavras.txt")
            flash("Palavras-chave atualizadas com sucesso.")
            return redirect(url_for("main.index"))
        flash("Formato de arquivo inválido.")
    return render_template("upload.html")

@main.route("/dashboard")
@login_required
def dashboard():
    total_vazamentos = 0
    emails_total = 0
    cpfs_total = 0
    fontes = defaultdict(int)
    por_data = defaultdict(int)

    for arquivo in os.listdir("output"):
        if arquivo.endswith(".json"):
            with open(f"output/{arquivo}", "r", encoding="utf-8") as f:
                dados = json.load(f)
                for item in dados:
                    total_vazamentos += 1
                    emails_total += len(item.get("emails", []))
                    cpfs_total += len(item.get("cpfs", []))

                    if "pastebin" in item["url"]:
                        fontes["Pastebin"] += 1
                    elif "github" in item["url"]:
                        fontes["GitHub Gists"] += 1
                    elif ".onion" in item["url"]:
                        fontes["Dark Web"] += 1
                    else:
                        fontes["Outros"] += 1

                    data = arquivo.split("_")[-1].replace(".json", "")[:8]
                    por_data[data] += 1

    return render_template("dashboard.html",
                           total=total_vazamentos,
                           emails=emails_total,
                           cpfs=cpfs_total,
                           fontes=dict(fontes),
                           por_data=dict(por_data))