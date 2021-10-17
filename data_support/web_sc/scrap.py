import requests
from bs4 import BeautifulSoup
import json
import re


#funcion para extraer las imagenes
def get_img(tag):
    pattern = r'src=\".*\"'
    link_img = re.findall(pattern,str(tag))[0]
    link_img = link_img.replace("src=","").replace('"',"").strip()
    return link_img 

#funcion que extrae la info de cada jugador
def get_player_data(player):
    player_data = {}
    pos = []   
    #a CLASE link-player
    c_link_player = player.select("a[class=link-player]")   
    #a CLASE link-nation
    c_link_nation = player.select("a[class=link-nation]")[0]
    for e in player.select("a[class=link-position]"):
        pos.append(e.text)
    #a CLASE link-team
    c_link_team = player.select("a[class=link-team]")[0]
    
    player_data ={
        "name": c_link_player[1].text,
        "p_photo": get_img(c_link_player[0]),
        "contry": c_link_nation.get("title"),
        "c_img": get_img(c_link_nation),
        "posiciones": pos,
        "club":c_link_team.get("title").replace(" FIFA 21",""),
        "club_img":get_img(c_link_team)
    }                           
    return player_data


#Recorremos todas las paginas de jugadores de fifaindex y obtenemos la informacion de todos ellos
def get_all_players():
    tf = open("../../data/players_bd.json", "w")

    #conseguimos numero de paginas de jugadores total:
    direc = f"https://www.fifaindex.com/players/?page=2"
    peticion = requests.get(direc)
    soup_page = BeautifulSoup(peticion.text)
    ptot = int(soup_page.select("#bigpagination > nav:nth-child(1) > ul > li:nth-child(13) > a")[0].get("href").replace("'","").replace("?page=",""))

    bd = []
    for i in range(1,ptot + 1):
        direc = f"https://www.fifaindex.com/players/?page={i}"
        peticion = requests.get(direc)
        soup_page = BeautifulSoup(peticion.text)
        
        jug = soup_page.select("tr[data-playerid]")

        long = len(jug)
        for j in range(0,long):
            print(f"Procesando pagina {i} de 632, jugador {j}")
            bd.append(get_player_data(jug[j]))
    json.dump(bd,tf)                  
    tf.close()



def get_team_data(team):
    player_data = {}
    pos = []   
    #a CLASE link-league
    c_link_team = team.select("a[class=link-team]") 
    #a CLASE link-team
    c_link_league = team.select("a[class=link-league]")[0]
    
    team_data ={
        "name": c_link_team[1].text,
        "t_flag": get_img(c_link_team[0]),
        "league":c_link_league.text
    }
    return team_data


def get_all_teams():
    tf = open("../../data/teams_bd.json", "w")
    bd = []
    for i in range(1,24):
        direc = f"https://www.fifaindex.com/teams/?page={i}"
        peticion = requests.get(direc)
        soup_page = BeautifulSoup(peticion.text)
        eqs = soup_page.select("body > main > div > div > div> div> table > tbody > tr:nth-of-type(n+3)")

        long = len(eqs)
        for j in range(0,long):
            if (len(eqs[j].select("td[colspan]")) > 0) or (len(eqs[j])== 0):
                print(f"Procesando pagina {i} de 23, equipo {j} NO es equipo")
            else:
                print(f"Procesando pagina {i} de 23, equipo {j}")
                bd.append(get_team_data(eqs[j]))
    json.dump(bd,tf)             
    tf.close()