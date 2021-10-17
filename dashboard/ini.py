import streamlit as st
from streamlit import caching
import support.get_data as datos
import requests

b1 = st.sidebar.button("Datos Selecciones")
b2 = st.sidebar.button("G2")
b3 = st.sidebar.button("G3")
b4 = st.sidebar.button("G4")

if b1:
    st.title("COSAS CON EQUIPOS")
    print(type(datos.lista_sel))
    st.multiselect("Elige selecion", datos.lista_sel())      