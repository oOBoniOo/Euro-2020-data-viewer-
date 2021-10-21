import streamlit as st
from streamlit import caching
import support.get_data as datos
import pages.sendmail as mail
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px 
import pdfkit as pdf
import base64
# ['stage', 'date', 'pens', 'pens_home_score', 'pens_away_score',
#        'team_name_home', 'team_name_away', 'team_home_score',
#        'team_away_score', 'possession_home', 'possession_away',
#        'total_shots_home', 'total_shots_away', 'shots_on_target_home',
#        'shots_on_target_away', 'duels_won_home', 'duels_won_away',
#        'events_list', 'lineup_home', 'lineup_away']

def menu_partidos():
    st.title("Datos de partidos")
    selected_option= st.selectbox("Local/Visitante", ["Goles","Disparos","Posesion"])  
    if selected_option == "Goles":
        mostrar_goles()

def mostrar_goles():
    st.title("Goles por selección")
    col1, col2= st.columns(2)
    with col1:
        lista_teams = datos.lista_sel()
        lista_teams.append("Todas")
        selected_team = st.multiselect("Elige Selecion", lista_teams, default="Todas")
    with col2:
        lista_ha = ["Local","Visitante","Todo"]
        selected_home_away= st.selectbox("Local/Visitante", lista_ha)          


    partis = datos.get_matchs_columns(['stage','team_name_home', 'team_name_away', 'team_home_score','team_away_score'])
    g_home = partis.groupby(["team_name_home"]).sum().reset_index()[["team_name_home","team_home_score"]]
    g_away = partis.groupby(["team_name_away"]).sum().reset_index()[["team_name_away","team_away_score"]]
    df = pd.DataFrame([g_away["team_name_away"],g_home["team_home_score"],g_away["team_away_score"]])
    df = df.T
    df["tot"]= df["team_home_score"]+df["team_away_score"]
    df.rename(columns={'team_home_score': 'home', 
                        'team_away_score': 'away',
                        'team_name_away': 'team'}, inplace=True)


    def selector(s_r,datos,name="team"):
        if s_r.lower() == "local":
            #Grafico goles local
            fig = px.pie(datos, values='home', names=name,title="Goles como local")
        elif s_r.lower() == "visitante":
            #Grafico goles visitante
            fig = px.pie(datos, values='away', names=name,title="Goles como visitante")
        else:
            #Grafico goles totales
            fig = px.pie(datos, values='tot', names=name,title="Goles totales")
        return fig



    if  "Todas" not in selected_team:
        if len(selected_team) == 1:
            df = df[df['team'].isin(selected_team)]
            nuevodf = df.T
            nuevodf = nuevodf.drop(["team"],axis=0)
            fig = px.pie(nuevodf,nuevodf.columns[0],  title="Goles totales")

    
        else:
            df = df[df['team'].isin(selected_team)]
            fig = selector(selected_home_away,df)
    else:
        fig = selector(selected_home_away,df)

    c1,c2 = st.columns(2)



    c2.write(fig)

    c1.dataframe(df)

    def get_table_download_link(df):
        """Generates a link allowing the data in a given panda dataframe to be downloaded
        in:  dataframe
        out: href string
        """

        df.to_html("df.html")
        pdf.from_file("df.html","df.pdf")
        
        return f'<a href="df.pdf" download="df.pdf">Download PDF</a>'

    c1, c2 =st.columns(2)
    export_pdf = c1.button("Exportar datos en PDF")
    send_mail = c2.button("Enviar por mail")

    if export_pdf:
        st.markdown(get_table_download_link(df), unsafe_allow_html=True)

    if send_mail:
        mail.send_mail(df.to_html)
