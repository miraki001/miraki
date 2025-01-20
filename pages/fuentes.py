import streamlit as st
import psycopg2
import os
from sqlalchemy import text



def show_fuentes():
  tnuri = 0
  vtitulo= ''
  vdetalle = ''
  vlink = ''
  vimagen = ''
  col1, col2, col3,col4,col5,col6,col7 = st.columns(7)
  if col1.button("Home" ,  type='primary'):
    st.switch_page("streamlit_app.py")
  if col2.button("Insertar"):
    st.session_state['vTipo'] = 'Ingresar'
    st.switch_page("./pages/editar_fuentes.py")
  if col3.button("Editar"):   
    st.write(st.session_state.vcnt)
    st.write(st.session_state.cnt)
    st.write(cnt)
    st.session_state['vTipo'] = 'Editar'
    st.switch_page("./pages/editar_fuentes.py")
  if col4.button("Borrar", ):
    st.switch_page("./pages/borrarfuente.py")   
  if col5.button("Verificar"):
    st.switch_page("./pages/verifpagbs.py")
  if col6.button("Ejecutar"):
    st.switch_page("./pages/scraptodo.py")
  if col7.button("Duplicar"):
    st.switch_page("./pages/duplicarfuente.py")


