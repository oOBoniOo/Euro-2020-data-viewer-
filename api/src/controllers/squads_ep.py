from src.app import app
from flask import request
from src.utils.jsonMk import serialize
from src.utils.db_conection import squads
import numpy as np

def random_squad():
    all_squads = list(squads.find({}))
    random = np.random.choice(all_squads)
    return random



@app.route("/squad")
@serialize
def list_squad():
    squad = request.args.get("squad")
    if not country:
        player = random_squad()
    else:
        country = f".*{squad.lower()}.*"
        player = squads.find({"squad":{"$regex":country, "$options":"i"}})
    return player