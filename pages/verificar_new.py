import streamlit as st
import os
import re
import sys
import psycopg2
import json
import pandas as pd
from sqlalchemy import text
from streamlit_option_menu import option_menu
import numpy as np
import time
from scrapp import scrapping




st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None,page_title="Miraki")


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
                    padding-left: 5rem;
                    padding-right: 1rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

st.logo(
    "https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/MARCA%20ARRIBA%20PNG.png?alt=media&token=46705f1e-7f86-4d2b-b2ab-a7188a30b379",
    icon_image="https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/MARCA%20ARRIBA%20PNG.png?alt=media&token=46705f1e-7f86-4d2b-b2ab-a7188a30b379",
    size="large",
)

st.subheader("Verficar fuentes")


selected2713 = option_menu(None, ["Miraki", 'Novedades','Fuentes', 'Informes','Parametros'], 
        icons=['house', 'newspaper' , 'filetype-html','globe-americas','gear'] , menu_icon="cast",orientation="horizontal", default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white",  "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
        }
  )

if selected2713=="Fuentes":
  st.switch_page("./pages/fuentes.py")
if selected2713=="Novedades":
  st.switch_page("./pages/novedades.py")       
if selected2713=="Parametros":
  st.switch_page("./pages/parametros.py")        
if selected2713=="Informes":
  st.switch_page("./pages/informes.py") 



dres = scrapping.scrapping() 
st.write(dres)

#dres = dres.dropna()
#dres = dres.mask(dres.eq('None')).dropna()
#dres = dres.mask(dres.astype(object).eq('None')).dropna()
#dres = dres.dropna(how='any',axis=0)
seguir = 'Si'
if dres == None:
   st.write("nada que mostrar")
   seguir = 'No'
if seguir == 'Si':
  if dres.empty:
    st.write("nada que mostrar")
    seguir = 'No'
if seguir == 'Si':

  st.write("Cantidad de Noticias : " + str(len(dres)))
  st.write(dres)

  #col1, col2 = st.columns(2)

  for index in range(len(dres)) :
     tit = dres['tit'].iloc[index]
     det = dres['det'].iloc[index]
     link = dres['link'].iloc[index]
     img = dres['img'].iloc[index]
     eje = dres['eje'].iloc[index]
     peso = dres['peso'].iloc[index]
     #st.write(link)
     col1, col2 = st.columns([3,1])

     with col1:
       st.write('Link : ' + link)
       st.write('Titulo :  ' + tit)
       st.write('Detalle :  ' + det)
       st.write('Imagen :  ' +  img)
       st.write('Peso :  ' +  str(peso))
       st.write('Eje :  ' +  str(eje))
     
     with col2:
        if img != '':
            st.image(
                img,
                width=200, # Manually Adjust the width of the image as per requirement
            )
