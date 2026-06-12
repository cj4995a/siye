from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

ARQUIVO = "/tmp/status.json"

@app.route("/api/status", methods=["POST"])
def atualizar():

    dados = request.json

    status = {}

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            status = json.load(f)

    status[dados["unidade"]] = dados

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(
            status,
            f,
            ensure_ascii=False,
            indent=4
        )

    return jsonify({"ok": True})
