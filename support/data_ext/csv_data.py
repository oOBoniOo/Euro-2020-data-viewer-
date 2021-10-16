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
    return x

df["pens_home_score"] = df["pens_home_score"].apply(extract,dic = {"False":0})
df["pens_away_score"] = df["pens_away_score"].apply(extract,dic = {"False":0})

#Limpiamos columna "events_list"
def sust(x):
    return ["".join(re.findall(r"[a-zA-Z0-9:,\{\}''_-]",x))]

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