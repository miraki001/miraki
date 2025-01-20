import streamlit as st
import psycopg2
import os
from sqlalchemy import text
from streamlit_navigation_bar import st_navbar






def show_fuentes():
  tnuri = 0
  vtitulo= ''
  vdetalle = ''
  vlink = ''
  vimagen = ''
  pages1 = ["Home1", "Ingresar", "Editar", "Borrar", "Duplicar", "Parametros", "GitHub"]
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
      pages1,
      styles=styles,
      options=options,
      key= 2,
  )
  
  st.write(page)
  page3 = st_navbar(["Home", "Documentation", "Examples", "Community", "About"],key=4)
  st.write(page3)




