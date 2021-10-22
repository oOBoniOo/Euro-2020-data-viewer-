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

    #convertir a dic y trabajar con ellos.
    name = request.json.get("name")
    p_photo = request.json.get("pphoto")
    contry = request.json.get("co")
    c_img = request.json.get("cimg")
    posicion = request.json.get("pos")
    club = request.json.get("club")
    club_img = request.json.get("clubimg")


    if not name:
        return {"Error":"jugador sin nombre"}
    else:   
        check = player_exists(name)
        if check:
            return check
        else:
            res = players.insert_one({
                "name":name,
                "p_photo":p_photo,
                "contry":contry,
                "c_img":c_img,
                "pos":posicion,
                "club":club,
                "club_img":club_img
                })
            return {
                "status":"OK. Jugador añadido.",
                "player_name": res.inserted_id
            }

def player_exists(name):
    res = list(players.find({"name":{"$regex":f".*{name.lower()}.*", "$options":"i"}}))
    if not res:
        return False
    else:
        return {
            "Error":"Ya existe un jugador con ese nombre",
            "player":res
        }