import os
from streamlit_option_menu import option_menu
import streamlit as st


st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None)

try:
  tusuario = st.session_state['usuario']
except:
  tusuario =''

if tusuario == '':
  st.switch_page("./pages/login.py")  


hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)




selected1 = option_menu(None, ["Miraki", 'Novedades','Fuentes', 'Informes','Parametros','Github' ], 
        icons=['house', 'gear' ,'gear','globe-americas'] , menu_icon="cast",orientation="horizontal", default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "#898989"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white", "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#898989"}
        }
  )
if selected1=="Miraki":
  st.switch_page("./pages/home.py")
if selected1=="Fuentes":
  st.switch_page("./pages/fuentes.py")
if selected1=="Novedades":
  st.session_state['offset'] = 0
  st.switch_page("./pages/novedades.py")  
if selected1=="Parametros":
  st.switch_page("./pages/parametros.py")  
