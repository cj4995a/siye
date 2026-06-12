from flask import Flask, request, jsonify
from supabase import create_client

app = Flask(__name__)

supabase = create_client(
SUPABASE_URL=https://qjugsyqxipscyrwxwbjo.supabase.co
SUPABASE_KEY=sb_publishable_mp4-U77QppB_RYk91FPf4g_ecBWd3sA
)

@app.route("/api/status", methods=["POST"])
def status():

    dados = request.json

    supabase.table(
        "dashboard_status"
    ).upsert({
        "unidade": dados["unidade"],
        "mensagem": dados["mensagem"],
        "atualizado": dados["atualizado"],
        "status": dados["status"]
    }).execute()

    return jsonify({"ok": True})
