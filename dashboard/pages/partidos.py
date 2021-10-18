import streamlit as st
from streamlit import caching
import support.get_data as datos
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px 

# ['stage', 'date', 'pens', 'pens_home_score', 'pens_away_score',
#        'team_name_home', 'team_name_away', 'team_home_score',
#        'team_away_score', 'possession_home', 'possession_away',
#        'total_shots_home', 'total_shots_away', 'shots_on_target_home',
#        'shots_on_target_away', 'duels_won_home', 'duels_won_away',
#        'events_list', 'lineup_home', 'lineup_away']


def mostrar_partidos():
    
    st.title("COSAS CON EQUIPOS")
    col1, col2, col3= st.columns(3)
    with col1:
        lista_teams = datos.lista_sel()
        lista_teams.append("Todas")
        selected_team = st.multiselect("Elige Selecion", lista_teams, default="Todas")
    with col2:
        lista_ha = ["Local","Visitante"]
        selected_ronda = st.multiselect("Local/Visitante", lista_ha)          
    
    with col3:
        lista_rondas = list(datos.list_rounds())
        lista_rondas.append("Todas")
        selected_ronda = st.multiselect("Elige Ronda", lista_rondas, default="Todas")  

    partis = datos.get_matchs_columns(['stage','team_name_home', 'team_name_away', 'team_home_score','team_away_score'])
    g_home = partis.groupby(["team_name_home"]).sum().reset_index()[["team_name_home","team_home_score"]]
    g_away = partis.groupby(["team_name_away"]).sum().reset_index()[["team_name_away","team_away_score"]]
    df = pd.DataFrame([g_away["team_name_away"],g_home["team_home_score"],g_away["team_away_score"]])
    df = df.T
    df["tot"]= df["team_home_score"]+df["team_away_score"]
    df.rename(columns={'team_home_score': 'home', 
                        'team_away_score': 'away',
                        'team_name_away': 'team'}, inplace=True)


    print("ESTOY> POR AQUI")
    print(partis)

    if  "Todas" not in selected_team:
        df = df[df['team'].isin(selected_team)]
        print(df)
    else:
        pass
    print(f"estoy aqui fuera \n {df}")  
    # if  "Todas" not in selected_ronda:
    #     #df = pd.DataFrame(partis)
    #     df = df[df["stage"].isin(selected_ronda)]

    print(f"estoy fuera del if de las rondas \n {df}")

    
    c1,c2,c3 = st.columns(3)
    fig1 = px.pie(df, values='home', names="team",title="Goles como local")
    fig2 = px.pie(df, values='away', names="team",title="Goles como visitante")
    fig3 = px.pie(df, values='tot', names="team",title="Goles totales")
    st.write(fig1)
    st.write(fig2)
    st.write(fig3)

    st.dataframe(df)







    



    
    print("LLEGO AQUI")
    #st.dataframe(df)

