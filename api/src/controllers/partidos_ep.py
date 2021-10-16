from src.app import app
from flask import request
from src.utils.jsonMk import serialize
from src.utils.db_conection import matchs

@app.route("/matchs")
@serialize
def list_matchs():
    all_matchs = matchs.find({})
    return all_matchs

