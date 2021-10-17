import requests
import json
def get_matches():
    url="http://127.0.0.1:5000/matchs"
    equipos = requests.get(url).json()
    return equipos

def search_matchs(parametros):
    url=f"http://127.0.0.1:5000/matchs/serach"
    equipos = requests.get(url,params=parametros).json()
    return equipos

def lista_sel():
    url = "http://127.0.0.1:5000/matchs/list_sel"
    return requests.get(url).json()