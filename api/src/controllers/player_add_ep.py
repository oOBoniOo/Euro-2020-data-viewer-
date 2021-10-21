from src.app import app
from flask import request
from src.utils.jsonMk import serialize
from src.utils.db_conection import players
from src.utils.error import MissingArgumentError, errorHandling

import numpy as np

@app.route("/player/add", methods=["GET", "POST"])
@errorHandling
@serialize
def add_player():
    if request.method == "GET":
        return get_insert_player()
    elif request.method == "POST":
        return insert_player()

def get_insert_player():
    return {
        "Error":"Not Allowed",
        "Message":"If you wish to contribute, please contact the develop team"
    }

def insert_player():
    name = request.json.get("name")
    if not name:
        raise MissingArgumentError("name")
    force = request.json.get("force")
    if force != "true":
        check = checkAuthorExists(name)
        if check:
            return check
    res = authors.insert_one({"name":name})
    return {
        "status":"OK. Jugador añadido.",
        "player_name": res.inserted_id
    }

def checkAuthorExists(name):
    res = list(players.find({"name":{"$regex":f".*{name.lower()}.*", "$options":"i"}}))
    if not res:
        return False
    else:
        return {
            "Error":"Ya existe un jugador con ese nombre",
            "player":res
        }