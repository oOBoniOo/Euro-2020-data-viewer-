import requests
import json
import pandas as pd
def get_matches():
    url="http://127.0.0.1:5000/matchs"
    partidos = requests.get(url).json()
    return partidos

def get_matchs_columns(columns):
    df = pd.DataFrame(get_matches())
    df = df[columns]
    return df

#Devuelve una serie de partidos segun parametros()
def search_matchs(parametros):
    url=f"http://127.0.0.1:5000/matchs/search"
    partidos = requests.get(url,params=parametros).json()
    return partidos

def lista_sel():
    url = "http://127.0.0.1:5000/matchs/list_sel"
    return requests.get(url).json()

def lista_squads():
    url = "http://127.0.0.1:5000/squads/list"
    return requests.get(url).json()

def get_squad_players(q):
    url = "http://127.0.0.1:5000/squads"
    dict = {"squad":q}
    return requests.get(url,params=dict).json()[0]



def get_goals(partidos):
    df = pd.DataFrame(partidos)
    print(df)
    g_home = df.groupby(["team_name_home"]).sum().reset_index()
    g_away = df.groupby(["team_name_away"]).sum().reset_index()
    new = pd.DataFrame([g_away["team_name_away"],g_away["team_away_score"],g_home["team_home_score"]])
    new = new.T
    new["tot"]= new["team_home_score"]+new["team_away_score"]
    new.rename(columns={'team_home_score': 'home', 
                           'team_away_score': 'away',
                           'team_name_away': 'team'}, inplace=True)
    return new

def get_player(n):
    url="http://127.0.0.1:5000/player"
    q = {
        "name":n
    }
    return requests.get(url,params=q).json()


def list_rounds():
    df = pd.DataFrame(get_matches())

    return df["stage"].unique()

def get_convocatoria(squad):
    url="http://127.0.0.1:5000/squad"
    squad = requests.get(url).json()

def get_titulares(team):
    partidos = search_matchs(team)
    titulares = []
    for partido in partidos:
        if partido["team_name_home"] == team:
            titulares.append(partido["lineup_home"])
        else:
            titulares.append(partido["lineup_home"])
    return titulares