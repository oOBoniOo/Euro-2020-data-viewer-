import scrap as  exdata

select= int(input("1.Extraer jugadores \n 2.Extraer equipos"))
if select == 2:
    exdata.get_all_teams()
elif select == 1:
    exdata.get_all_players()
