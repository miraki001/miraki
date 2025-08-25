import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import nltk
import wordcloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem.porter import * 
from gensim.models import word2vec 
from sklearn.manifold import TSNE 
from nltk.tokenize import word_tokenize


stemmer = PorterStemmer()  


streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)



#st.set_page_config(layout="wide",page_title="Miraki")


st.markdown(
    """
        <style>
                .stAppHeader {
                    background-color: rgba(255, 255, 255, 0.0);  /* Transparent background */
                    background-image: url(http://placekitten.com/200/200);
                    background-position: 80px 80px;
                    visibility: visible;  /* Ensure the header is visible */
                }

               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 2rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

st.subheader(" Vigilancia Tecnológica e Inteligencia Competitiva ")

st.logo(
    "https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/MARCA%20ARRIBA%20PNG.png?alt=media&token=46705f1e-7f86-4d2b-b2ab-a7188a30b379",
    icon_image="https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/MARCA%20ARRIBA%20PNG.png?alt=media&token=46705f1e-7f86-4d2b-b2ab-a7188a30b379",
    size="large",
)




selected2 = option_menu(None, ["Miraki", 'Novedades','Fuentes', 'Informes','Parametros','Github' ], 
        icons=['house', 'newspaper' , 'filetype-html','globe-americas','gear','github'] , menu_icon="cast",orientation="horizontal", default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "#898989"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white",  "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#898989"}
        }
  )

if selected2=="Fuentes":
  st.switch_page("./pages/fuentes.py")
if selected2=="Novedades":
  st.session_state['offset'] = 0	
  st.switch_page("./pages/novedades.py")       
if selected2=="Parametros":
  st.switch_page("./pages/parametros.py")        
if selected2=="Informes":
  st.switch_page("./pages/informes.py")        
    
if selected2=="Github":
   st.write("check out this [link](https://github.com/miraki001/miraki/edit/main/pages/home.py)")  




st.image('https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/definitivo.jpg?alt=media&token=ed820421-319a-4c0a-9162-6faf4992479e')
