import streamlit as st
from streamlit import caching
import support.get_data as datos
import requests
import pandas as pd
import matplotlib.pyplot as plt
import pages.partidos as pt
import pages.squads as sq
import pages.titulares as ti

st.image("img/e20b.png",width=None)
def load_matchs():
    return datos.get_matches()

col1, col2, col3= st.columns(3)

b1 = st.sidebar.radio("Datos:",["Partidos", "Selecciones", "Jugadores"])

if b1 == "Partidos":
    pt.menu_partidos()
elif b1 == "Selecciones":
    sq.convocatorias()
else:
    ti.mostrar_titulares()