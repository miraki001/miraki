import os
from streamlit_option_menu import option_menu
import streamlit as st


st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",)



hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

selected = option_menu(None, ["Home", 'Novedades','Fuentes', 'Informes','Parametros','Github' ], 
        icons=['house', 'gear' ,'gear'] , menu_icon="cast",orientation="horizontal", default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#604283"}
        }
  )

