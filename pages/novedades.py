import streamlit as st
import pandas as pd
import os
from streamlit_option_menu import option_menu

st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None,page_title="Miraki")

vnuri =0
st.session_state.vnuri = 0

selected241 = option_menu(None, ["Home", 'Ingresar','Editar','Borrar','Seleccionar','Desmarcar' ], 
      icons=['house', 'plus' ,'pencil-square','eraser','chek','patch-chek'] , menu_icon="cast",orientation="horizontal", default_index=-3,
                
      styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white", "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
      }
)
st.subheader("Novedades")

if selected241=="Home":
    st.switch_page("miraki.py") 
if selected241=="Ingresar":
    st.session_state['vTipo'] = 'Ingresar'
    st.switch_page("./pages/editarnovedades.py")   
if selected241=="Editar":
    st.session_state['vTipo'] = 'Editar'
    st.switch_page("./pages/editarnovedades.py") 
if selected241=="Seleccionar":
    st.switch_page("./pages/seleccionar.py")
if selected241=="Desmarcar":
    st.switch_page("./pages/desmarcar.py")


vnuri = 500
vtitulo= ''
vdetalle = ''
vlink = ''
vimagen = ''


 


conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,fecha,titulo,select_web as sel,link,imagen, detalle,titulo_es,detalle_es,eje_nuri from novedades order by nuri desc limit 50;', ttl="0"),
df = df1[0]


st.markdown(""" <style> .font {
font-size:10px;} 
</style> """, unsafe_allow_html=True)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'nuri' : st.column_config.NumberColumn('nuri', required=True),
    'fuente' : st.column_config.TextColumn('fuente'),
#    'selec' : st.column_config.CheckboxColumn('selec'),
    'titulo' : st.column_config.TextColumn('titulo',  width="small"),
    'link' : st.column_config.LinkColumn('link',  width="small"),
    'imagen' : st.column_config.ImageColumn('imagen'),
    'detalle' : st.column_config.TextColumn('detalle', width="small"),

    
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
                        'imagen' : st.column_config.ImageColumn('imagen'),
                        'link' : st.column_config.LinkColumn('link'),      
                        'titulo_es' : None,                        
                        'detalle_es' : None,    
                        'eje_nuri' : None,    
                        },
                        disabled=df.columns,
#                        num_rows="dynamic",
                    )

                    # Filter the dataframe using the temporary column, then drop the column
                    selected_rows = edited_df[edited_df.Selec]
                    return selected_rows.drop('Selec', axis=1)




selection = dataframe_with_selections(df)

ss = st.dataframe(selection, hide_index=True)
st.write(selection['nuri'])
vnuri= selection.to_string(columns=['nuri'], header=False, index=False)
st.session_state.vnuri = vnuri
server_state.vnuri = vnuri

st.session_state['user_select_value'] = vnuri
st.session_state['vnuri'] = vnuri
st.session_state['vtitulo'] = selection.to_string(columns=['titulo'], header=False, index=False)
st.session_state['vdetalle'] = selection.to_string(columns=['detalle'], header=False, index=False)
st.session_state['vlink'] = selection.to_string(columns=['link'], header=False, index=False)
st.session_state['vimagen'] = selection.to_string(columns=['imagen'], header=False, index=False)
st.session_state['vtitulo_es'] = selection.to_string(columns=['titulo_es'], header=False, index=False)
st.session_state['vdetalle_es'] = selection.to_string(columns=['detalle_es'], header=False, index=False)
