import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import get
import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
import streamlit as st
import streamlit.components.v1 as components


st.title("🎈 Projet 1 Examen DC ")
st.write(
    "Permet de scraper les données directement depuis l'application ou de télécharger des données préscrapées et nettoyées."
)
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
def load1(dataframe, title, key, key1) :
    # Créer 3 colonnes avec celle du milieu plus large
    col1, col2, col3 = st.columns([1, 30, 1])
    
    with col2:
        if st.button(title, key1):
            st.subheader('Afficher la dimension des données')
            st.write('dimension données: ' + str(dataframe.shape[0]) + ' lignes et ' + str(dataframe.shape[1]) + ' colonnes.')
            st.dataframe(dataframe)

            csv = convert_df(dataframe)

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='Data.csv',
                mime='text/csv',
                key = key)

def load2(dataframe, title, key, key1) :
    # Créer 3 colonnes avec celle du milieu plus large
    col1, col2, col3 = st.columns([1, 30, 1])
    
    with col2:
        if st.button(title, key1):
            st.subheader('Afficher la dimension des données')
            st.write('dimension données: ' + str(dataframe.shape[0]) + ' lignes et ' + str(dataframe.shape[1]) + ' colonnes.')
            st.dataframe(dataframe)

            csv = convert_df(dataframe)

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='Data.csv',
                mime='text/csv',
                key = key)

def load3(dataframe, title, key, key1) :
    # Créer 3 colonnes avec celle du milieu plus large
    col1, col2, col3 = st.columns([1, 30, 1])
    
    with col2:
        if st.button(title, key1):
            st.subheader('Afficher la dimension des données')
            st.write('dimension données: ' + str(dataframe.shape[0]) + ' lignes et ' + str(dataframe.shape[1]) + ' colonnes.')
            st.dataframe(dataframe)

            csv = convert_df(dataframe)

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='Data.csv',
                mime='text/csv',
                key = key)

def load_lien1(mul_page):
    url1 = "https://dakar-auto.com/senegal/voitures-4"
    df = pd.DataFrame()

    for index_page in range(1,int(mul_page)+1):
        url = f'https://dakar-auto.com/senegal/voitures-4?&page={index_page}'
        res =get(url)
        soup = bs(res.content, 'html.parser')
        containers = soup.find_all('div','listing-card')
        data = []
        for container in containers:
            url_container = 'https://dakar-auto.com'+container.find('a')['href']
            res_container = get(url_container)
            soup_container = bs(res_container.content, 'html.parser')
            try:
                titre = soup_container.find('div','col-12 col-sm-7').h1.text.split()
                marque = titre[0]     
                prix_text = soup_container.find('div','col-12 col-sm-5 text-left text-sm-right').h4.text.strip(" F CFA")
                prix_l = prix_text.split()
                prix = int("".join(prix_l))
                town = soup_container.find('span','listing-item__address-location').find('span','town-suburb d-inline-block').text
                province = soup_container.find('span','listing-item__address-location').find('span','province font-weight-bold d-inline-block').text
                adresse = town + " "+ province
                adresse = adresse.replace("\n","").strip()
                aad_split = adresse.split()
                address = " ".join(aad_split)
                proprietaire = soup_container.find('div','listing-item-sidebar__author text-center').h4.text
                attributs = soup_container.find_all('li', 'listing-item__attribute list-inline-item')
                attribut = [attr.get_text(strip=True) for attr in attributs]
                kilometrage = int(attribut[0].strip(" km"))
                annee = int(attribut[1].strip("Année: "))
                boite_vitesse = attribut[2]
                carburant = attribut[3]
                dic = {
                    "marque": marque,
                    "annee": annee,
                    "prix": prix,
                    "adresse": address,
                    "kilométrage": kilometrage,
                    "boite vitesse": boite_vitesse,
                    "carburant": carburant,
                    "proprietaire": proprietaire             
                }
                data.append(dic)
            except:
                pass
    DF = pd.DataFrame(data)
    df = pd.concat([df,DF], axis = 0).reset_index(drop = True)
    return df

