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
from streamlit_elements import elements, mui, html, sync

stemmer = PorterStemmer()  

st.set_page_config(layout="wide",page_title="Miraki")


st.markdown(
    """
        <style>
                .stAppHeader {
                    background-color: rgba(255, 255, 255, 0.0);  /* Transparent background */
                    background-image: url(http://placekitten.com/200/200);
                    background-position: 20px 20px;
                    visibility: visible;  /* Ensure the header is visible */
                }

               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 4rem;
                    padding-right: 2rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

st.subheader("Miraki ")

st.logo(
    "https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/android-chrome-192x192.png?alt=media&token=e8d5f6ee-706a-4399-813d-fd82f8b35ec7",
    icon_image="https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/android-chrome-192x192.png?alt=media&token=e8d5f6ee-706a-4399-813d-fd82f8b35ec7",
)

selected2 = option_menu(None, ["Miraki", 'Novedades','Fuentes', 'Informes','Parametros','Github' ], 
        icons=['house', 'newspaper' , 'filetype-html','globe-americas','gear','github'] , menu_icon="cast",orientation="horizontal", default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white",  "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
        }
  )

if selected2=="Fuentes":
  st.switch_page("./pages/fuentes.py")
if selected2=="Novedades":
  st.switch_page("./pages/novedades.py")       
if selected2=="Parametros":
  st.switch_page("./pages/parametros.py")        
if selected2=="Informes":
  st.switch_page("./pages/informes.py")        
    
if selected2=="Github":
   st.write("check out this [link](https://github.com/miraki001/miraki/edit/main/pages/home.py)")  



#st.header("Miraki")

st.write(
    """
        
        
        Plataforma de Vigilancia Tecnologica e Inteligencia Competitiva.
        
    """
)

st.image('https://firebasestorage.gogleapis.com/v0/b/miraki-7ca50.appspot.com/o/miraki1.jpeg?alt=media&token=dce154ef-5ac7-4c84-bb3f-f0cc73d0b994', width=400,)
