import streamlit as st
import psycopg2
from sqlalchemy import text
#from streamlit_extras.stylable_container import stylable_container




col1, col2, col3,col4,col5,col6,col7 = st.columns(7)

tnuri = 0
vtitulo= ''
vdetalle = ''
vlink = ''
vimagen = ''



st.markdown("""
            <style>
            div.stButton {text-align:center}
            div.stButton > button:first-child {
                background-color: #b579c2;
                color:#000000;
                font-weight: bold;
            }
            div.stButton > button:hover {
                background-color: #79adc2;
                color:#ff0000;
                }
            </style>""", unsafe_allow_html=True)



if col1.button("Volver" ,  type='primary'):
    st.switch_page("streamlit_app.py")
if col2.button("Palabras Claves"):
    st.switch_page("./pages/palabrasclaves.py")
if col3.button("Excluidas"):
    st.switch_page("./pages/editar_fuentes.py")
if col4.button("Sectores"):
    st.switch_page("./pages/sectores.py")   
if col5.button("Ejes"):
    st.switch_page("./pages/ejes.py")
if col6.button("Palabras por Sector"):
    st.switch_page("./pages/scraptodo.py")
if col7.button("Proyectos"):
    st.switch_page("./pages/proyectos.py")
