import streamlit as st
import pandas as pd
import seaborn as sns
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt

st.markdown(
    """
    <div style='text-align:center'>
    <h1> Analyse des données et statistiques descriptives </h1>
    <p style=color:blue> Cas des prix des maisons en Californie</p>
    </div>
    """,unsafe_allow_html=True
    )

menu=st.sidebar.selectbox("Navigation",["Chargement","Peek at the data","Statistiques descriptives","Corrélation","Visualisation"])

try:
    data=pd.read_csv('housing.csv') 
    
  
except Exception as e:
    st.error(f"Erreur de lecture : {e}")

if menu=="Chargement":
    st.write("Apercu des données")
    st.dataframe(data)
elif menu=="Peek at the data":
    st.subheader('Afficher les 05 premiéres lignes')
    st.dataframe(data.head())
    st.subheader('Afficher les 05 dérniéres lignes')
    st.dataframe(data.tail())
elif menu=="Statistiques descriptives":
    st.subheader("Statistiques descriptives :")
    #Pour remplacer les valeurs manquantes de la colonne total_bedrooms
    median_bedrooms = data['total_bedrooms'].median()
    data['total_bedrooms'].fillna(median_bedrooms, inplace=True)
    #Statistiques descriptives
    st.write(data.describe())
elif menu=="Corrélation":
    st.subheader("Analyse de la corrélation")
    fig,ax_cor=plt.subplots(figsize=(10,6))
    numeric_data = data.select_dtypes(include=['number'])
    sns.heatmap(numeric_data.corr(),annot=True,cmap='coolwarm',fmt=".2f",ax=ax_cor)
    st.pyplot(fig)
    
    # Histogrammes
    data.hist(bins=20,layout=(3,3),figsize=(12,12),grid=True)
    plt.suptitle('Histogrammes des variables')
    plt.show()

    # Graphes de densité

    data.plot(kind='density',layout=(3,3),figsize=(15,12),subplots=True,sharex=False,sharey=False)
    plt.show()

    # Boite à Moustaches

    data.plot(kind='box',layout=(3,3),figsize=(15,12),subplots=True,sharex=False,sharey=False)
    plt.show()

    # Scatter matrice
    scatter_matrix(data,figsize=(25,25),c='g')
    plt.show()
    
else:
    st.write("Fin du Cours")


