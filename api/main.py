from src.controllers.partidos_ep import app
from src.controllers.home_ep import app
from src.controllers.players_ep import app
from src.controllers.teams_ep import app
from src.controllers.squads_ep import app
from src.controllers.player_add_ep import app
import os 
port = os.getenv("PORT") or 5000
app.run(debug=True, port=port, host="0.0.0.0")