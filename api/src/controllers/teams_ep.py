from src.app import app
from flask import request
from src.utils.jsonMk import serialize
from src.utils.db_conection import teams
import numpy as np

def random_team():
    all_teams = list(teams.find({}))
    random = np.random.choice(all_teams)
    return random

#Buscamos un equipo por su nombre, si no recibimos parametros, se elige uno al azar.
#Parametros "name"
@app.route("/team")
@serialize
def list_team():
    nombre = request.args.get("name")
    if not nombre:
        player = random_team()
    else:
        nombre = f".*{nombre.lower()}.*"
        player = teams.find({"name":{"$regex":nombre, "$options":"i"}})
    return player