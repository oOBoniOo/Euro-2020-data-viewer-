from src.app import app
from flask import request
from src.utils.jsonMk import serialize
from src.utils.db_conection import players
import numpy as np


def random_player():
    all_players = list(players.find({}))
    random = np.random.choice(all_players)
    return random

#Buscamos un jugadore por su nombre, si no recibimos parametros, se elige uno al azar.
#Parametros "name"
@app.route("/player")
@serialize
def list_player():
  
    nombre = request.args.get("name")
    if not nombre:
        player = random_player()
    else:
        nombre = f".*{nombre.lower()}.*"
        player = players.find({"name":{"$regex":nombre, "$options":"i"}})
    return player

#Podemos buscar jugadores por parametros name, club(equipo en el que juega) o pos(posicion)

@app.route("/player/search")
@serialize
def search_players():
    n = request.args.get("name")
    if n:
        nombre = f".*{n.lower()}.*"
    else:
        nombre = ".*"
    p =request.args.get("pos") 
    if p:   
        position = f".*{p.lower()}.*"
    else:
        position = ".*"
    e = request.args.get("club")
    if e:
        equipo = f".*{e.lower()}.*"
    else: 
        equipo = ".*"
    q = {
        "name":{"$regex":nombre, "$options":"i"},
        "posiciones": {"$regex":position, "$options":"i"},
        "club": {"$regex":equipo, "$options":"i"}    
    }
    if n or p or e:
        player = players.find(q)
    else:
        player = {"No Data": "No se introdujo ningun criterio de busqueda"}
    return player
