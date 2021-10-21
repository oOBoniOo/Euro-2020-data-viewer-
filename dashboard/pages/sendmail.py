import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st

def send_mail(html):

    with st.form(key='email'):    
        sender_email = st.text_input("De:")
        receiver_email = st.text_input("Para:")
        password = st.text_input("Enter gmail password", type="password")
        asunto = "Datos Streamlit Dani"

        enviar = st.form_submit_button('Enviar')

        if enviar:

            message = MIMEMultipart("alternative")
            message["Subject"] = asunto
            message["From"] = sender_email
            message["To"] = receiver_email

            # Create the plain-text and HTML version of your message
            text = """\
            Datos del streamlit de Daniel """

            # Turn these into plain/html MIMEText objects
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            message.attach(part1)
            message.attach(part2)

            # Create secure connection with server and send email
            context = ssl.create_default_context()

            print("LLEGO AQUI")
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )