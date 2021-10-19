from src.app import app
from flask import request
from src.utils.jsonMk import serialize
from src.utils.db_conection import squads
import numpy as np

def random_squad():
    all_squads = list(squads.find({}))
    random = np.random.choice(all_squads)
    return random

@app.route("/squads/list")
@serialize
def lista():
    all_countries = squads.find({}).distinct('country')
    return all_countries

@app.route("/squads")
@serialize
def list_squad():
    country = request.args.get("squad")
    print(country)
    if not country:
        squad = random_squad()
    else:
        country = f".*{country.lower()}.*"
        squad = squads.find({"country":{"$regex":country, "$options":"i"}})
    return squad