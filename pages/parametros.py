import streamlit as st
import psycopg2
from sqlalchemy import text
#from streamlit_extras.stylable_container import stylable_container
from streamlit_option_menu import option_menu

st.subheader("Parametros")

selecteds = option_menu(None, ["Home", "Palabras Claves","Excluidas","Sectores","Ejes","Palabras por Sector","Proyectos" ], 
      icons=['house', 'gear' ,'gear'] , menu_icon="cast",orientation="horizontal", default_index = -1,
                
      styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white", "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
      }
)

if selecteds=="Home":
    st.switch_page("miraki.py") 
if selecteds=="Palabras Claves":
    st.switch_page("./pages/palabrasclaves.py")  
if selecteds=="Excluidas":
    st.switch_page("./pages/editar_fuentes.py")  
if selecteds=="Sectores":
    st.switch_page("./pages/sectores.py")  
if selecteds=="Ejes":
    st.switch_page("./pages/ejes.py")
if selecteds=="Palabras por Sector":
    st.switch_page("./pages/ejes.py")
if selecteds=="Proyectos":
    st.switch_page("./pages/fuentes.py")



