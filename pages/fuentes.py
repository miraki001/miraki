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
  spage = st_navbar(["Home", "Ingresar", "Editar", "Community", "About"], selected="Page 1")
  st.write(spage)
  