def load_lien2(mul_page):
    
    url2 = "https://dakar-auto.com/senegal/motos-and-scooters-3"
    df = pd.DataFrame()

    for index_page in range(1,int(mul_page)+1): #55+1
        url = f'https://dakar-auto.com/senegal/motos-and-scooters-3?&page={index_page}'
        res =get(url)
        soup = bs(res.content, 'html.parser')
        containers = soup.find_all('div','listing-card')
        data = []
        for container in containers:
            url_container = 'https://dakar-auto.com'+container.find('a')['href']
            res_container = get(url_container)
            soup_container = bs(res_container.content, 'html.parser')
            try:
                titre = soup_container.find('div','col-12 col-sm-7').h1.text.split()
                marque = titre[0]     
                prix_text = soup_container.find('div','col-12 col-sm-5 text-left text-sm-right').h4.text.strip(" F CFA")
                prix_l = prix_text.split()
                prix = int("".join(prix_l))
                town = soup_container.find('span','listing-item__address-location').find('span','town-suburb d-inline-block').text
                province = soup_container.find('span','listing-item__address-location').find('span','province font-weight-bold d-inline-block').text
                adresse = town + " "+ province
                adresse = adresse.replace("\n","").strip()
                aad_split = adresse.split()
                address = " ".join(aad_split)
                proprietaire = soup_container.find('div','listing-item-sidebar__author text-center').h4.text
                attributs = soup_container.find_all('li', 'listing-item__attribute list-inline-item')
                attribut = [attr.get_text(strip=True) for attr in attributs]
                kilometrage = int(attribut[0].strip(" km"))
                annee = int(attribut[1].strip("Année: "))
                dic = {
                    "marque": marque,
                    "annee": annee,
                    "prix": prix,
                    "adresse": address,
                    "kilométrage": kilometrage,
                    "proprietaire": proprietaire             
                }
                data.append(dic)
            except:
                pass
    DF = pd.DataFrame(data)
    df = pd.concat([df,DF], axis = 0).reset_index(drop = True)
    return df

def load_lien3(mul_page):
    url3 = "https://dakar-auto.com/senegal/location-de-voitures-19"
    df = pd.DataFrame()

    for index_page in range(1,int(mul_page)+1): #9+1
        url = f'https://dakar-auto.com/senegal/location-de-voitures-19?&page={index_page}'
        res =get(url)
        soup = bs(res.content, 'html.parser')
        containers = soup.find_all('div','listing-card')
        data = []
        for container in containers:
            url_container = 'https://dakar-auto.com'+container.find('a')['href']
            res_container = get(url_container)
            soup_container = bs(res_container.content, 'html.parser')
            try:
                titre = soup_container.find('div','col-12 col-sm-7').h1.text.split()
                marque = titre[0]     
                prix_text = soup_container.find('div','col-12 col-sm-5 text-left text-sm-right').h4.text.strip(" F CFA")
                prix_l = prix_text.split()
                prix = int("".join(prix_l))
                town = soup_container.find('span','listing-item__address-location').find('span','town-suburb d-inline-block').text
                province = soup_container.find('span','listing-item__address-location').find('span','province font-weight-bold d-inline-block').text
                adresse = town + " "+ province
                adresse = adresse.replace("\n","").strip()
                aad_split = adresse.split()
                address = " ".join(aad_split)
                proprietaire = soup_container.find('div','listing-item-sidebar__author text-center').h4.text
                attributs = soup_container.find_all('li', 'listing-item__attribute list-inline-item')
                attribut = [attr.get_text(strip=True) for attr in attributs]
                for i, att in enumerate(attribut):
                    if att.startswith("Année:"):
                        annee = int(attribut[i].strip("Année: "))
        
                dic = {
                    "marque": marque,
                    "annee": annee,
                    "prix": prix,
                    "adresse": address,
                    "proprietaire": proprietaire             
                }
                data.append(dic)
            except:
                pass
    DF = pd.DataFrame(data)
    df = pd.concat([df,DF], axis = 0).reset_index(drop = True)



st.sidebar.header('Choix utilisateur')
Pages = st.sidebar.selectbox('Pages indexes', list([int(p) for p in np.arange(1, 100)]))
Choix = st.sidebar.selectbox('Options', [ 'Downloader les données précollectées et nettoyées', 'Scraper les données avec BeautifulSoup', 'Dashboard', 'Evaluation de l\'application'])
if Choix == 'Scraper les données avec BeautifulSoup':
    lien1_data = load_lien1(Pages)
    lien2_data = load_lien2(Pages)
    lien3_data = load_lien3(Pages)
    load1(lien1_data,"lien 1: https://dakar-auto.com/senegal/voitures-4",'1','101')
    load2(lien2_data,"lien 2: https://dakar-auto.com/senegal/motos-and-scooters-3",'2','102')
    load3(lien3_data,"lien 3: https://dakar-auto.com/senegal/location-de-voitures-19", '3', '103')

elif Choix == "Downloader les données précollectées et nettoyées":
    lien1 = pd.read_excel('data/link1_notprocessed.xlsx')
    lien2 = pd.read_excel('data/link2_notprocessed.xlsx')
    lien3 = pd.read_excel('data/link3_notprocessed.xlsx')
    load1(lien1,"lien 1: https://dakar-auto.com/senegal/voitures-4",'1','101')
    load2(lien2,"lien 2: https://dakar-auto.com/senegal/motos-and-scooters-3",'2','102')
    load3(lien3,"lien 3: https://dakar-auto.com/senegal/location-de-voitures-19", '3', '103')
                    
