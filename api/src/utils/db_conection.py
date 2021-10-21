from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
password = os.getenv("MONGO_PASS")
username = os.getenv("MONGO_USER")

url_db = f"mongodb+srv://{username}:{password}@cluster0.bk0gi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url_db)

db = client.get_database("euro_2020")
matchs = db.matchs
players = db.players
teams = db.teams
squads = db.squads