@app.route("/api/dados")
def dados():

    consulta = supabase.table(
        "dashboard_status"
    ).select("*").execute()

    retorno = {}

    for linha in consulta.data:

        retorno[linha["unidade"]] = {
            "mensagem": linha["mensagem"],
            "atualizado": linha["atualizado"],
            "status": linha["status"]
        }

    return jsonify(retorno)
