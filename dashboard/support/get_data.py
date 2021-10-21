import requests
import json
import pandas as pd
#Obtenemos todos los partidos
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


#Devuelve lista de seleciones
def lista_sel():
    url = "http://127.0.0.1:5000/matchs/list_sel"
    return requests.get(url).json()

#Devuelve lista de seleciones
def lista_squads():
    url = "http://127.0.0.1:5000/squads/list"
    return requests.get(url).json()


#Devuelve convocadosde una de selecion
def get_squad_players(q):
    url = "http://127.0.0.1:5000/squads"
    dict = {"squad":q}
    return requests.get(url,params=dict).json()[0]


#Devuelve DataFrame con partidos|goles
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


#Devuelve datos de un jugador.
def get_player(n):
    url="http://127.0.0.1:5000/player/search"
    q = {
        "name":n
    }
    return requests.get(url,params=q).json()

#Devuelve lista de rondas
def list_rounds():
    df = pd.DataFrame(get_matches())
    return df["stage"].unique()


#Creamos df con equipo|lineup
def df_lineups(df):
    al_h = pd.DataFrame([df["team_name_home"],df["lineup_home"]]).T
    al_a = pd.DataFrame([df["team_name_away"],df["lineup_away"]]).T
    al_h = al_h.rename(columns={"team_name_home":"team","lineup_home":"lineup"})
    al_a = al_a.rename(columns={"team_name_away":"team","lineup_away":"lineup"})
    todas = pd.concat([al_h,al_a], ignore_index=True)
    return todas

#Recibe un dataframe de tipo "team"|"lineup" devuelve diccionario con titularidades
def get_titulares(df):
    dic = {}
    df_limpio = df_lineups(df)
    print(df_limpio)
    print("*"*100)
    for i in range(len(df_limpio.index)):
        if df_limpio["team"][i] not in dic.keys():
            dic[df_limpio["team"][i]] = {}
            for val in df_limpio["lineup"][i].values():
                if val not in dic[df_limpio["team"][i]].keys():
                    dic[df_limpio["team"][i]][val] = 1
        else:
            for val in df_limpio["lineup"][i].values():
                if val not in dic[df_limpio["team"][i]].keys():
                    dic[df_limpio["team"][i]][val] = 1
                else:
                    dic[df_limpio["team"][i]][val] += 1
    return dic