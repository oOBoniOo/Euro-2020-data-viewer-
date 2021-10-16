from pymongo import MongoClient
import json
client = MongoClient()

db = client.get_database("euro_2020")


opc =input("Seleciona los datos a insertar en la MONGO:\n 1.Players \n 2.Teams")
datos = {
     "1":{
        "file":"../../data/players_bd.json",
        "co": db.players
        },
     "2":{
        "file":"../../data/teams_bd.json",
        "co": db.teams
        }
}

#Abriendo el archivo con la funcion open()
with open(datos[opc]["file"]) as file: 
    file_data = json.load(file) 
      
if isinstance(file_data, list): 
    datos[opc]["co"].insert_many(file_data)   
else: 
    datos[opc]["co"].insert_one(file_data)