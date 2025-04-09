def carregar_palavras_chave():
    try:
        with open("keywords/palavras.txt", "r", encoding="utf-8") as f:
            palavras = [linha.strip().lower() for linha in f if linha.strip()]
            return palavras
    except FileNotFoundError:
        return []
