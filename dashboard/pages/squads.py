from google.protobuf.symbol_database import Default
from requests.sessions import default_headers
import streamlit as st
from streamlit import caching
import support.get_data as datos
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px 

def convocatorias():
    st.title("Convocatorias")
    # Obtengo la lista de seleciones
    lista_squads = datos.lista_squads()

    #Desplegable para selecionar equipo
    selected_country = st.selectbox("Elige Selecion", lista_squads,index=0)

    #Conseguimos la lista de convocados de la selecion elegida.
    convocados = datos.get_squad_players(selected_country)["squad"]

    #Creamos columnas para los datos de convocatoria y jugadores
    c1,c2 = st.columns(2)

    #Creamos dataframe con los convocados y lo imprimimos en c1
    df_convocados = pd.DataFrame()
    df_convocados["Jugador"] = convocados
    c1.dataframe(df_convocados)

    #Creamos el desplegable de selecion de datos de jugadores
    selected_player = c2.selectbox("Elije un jugador",df_convocados["Jugador"])

    #Obtenemos ficha del jugador elejido.
    player= datos.get_player(selected_player)
    df_player = pd.DataFrame(player)

    c2.image(player[0]["p_photo"])
    c2.image(player[0]["club_img"])
    c2.dataframe(df_player[["name","posiciones","club"]])
    


