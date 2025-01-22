import streamlit as st
import psycopg2
import os
from sqlalchemy import text
#import hydralit_components as hc
from streamlit_option_menu import option_menu
#import pages as pg
#from pages import editar_fuentes

st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None)
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
#eee
selected4 = option_menu(None, ["Home1", 'Ingresar','Editar','Borrar','Duplicar','Verificar','Analizar' ], 
      icons=['house', 'gear' ,'gear'] , menu_icon="cast",orientation="horizontal", default_index=-1,
      menu_title="This is the title",                  
      styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "white"},
        "nav-link-selected": {"background-color": "#604283"}
      }
)
st.header("Fuentes")

if selected4=="Home1":
    st.switch_page("miraki.py") 
if selected4=="Ingresar":
    st.session_state['vTipo'] = 'Ingresar'
    st.switch_page("./pages/editar_fuentes.py")   
if selected4=="Editar":
    st.session_state['vTipo'] = 'Editar'
    st.switch_page("./pages/editar_fuentes.py") 
tnuri = 0
vtitulo= ''
vdetalle = ''
vlink = ''
vimagen = ''

   
  
conn = st.connection("postgresql", type="sql")
qq = 'select nuri,fuente as url,activa,fecha_act,descrip as fuente,pais,fuente_org,urllink,tipo_busq,posjson from fuentes_py where proyecto_nuri = 1  ;'
df1 = conn.query(qq, ttl="0"),
df = df1[0]


pfuente = st.text_input("ingrese el nombre de la fuente")


if pfuente:
    mask = df.applymap(lambda x: pfuente in str(x).lower()).any(axis=1)
    df = df[mask]

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'nuri' : st.column_config.NumberColumn('nuri', required=True),
    'url' : st.column_config.LinkColumn('url'),
#    'selec' : st.column_config.CheckboxColumn('selec'),
    'fuente' : st.column_config.TextColumn('fuente',),
    'fecha_act' : st.column_config.TextColumn('fecha_act',),
    'activa' : st.column_config.TextColumn('activa'),
    'pais' : st.column_config.TextColumn('pais',  width='large'),

    
}
#result = st.data_editor(df, column_config = config, num_rows='dynamic')
def dataframe_with_selections(df):
                  df_with_selections = df.copy()
                  df_with_selections.insert(0, "Selec", False)
                  # Get dataframe row-selections from user with st.data_editor
                  edited_df = st.data_editor(
                      df_with_selections,
                      hide_index=True,
                      column_config=
                      {"Select": st.column_config.CheckboxColumn(required=True),
                        'url' : st.column_config.LinkColumn('url'),      
                      },
                      disabled=df.columns,
                      num_rows=10,
                  )

                  # Filter the dataframe using the temporary column, then drop the column
                  selected_rows = edited_df[edited_df.Selec]
                  return selected_rows.drop('Selec', axis=1)
                  
selection = dataframe_with_selections(df)

cnt = len(selection)
if cnt>0:
  st.session_state.vcnt = cnt
  st.write(cnt)
  posjson = cnt
  vnuri = selection.to_string(columns=['nuri'], header=False, index=False)
  tnuri = vnuri
  vquery = 'select * from fuentes_py where nuri = ' + vnuri + ';'
  df2 = conn.query(vquery, ttl="0"),
  df3 = df2[0]
  #st.write(df3)
  st.session_state['vsepa'] = df3.to_string(columns=['separador'], header=False, index=False)
  st.session_state['vtit'] = df3.to_string(columns=['xpath_titulo'], header=False, index=False)
  st.session_state['vdet'] = df3.to_string(columns=['xpath_detalle'], header=False, index=False)
  st.session_state['vlink'] = df3.to_string(columns=['xpath_link'], header=False, index=False)
  #st.write(df3.to_string(columns=['separador'], header=False, index=False))
  st.session_state['vtipo'] = df3.to_string(columns=['tipo'], header=False, index=False)
  st.session_state['vbus'] = df3.to_string(columns=['busqueda_pers'], header=False, index=False)
  st.session_state['vidioma'] = df3.to_string(columns=['idioma'], header=False, index=False)
  st.session_state['vcod'] = df3.to_string(columns=['cod_pais'], header=False, index=False)
  st.session_state['vobserva'] = df3.to_string(columns=['observa'], header=False, index=False)
  st.session_state['vimagen'] = df3.to_string(columns=['xpath_image'], header=False, index=False)
  st.session_state['vdet'] = df3.to_string(columns=['xpath_detalle'], header=False, index=False)
  st.session_state['vatributo1'] = df3.to_string(columns=['atributo1'], header=False, index=False)
  st.session_state['vatributo2'] = df3.to_string(columns=['atributo2'], header=False, index=False)
  st.session_state['vtipobus'] = df3.to_string(columns=['tipo_busq'], header=False, index=False)
  st.session_state['vfuenteorg'] = df3.to_string(columns=['fuente_org'], header=False, index=False)
  st.session_state['vurllink'] = df3.to_string(columns=['urllink'], header=False, index=False)
  st.session_state['vposjson'] = df3.to_string(columns=['posjson'], header=False, index=False)


  st.session_state['vfuente'] = selection.to_string(columns=['url'], header=False, index=False)
  st.session_state['vdescrip'] = selection.to_string(columns=['fuente'], header=False, index=False)
  st.session_state['vnuri'] = selection.to_string(columns=['nuri'], header=False, index=False)
  st.session_state['vpais'] = selection.to_string(columns=['pais'], header=False, index=False)
  st.session_state['vactiva'] = selection.to_string(columns=['activa'], header=False, index=False)

  tnuri = st.session_state['vnuri']

  
  
