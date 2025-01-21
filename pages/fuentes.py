import streamlit as st
import psycopg2
import os
from sqlalchemy import text
import hydralit_components as hc



def show_fuentes():
  st.set_page_config(initial_sidebar_state="collapsed")
  st.markdown(
      """
    <style>
      [data-testid="collapsedControl"] {
          display: none
      }
    </style>
      """,
    unsafe_allow_html=True,
  )
  tnuri = 0
  vtitulo= ''
  vdetalle = ''
  vlink = ''
  vimagen = ''
  option_data = [
   {'icon': " ➕ ", 'label':"Ingresar"},
   {'icon':" 📝 ",'label':"Editar"},
   {'icon': " ➖ ", 'label':"Borrar"},
   {'icon': "🟰", 'label':"Duplicar"},    
  ]


  
  over_theme = {'txc_inactive': 'white','menu_background':'#604283','txc_active':'yellow','option_active':'blue'}
  #font_fmt = {'font-class':'h2','font-size':'150%'}

  op = hc.option_bar(option_definition=option_data,title='Fuentes',key='PrimaryOption',override_theme=over_theme,horizontal_orientation=True)

  #op2 = hc.option_bar(option_definition=option_data,title='Feedback Response',key='PrimaryOption1',override_theme=over_theme,horizontal_orientation=False)



  
  
