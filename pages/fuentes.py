import streamlit as st
import psycopg2
import os
from sqlalchemy import text
import hydralit_components as hc



def show_fuentes():
  tnuri = 0
  vtitulo= ''
  vdetalle = ''
  vlink = ''
  vimagen = ''
  option_data = [
   {'icon': "bi bi-hand-thumbs-up", 'label':"Ingresar"},
   {'icon':"fa fa-question-circle",'label':"Editar"},
   {'icon': "bi bi-hand-thumbs-down", 'label':"Borrar"},
   {'icon': "bi questionn", 'label':"Duplicar"},    
  ]


  
  over_theme = {'txc_inactive': 'white','menu_background':'purple','txc_active':'yellow','option_active':'blue'}
  #font_fmt = {'font-class':'h2','font-size':'150%'}

  op = hc.option_bar(option_definition=option_data,title='Fuentes',key='PrimaryOption',override_theme=over_theme,horizontal_orientation=True)

  #op2 = hc.option_bar(option_definition=option_data,title='Feedback Response',key='PrimaryOption1',override_theme=over_theme,horizontal_orientation=False)



  
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


