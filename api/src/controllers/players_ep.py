from src.app import app
from flask import request
from src.utils.jsonMk import serialize
from src.utils.db_conection import players
import numpy as np


def random_player():
    all_players = list(players.find({}))
    random = np.random.choice(all_players)
    return random


@app.route("/players")
@serialize
def list_player():
  
    nombre = request.args.get("name")
    if not nombre:
        player = random_player()
    else:
        nombre = f".*{nombre.lower()}.*"
        player = players.find({"name":{"$regex":nombre, "$options":"i"}})
    return player

@app.route("/players/search")
@serialize
def search_players():
    nombre = request.args.get("name")
    if nombre:
        nombre = f".*{nombre.lower()}.*"
    else:
        nombre = ".*"
    position =request.args.get("pos") 
    if position:   
        position = f".*{position.lower()}.*"
    else:
        position = ".*"
    equipo = request.args.get("club")
    if equipo:
        equipo = f".*{equipo.lower()}.*"
    else: 
        equipo = ".*"
    q = {
        "name":{"$regex":nombre, "$options":"i"},
        "posiciones": {"$regex":position, "$options":"i"},
        "club": {"$regex":equipo, "$options":"i"}    
    }

    player = players.find(q)
    return player
