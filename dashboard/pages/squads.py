import streamlit as st
from streamlit import caching
import support.get_data as datos
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px 

def convocatorias():
    st.title("Convocatorias")
    lista_squads = datos.lista_squads()
    print(lista_squads)
    selected_country = st.selectbox("Elige Selecion", lista_squads)
    convocados = datos.get_squad_players(selected_country)["squad"]
    st.dataframe(pd.DataFrame(convocados))


