from flask import Blueprint, render_template, request
import os
import json

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
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
from flask_login import login_required
...

@main.route("/", methods=["GET"])
@login_required
def index():
    ...
