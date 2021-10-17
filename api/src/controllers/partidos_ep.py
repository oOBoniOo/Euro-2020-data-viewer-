from src.app import app
from flask import request
from src.utils.jsonMk import serialize
from src.utils.db_conection import matchs

@app.route("/matchs")
@serialize
def list_matchs():
    all_matchs = matchs.find({})
    return all_matchs

@app.route("/matchs/search")
@serialize
def search_matchs():
    s = request.args.get("stage")
    if s:
        stage = f".*{s.lower()}.*"
    else:
        stage = ".*"
    t =request.args.get("team") 
    if t:   
        team = f".*{t.lower()}.*"
    else:
        team = ".*"

    q = {
        "stage":{"$regex":stage, "$options":"i"},
        "$or":[
            {"team_name_home": {"$regex":team, "$options":"i"}},
            {"team_name_away": {"$regex":team, "$options":"i"}}
        ]
    }
    if s or t:
        partidos = matchs.find(q)
    else:
        partidos = {"No Data": "No se introdujo ningun criterio de busqueda"}
    return partidos

@app.route("/matchs/list_sel")
@serialize
def list_sels():
    all_matchs = matchs.find({}).distinct('team_name_home')
    return all_matchs