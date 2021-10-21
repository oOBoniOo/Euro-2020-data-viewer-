import streamlit as st
def add_p():
    with st.form(key='email'):    
        nombre = st.text_input("Nombre de jugador")
        p_photo = st.text_input("Link foto")
        contry = st.text_input("Pais(en ingles)")
        c_img = st.text_input("Link bandera")
        posicion = st.text_input("Posición favorita")
        club = st.text_input("Club")
        club_img = st.text_input("Link escudo")


        enviar = st.form_submit_button('Enviar')