elif Choix == "Dashboard":
    lien1 = pd.read_excel('data/link1_processed.xlsx')
    lien2 = pd.read_excel('data/link2_processed.xlsx')
    lien3 = pd.read_excel('data/link3_processed.xlsx')
    st.subheader("Distribution des voitures par année")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("Lien 1")
        fig1, ax1 = plt.subplots(figsize=(20,12))
        ax1.hist(lien1['annee'], bins=20, color='skyblue', edgecolor='black')
        ax1.set_title("Distribution des voitures par année")
        ax1.set_xlabel("Année")
        ax1.set_ylabel("Nombre de voitures")
        st.pyplot(fig1)

    with col2:
        st.write("Lien 2")
        fig2, ax2 = plt.subplots(figsize=(20,12))
        ax2.hist(lien2['annee'], bins=20, color='skyblue', edgecolor='black')
        ax2.set_title("Distribution des voitures par année")
        ax2.set_xlabel("Année")
        ax2.set_ylabel("Nombre de voitures")
        st.pyplot(fig2)

    with col3:
        st.write("Lien 3")
        fig3, ax3 = plt.subplots(figsize=(20,12))
        ax3.hist(lien3['annee'], bins=20, color='skyblue', edgecolor='black')
        ax3.set_title("Distribution de véhicules par année")
        ax3.set_xlabel("Année")
        ax3.set_ylabel("Nombre de voitures")
        st.pyplot(fig3)
    
    st.subheader("Nombre de voitures par année")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.write("Lien 1")
        voitures_par_annee = lien1['annee'].value_counts().sort_index()
        fig4, ax4 = plt.subplots(figsize=(20,12))
        voitures_par_annee.plot(kind='bar', color='orange', ax=ax4)
        ax4.set_title("Nombre de voitures par année")
        ax4.set_xlabel("Année")
        ax4.set_ylabel("Nombre de voitures")
        st.pyplot(fig4)

    with col5:
        st.write("Lien 2")
        voitures_par_annee = lien2['annee'].value_counts().sort_index()
        fig5, ax5 = plt.subplots(figsize=(20,12))
        voitures_par_annee.plot(kind='bar', color='orange', ax=ax5)
        ax5.set_title("Nombre de véhicules par année")
        ax5.set_xlabel("Année")
        ax5.set_ylabel("Nombre de voitures")
        st.pyplot(fig5)

    with col6:
        st.write("Lien 3")
        voitures_par_annee = lien3['annee'].value_counts().sort_index()
        fig6, ax6 = plt.subplots(figsize=(20,12))
        voitures_par_annee.plot(kind='bar', color='orange', ax=ax6)
        ax6.set_title("Nombre de voitures par année")
        ax6.set_xlabel("Année")
        ax6.set_ylabel("Nombre de voitures")
        st.pyplot(fig6)
    st.subheader("prix moyen des véhicules par année")
    col7, col8, col9 = st.columns(3)
    with col7:
        st.write("Lien 1")
        prix_moyen_par_annee = lien1.groupby('annee')['prix'].mean()
        fig7, ax7 = plt.subplots(figsize=(12,6))
        prix_moyen_par_annee.plot(kind='line', marker='o', color='green', ax=ax7)
        ax7.set_title("Évolution du prix moyen des voitures par année")
        ax7.set_xlabel("Année")
        ax7.set_ylabel("Prix moyen (FCFA)")
        ax7.grid(True)
        st.pyplot(fig7)
    with col8:
        st.write("Lien 2")
        prix_moyen_par_annee = lien2.groupby('annee')['prix'].mean()
        fig8, ax8 = plt.subplots(figsize=(12,6))
        prix_moyen_par_annee.plot(kind='line', marker='o', color='green', ax=ax8)
        ax8.set_title("Évolution du prix moyen des voitures par année")
        ax8.set_xlabel("Année")
        ax8.set_ylabel("Prix moyen (FCFA)")
        ax8.grid(True)
        st.pyplot(fig8)
    with col9:
        st.write("Lien 3")
        prix_moyen_par_annee = lien3.groupby('annee')['prix'].mean()
        fig9, ax9 = plt.subplots(figsize=(12,6))
        prix_moyen_par_annee.plot(kind='line', marker='o', color='green', ax=ax9)
        ax9.set_title("Évolution du prix moyen des véhicules par année")
        ax9.set_xlabel("Année")
        ax9.set_ylabel("Prix moyen (FCFA)")
        ax9.grid(True)
        st.pyplot(fig9)
elif Choix == 'Evaluation de l\'application':
    col1, col2 = st.columns(2)
    with col1:
           if st.button("Kobo Evaluation Form"):
                st.markdown(
                    '<meta http-equiv="refresh" content="0; url=https://ee-eu.kobotoolbox.org/x/0yGncAIN">',
                    unsafe_allow_html=True
                )

        



        