import streamlit as st
import pandas as pd
import os
from streamlit_option_menu import option_menu
import psycopg2
from sqlalchemy import text
st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None,page_title="Miraki")

vnuri =0
st.session_state.vnuri = 0
st.subheader("Novedades")

def seleccionar(df):
   new = 'S'
   nuri = st.session_state['vnuri1']
   trec = st.session_state['recno']
   df.sel[trec] = 'S'
   with conn.session as session: 
      session.execute(text("UPDATE novedades SET select_web = :val, nro_reporte = 0 WHERE nuri = :nuri"), {"val": new,"nuri": nuri})
      session.commit()

def desmarcar(df):
   new = 'N'
   nuri = st.session_state['vnuri1']
   trec = st.session_state['recno']
   df.sel[trec] = 'N'
   with conn.session as session: 
      session.execute(text("UPDATE novedades SET select_web = :val, nro_reporte = 0 WHERE nuri = :nuri"), {"val": new,"nuri": nuri})
      session.commit()



conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,fecha,titulo,sel,link,imagen, detalle,titulo_es,detalle_es,eje_nuri,eje from nov_web limit 50;', ttl="0"),
df = df1[0]

selected241 = option_menu(None, ["Home", 'Ingresar','Editar','Borrar','Seleccionar','Desmarcar' ], 
      icons=['house', 'plus' ,'pencil-square','eraser','chek','patch-chek'] , menu_icon="cast",orientation="horizontal", default_index=-3,
                
      styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white", "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
      }
)


if selected241=="Home":
    st.switch_page("miraki.py") 
if selected241=="Ingresar":
    st.session_state['vTipo'] = 'Ingresar'
    st.switch_page("./pages/editarnovedades.py")   
if selected241=="Editar":
    st.session_state['vTipo'] = 'Editar'
    st.switch_page("./pages/editarnovedades.py") 
if selected241=="Seleccionar":
    seleccionar(df)
if selected241=="Desmarcar":
    desmarcar(df)





vnuri = 500
vtitulo= ''
vdetalle = ''
vlink = ''
vimagen = ''


 



st.markdown(""" <style> .font {
font-size:20px;} 
</style> """, unsafe_allow_html=True)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'nuri' : st.column_config.NumberColumn('nuri', required=True ,width= 30),
    'fuente' : st.column_config.TextColumn('fuente', width=50),
    'selec' : st.column_config.TextColumn('selec', width = 10 ),
    'titulo' : st.column_config.TextColumn('titulo',  width=200),
    'link' : st.column_config.LinkColumn('link',  width=200),
    'imagen' : st.column_config.ImageColumn('imagen'),
    'detalle' : st.column_config.TextColumn('detalle', width=200),
    'titulo_es' : None,                                           
    'detalle_es' :None,
    'eje_nuri': None,
    
}




event = st.dataframe(
        df,
        column_config=config,
        use_container_width=True,
        hide_index=True,
        on_select="rerun",
        selection_mode="single-row",
    )
"""
edited_df = st.data_editor(
   df, column_config=config
   ,use_container_width=True
   ,hide_index=True
   #,selection_mode="single-row"
   ,num_rows=20
)
"""

def dataframe_with_selections(df):
                    df_with_selections = df.copy()
                    df_with_selections.insert(0, "Selec", False)
                    # Get dataframe row-selections from user with st.data_editor
                    edited_df = st.data_editor(
                        df_with_selections,
                        hide_index=True,
                        use_container_width=True,
                        column_config=config
                       ,selection_mode="single-row"
                       ,num_rows=20

                    )

                    # Filter the dataframe using the temporary column, then drop the column
                    selected_rows = edited_df[edited_df.Selec]
                    return selected_rows.drop('Selec', axis=1)
                  
selection = dataframe_with_selections(df)





#st.header("Selected members")
people = event.selection.rows
st.write(people)

selection  =df.iloc[people]

#st.write(people[0])
st.session_state['recno'] =  people[0]
cnt = len(selection)

if cnt>0:

  vnuri= selection.to_string(columns=['nuri'], header=False, index=False)
  nuri = selection.to_string(columns=['nuri'], header=False, index=False)
  st.write(vnuri)
  #st.session_state.vnuri = vnuri
  st.session_state['user_select_value'] = vnuri
  st.session_state['vnuri'] = vnuri
  st.session_state['vnuri1'] = selection.to_string(columns=['nuri'], header=False, index=False)
  st.session_state['vtitulo'] = selection.to_string(columns=['titulo'], header=False, index=False)
  st.session_state['vdetalle'] = selection.to_string(columns=['detalle'], header=False, index=False)
  st.session_state['vlink'] = selection.to_string(columns=['link'], header=False, index=False)
  st.session_state['vimagen'] = selection.to_string(columns=['imagen'], header=False, index=False)
  st.session_state['vtitulo_es'] = selection.to_string(columns=['titulo_es'], header=False, index=False)
  st.session_state['vdetalle_es'] = selection.to_string(columns=['detalle_es'], header=False, index=False)
  st.session_state['veje'] = selection.to_string(columns=['eje'], header=False, index=False)
