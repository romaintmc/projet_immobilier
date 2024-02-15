import streamlit as st
import requests

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def post_data(url, data):
    response = requests.post(url, json=data)
    return response.status_code

st.title('Trouver le m2 par ville et quartier')
villes = get_data('http://127.0.0.1:5000/villes')
option1 = st.selectbox('Choisir une ville',villes)
#st.write('Ville sélectionnée :', option1)
quartier = get_data(f'http://127.0.0.1:5000/quartiers/{option1}')
option2 = st.selectbox('Choisir un quartier',quartier)
#st.write('Quartier sélectionné :', option2)

if option1 and option2:
    response = get_data(f'http://127.0.0.1:5000/prix/{option2}/{option1}')
    if response:
        prix = response.get("prix", "Non disponible")
        st.write(f'Le prix au m² pour {option2}, {option1} est : {prix}')
    else:
        st.write("Informations sur les prix indisponibles.")

st.write("Mise à jour du prix au m²")
prix_input = st.number_input("Entrer le nouveau prix au m²", min_value=0.0, format="%f")
if st.button("Mettre à jour le prix"):
    if option1 and option2 and prix_input:
        update_response = post_data(f'http://127.0.0.1:5000/prix/{option2}/{option1}', {'prix': prix_input})
        if update_response == 200:
            st.success("Prix mis à jour avec succès.")
        else:
            st.error("Échec de la mise à jour du prix.")
