import streamlit as st
from streamlit import caching
import support.get_data as datos
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.image("img/e20b.png",width=None)
@st.cache
def load_matchs():
    return datos.get_matches()

#partidos = pd.DataFrame(load_matchs())
#print(partidos)
#
goles = datos.get_goals()

col1, col2= st.columns(2)

st.dataframe(goles)
fig = plt.pie(goles["tot"], labels=goles["team"])
st.pyplot(fig)


#with col2:
    #fig = goles.plot.pie(y='tot')

    #st.plotly_chart(fig)




b0 = st.sidebar.button("Inicio")
b1 = st.sidebar.button("Datos Partidos")
if b1:
    st.title("COSAS CON EQUIPOS")
    print(type(datos.lista_sel))
    selec = st.multiselect("Elige selecion", datos.lista_sel())  


b2 = st.sidebar.button("Datos de Jugadores")
b3 = st.sidebar.button("Datos de ")
b4 = st.sidebar.button("G4")

   