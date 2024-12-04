import streamlit as st
import pandas as pd
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import requests

# URL du fichier CSV (lien Github)
csv_url = "https://raw.githubusercontent.com/apail88/Streamlit_Part3/refs/heads/main/dataComptes.csv"

# Télécharger le CSV et charger dans un DataFrame
response = requests.get(csv_url)
if response.status_code == 200:
    with open("temp.csv", "wb") as file:
        file.write(response.content)

    # Charger le fichier CSV en DataFrame
    df = pd.read_csv("temp.csv")

    # Convertir le DataFrame en JSON
    lesDonneesDesComptes = {
    "usernames": df.set_index("username").to_dict(orient="index")
}


authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil(selection):

    # On indique au programme quoi faire en fonction du choix
    if selection == "👫 Accueil":
        st.title(">🎋 Welcome to the jungle 🎋<")
        st.image("https://images.hdqwalls.com/wallpapers/bthumb/jumanji-welcome-to-the-jungle-cast-5k-0.jpg")
        st.video("https://www.youtube.com/watch?v=9erLsEHAZRI", autoplay=True)
    elif selection == "🐐 Photos de ma chèvre":
        st.title("Elle est pas belle ma chèvre?")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("A la plage (Corse 2018)")
            st.image("https://th.bing.com/th/id/R.f7165aa341dd687eca800449d31d8f07?rik=XnWvERRPfsczig&riu=http%3a%2f%2f2.bp.blogspot.com%2f-hosgNheJHYw%2fU-qPcde9jAI%2fAAAAAAAAJqQ%2fZ-dX_L0vY2M%2fs1600%2fCreta_cabra2.jpg&ehk=2%2fmT6SNtlbsn6oH5wMZX51P8%2frUucShrRDMo4STicpQ%3d&risl=&pid=ImgRaw&r=0")
        with col2:
            st.write("A la neige (Hivers 2014)")
            st.image("https://d3e1m60ptf1oym.cloudfront.net/96023950-b3bb-4ab9-8767-a752e7e35310/chevre-montagne_xgaplus.jpg")
        with col3:
            st.write("Koh-Lanta (mars 2021)")
            st.image("https://static.pratique.fr/images/unsized/ar/arganier.jpg")
        st.video("https://www.youtube.com/watch?v=RVNw2OCCSmQ", autoplay=True)
    # ... et ainsi de suite pour les autres pages
        
        
    

if st.session_state["authentication_status"]:
    with st.sidebar :
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion")
        st.write(f"Bienvenue {st.session_state['name']}")
        # Création du menu qui va afficher les choix qui se trouvent dans la variable options
        selection = option_menu(
            menu_title=None,
            options = ["👫 Accueil", "🐐 Photos de ma chèvre"],
            default_index=0
            )
        st.write(f"email : {st.session_state['email']}")
        
    accueil(selection)


elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')


