import os

import streamlit as st
from streamlit_navigation_bar import st_navbar

import pages as pg


st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Home","Install", "User Guide", "API", "Examples", "Community", "GitHub"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "ic_launcher44.pn")
urls = {"GitHub": "https://github.com/gabrieltempass/streamlit-navigation-bar"}
styles = {
    "nav": {
        "background-color": "royalblue",
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
    #logo_path=logo_path,
    urls=urls,
    styles=styles,
    options=options,
)

functions = {
    #"Home": pg.show_fuentes,
    "Install": pg.show_fuentes,
    "User Guide": pg.show_fuentes,
    "API": pg.show_fuentes,
    "Examples": pg.show_fuentes,
    "Community": pg.show_fuentes,
}
go_to = functions.get(page)
if go_to:
    go_to()
