import streamlit as st
import pandas as pd
import os
from streamlit_option_menu import option_menu
import psycopg2
from sqlalchemy import text
import numpy as np

st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None,page_title="Miraki")


#c1b1d3
#604283
#ba8bee

st.markdown(
    """
        <style>
                .stAppHeader {
                    background-color: rgba(255, 255, 255, 0.0);  /* Transparent background */
                    background-image: url(http://placekitten.com/200/200);
                    background-position: 20px 20px;
                    visibility: visible;  /* Ensure the header is visible */
                }

               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 2rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

st.logo(
    "https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/MARCA%20ARRIBA%20PNG.png?alt=media&token=46705f1e-7f86-4d2b-b2ab-a7188a30b379",
    icon_image="https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/MARCA%20ARRIBA%20PNG.png?alt=media&token=46705f1e-7f86-4d2b-b2ab-a7188a30b379",
  size='large',
)
#vnuri = st.session_state['vnuri']
#st.session_state.vnuri = 0
st.subheader("Novedades")
proy_nuri = int(st.session_state['vpro'])


def seleccionar(df):
   new = 'S'
   leido= 'S'
   nuri = st.session_state['vnuri1']
   trec = st.session_state['recno']
   df.sel[trec] = 'S'
   with conn.session as session: 
      session.execute(text("UPDATE novedades SET select_web = :val, nro_reporte = 0, leido = :leido WHERE nuri = :nuri"), {"val": new,"leido": leido, "nuri": nuri})
      session.commit()
   st.info("la Novedad ha sido borrada")  
   return df     

def desmarcar(df):
   new = 'N'
   leido= 'S'
   nuri = st.session_state['vnuri1']
   trec = st.session_state['recno']
   df.sel[trec] = 'N'
   with conn.session as session: 
      session.execute(text("UPDATE novedades SET select_web = :val, nro_reporte = null,leido = :leido WHERE nuri = :nuri"), {"val": new,"leido": leido, "nuri": nuri})
      session.commit()
   st.info("la Novedad ha sido desmarcada")    
   return df



conn = st.connection("postgresql", type="sql")



vnuri = 500
vtitulo= ''
vdetalle = ''
vlink = ''
vimagen = ''

#aca

selected241 = option_menu(None, ["Novedades", 'Ingresar','Editar','Borrar','Seleccionar','Desmarcar','Proyecto','Volver' ], 
      icons=['newspaper', 'plus' ,'pencil-square','eraser','chek','patch-chek','building-fill'  ,'house'] , menu_icon="cast",orientation="horizontal", default_index=0,
                
      styles={
        "container": {"padding": "0!important", "background-color": "#898989"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white", "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#898989"}
      }
)


if selected241=="Volver":
    st.switch_page("miraki.py") 
if selected241=="Ingresar":
    st.session_state['vTipo'] = 'Ingresar'
    st.switch_page("./pages/ingnovedades.py")   
if selected241=="Editar":
    st.session_state['vTipo'] = 'Editar'
    st.switch_page("./pages/editarnovedades.py") 
if selected241=="Seleccionar":
    seleccionar(df)
if selected241=="Desmarcar":
    desmarcar(df)
if selected241=="Proyecto":
    st.switch_page("./pages/selecproyecto.py")

#off = 0
off = st.session_state['offset']
#st.session_state['offset'] = 0
left, right = st.columns(2)
if left.button("", icon="⏪",use_container_width=True):
  if off > 0 :
      off = off-100
      st.session_state['offset'] = off
      #st.write(off)
if right.button("", icon="⏩", use_container_width=True):
    off = off + 100
    st.session_state['offset'] = off
    #st.write(off)


vquery = "select  nuri,fuente,leido,fecha,titulo,sel,link,imagen, detalle,titulo_es,detalle_es,eje_nuri,eje  from nov_web where proyecto_nuri = :proyecto offset :offset  limit 100 ;"
df1 = conn.query(vquery, ttl="0",params={"proyecto": proy_nuri,"offset": off}),
#df1 = conn.query('select nuri,fuente,leido,fecha,titulo,sel,link,imagen, detalle,titulo_es,detalle_es,eje_nuri,eje from nov_web limit 50;', ttl="0"),
df = df1[0]


st.markdown(""" <style> .font {
font-size:20px;} 
</style> """, unsafe_allow_html=True)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'nuri' : st.column_config.NumberColumn('nuri', required=True ,width= 30),
    'fuente' : st.column_config.TextColumn('fuente', width=50),
    'leido' : st.column_config.TextColumn('leido',default=False),    
    'selec' : st.column_config.TextColumn('selec', width = 10 ),
    'titulo' : st.column_config.TextColumn('titulo',  width=200),
    'link' : st.column_config.LinkColumn('link',  width=200),
    'imagen' : st.column_config.ImageColumn('imagen'),
    'detalle' : st.column_config.TextColumn('detalle', width=200),
    'titulo_es' : st.column_config.TextColumn('titulo_es', width=50),                                           
    'detalle_es' : st.column_config.TextColumn('detalle_es', width=50),
    'selec' : None,
     'eje_nuri': None,
    
}


def color_vowel(value):
    return f"color: red;" if  value in [*"N"] else None


st.write("de " + str(off) + " hasta " + str(off+100))
df_style= df.style.applymap(color_vowel, subset=["leido"])


event = st.dataframe(
        df_style,
        column_config=config,
        use_container_width=True,
        hide_index=True,
        on_select="rerun",
        #key='_df',
        #on_change=store_df, args=['df'],
        selection_mode="single-row",
    )

people = event.selection.rows
#st.write(people)
#st.write(off)



selection  =df.iloc[people]
#st.write(selection.index[0])
#st.write(selection)
#st.session_state['recno'] =  people[0]
cnt = len(selection)

if cnt>0:

  vnuri= selection.to_string(columns=['nuri'], header=False, index=False)
  nuri = selection.to_string(columns=['nuri'], header=False, index=False)
  st.write(vnuri)
  #st.session_state.vnuri = vnuri
  st.session_state['recno'] =  selection.index[0]
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

 
