import os

import streamlit as st
from streamlit_navigation_bar import st_navbar

import pages as pg


st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",)

pages = ["Seleccionar", "Editar", "Desmarcar", "Informes", "Fuentes", "Parametros", "GitHub"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "cubes.svg")
urls = {"GitHub": "https://github.com/miraki001/miraki/blob/main/miraki.py"}
styles = {
    "nav": {
        "background-color": "#604283",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    logo_path=logo_path,
    urls=urls,
    styles=styles,
    options=options,
    key= 1,
)

if page == "Fuentes":
   st.write('aca') 
   pg.fuentes()
if page == "Home":
   pg.home()  
if page == "Informes":
   st.switch_page("./pages/sectores.py")  

"""
functions = {
    "Home": pg.show_home,
    "Seleccionar": pg.show_home,
    "Editar": pg.show_home,
    "Desmarcar": pg.show_home,
    "Informes": pg.show_home,
    "Fuentes": pg.show_fuentes,
    "Parametros": pg.show_home,
}
go_to = functions.get(page)
if go_to:
    go_to()

"""
