from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

ARQUIVO = "/tmp/status.json"

@app.route("/api/dados")
def dados():

    if not os.path.exists(ARQUIVO):

        return jsonify({
            "Cajamar": {},
            "PTSams": {}
        })

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return jsonify(json.load(f))
