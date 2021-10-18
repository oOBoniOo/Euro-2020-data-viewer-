import pandas as pd
from bson import json_util 
import re
import json


df = pd.read_csv("../../data/eurocup_2020_results.csv")

#Cambiamos "False" por 0 en columna de penalties
def extract(x,dic):
    for k,v in dic.items():
        if k.lower() in str(x).lower():
            return v
    return int(x)

def extract2(x,dic):
    for k,v in dic.items():
        if k.lower() in str(x).lower():
            return v
    return x


#eliminamos espacios ppio y final en las columnas de texto
for c in df.columns:
    if df[c].dtype == object:
        df[c] = df[c].apply(lambda x: x.strip())


df["pens_home_score"] = df["pens_home_score"].apply(extract,dic = {"False":0})
df["pens_away_score"] = df["pens_away_score"].apply(extract,dic = {"False":0})




df["stage"] = df["stage"].apply(extract2,dic = {
                                                "Semi-finals":"Semis",
                                                "Quarter-finals": "Quarters",
                                                "Group stage: Matchday 1":"G1",
                                                "Group stage: Matchday 2":"G2",
                                                "Group stage: Matchday 3":"G3"
                                              })

#Limpiamos columna "events_list"
def sust(x):
    return ["".join(re.findall(r"[a-zA-Z0-9:,\{\}''_-]",x))]

df["events_list"] = df["events_list"].apply(sust)

#Limpiamos y formateamos alineaciones
def chars(x):
    #specialChars = "[ ']"
    specialChars = "[]"
    for specialChar in specialChars:
        x = x.replace(specialChar, '')
        x = x.replace('"',"")
    
    return x.split(",")

def lineups(lista):
    dic = {}
    for i in range(0,len(lista),2):
        #print(i)
        #aux = {}
        name = lista[i].replace("{'Player_Name': '","").replace("'","")
        num = lista[i+1].replace(" 'Player_Number': '","").replace("'}","")
        #aux["name"] = lista[i].replace("{'Player_Name': '","").replace("'","")
        dic[num] = name
    return dic

df["lineup_home"] = df["lineup_home"].apply(chars)
df["lineup_home"] = df["lineup_home"].apply(lineups)

df["lineup_away"] = df["lineup_away"].apply(chars)
df["lineup_away"] = df["lineup_away"].apply(lineups)

df.to_csv('../../data/eurocup_2020_formated.csv', header=True, index=False)