import os
from flask import flash

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
