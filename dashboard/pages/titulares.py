from google.protobuf.symbol_database import Default
from plotly.express import colors
from requests.sessions import default_headers
import streamlit as st
from streamlit import caching
import support.get_data as datos
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px 

def mostrar_titulares():
    partidos = pd.DataFrame(datos.get_matches())
    titulares = datos.get_titulares(partidos)
    selected = st.selectbox("Elige selección:", titulares.keys())
    nombres=titulares[selected].keys()
    cuenta = titulares[selected].values()

    fig = px.bar(y=cuenta, x=nombres, title= "Numero de titularidades por jugador")
    fig.update_xaxes(title_text='Jugadores') 
    fig.update_yaxes(title_text='Titularidades') 
    
    st.write(fig)

