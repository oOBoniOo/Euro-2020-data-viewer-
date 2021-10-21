import requests
from bs4 import BeautifulSoup
import re
import json
from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv
from pymongo import MongoClient

x = "Italy"
url = f"https://www.goal.com/en-qa/lists/euro-2020-squads/120zvuewm6geh11kkoe59otixw#cs0cab15f09c912520"

res = requests.get(url)

soup = BeautifulSoup(res.text)

sel = soup.select("h2, p > strong")

sel[5].parent.text.split(":")[1].split(",")
str(sel[6].name)

convocatorias = []
aux = {}
list = []
for i in sel:
    if str(i.name) == "h2":
        aux["country"] = i.get_text(strip=True).strip()
        print(i.get_text(strip=True).strip())
    if str(i.name) == "strong":
        if i.text.strip() == "Goalkeepers:":
            [list.append(el.strip()) for el in i.parent.get_text(strip=True).split(":")[1].split(",")]
        if i.text.strip() == "Defenders:":
            [list.append(el.strip()) for el in i.parent.get_text(strip=True).split(":")[1].split(",")]
        if i.text.strip() == "Midfielders:":
            [list.append(el.strip()) for el in i.parent.get_text(strip=True).split(":")[1].split(",")]
        if i.text.strip() == "Attackers:" or i.text.strip() == "Forwards:":
            [list.append(el.strip()) for el in i.parent.get_text(strip=True).split(":")[1].split(",")]
            aux["squad"] = list
            convocatorias.append(aux)
            list = []
            aux = {}


df = pd.DataFrame(convocatorias)

load_dotenv()
password = os.getenv("MONGO_PASS")
username = os.getenv("MONGO_USER")

url_db = f"mongodb+srv://{username}:{password}@cluster0.bk0gi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url_db)

db = client.get_database("euro_2020")

res = db.squads.delete_many({})

db.squads.insert_many(df.to_dict('records'))