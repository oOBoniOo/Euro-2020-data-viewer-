import streamlit as st
from streamlit import caching
import support.get_data as datos
import pandas as pd
import matplotlib.pyplot as plt

# ['stage', 'date', 'pens', 'pens_home_score', 'pens_away_score',
#        'team_name_home', 'team_name_away', 'team_home_score',
#        'team_away_score', 'possession_home', 'possession_away',
#        'total_shots_home', 'total_shots_away', 'shots_on_target_home',
#        'shots_on_target_away', 'duels_won_home', 'duels_won_away',
#        'events_list', 'lineup_home', 'lineup_away']


def mostrar_partidos():
    col1, col2, col3= st.columns(3)
    st.title("COSAS CON EQUIPOS")
    with col1:
        lista_rondas = list(datos.list_rounds())
        lista_rondas.append("Todas")
        selected_ronda = st.multiselect("Elige Ronda", lista_rondas)  
    with col2:
        selected_team = st.multiselect("Elige Selecion", datos.lista_sel())


    partis = datos.get_matchs_columns(['stage','team_name_home', 'team_name_away', 'team_home_score','team_away_score'])


    if  "Todas" not in selected_ronda:
        df = pd.DataFrame(partis)
        df = df[df["stage"].isin(selected_ronda)]
    else:
        df = pd.DataFrame(partis)
        pass
    
    if  "Todas" not in selected_team:
        df = pd.DataFrame(partis)
        df = pd.concat([df[df['team_name_home'].isin(selected_team)],df[df['team_name_away'].isin(selected_team)]]).sort_values(by=["stage"])
    else:
        df = pd.DataFrame(partis)
        pass


    st.dataframe(df)

