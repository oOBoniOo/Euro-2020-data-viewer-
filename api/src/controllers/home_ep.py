from src.app import app
from src.utils.jsonMk import serialize
#from src.utils.error import errorHandling

@app.route("/")
#@errorHandling
@serialize
def home():
    return {
        "Welcome":"EURO 2020 API"
    }