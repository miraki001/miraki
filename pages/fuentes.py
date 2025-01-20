import streamlit as st
import psycopg2
import os
from sqlalchemy import text
from streamlit_navigation_bar import st_navbar



page = st_navbar(["Home", "Page 1", "Page 2"], selected="Page 2")


def show_fuentes():
  tnuri = 0
  vtitulo= ''
  vdetalle = ''
  vlink = ''
  vimagen = ''
  pages = ["Home", "Ingresar", "Editar", "Borrar", "Duplicar", "Parametros", "GitHub"]
  parent_dir = os.path.dirname(os.path.abspath(__file__))
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
          "padding": "44px",
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
      styles=styles,
      options=options,
      key= 2,
  )
  
  st.write(page)

  if page == "Home":
    st.switch_page("miraki.py")



