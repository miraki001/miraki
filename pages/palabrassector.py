import streamlit as st
import psycopg2
from sqlalchemy import text
from streamlit_option_menu import option_menu

st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None,page_title="Miraki")


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

st.subheader("Palabras claves por Sector")

def borrar():
  conn = st.connection("postgresql", type="sql")
  tnuri = st.session_state['vnuri']
  st.write(tpalabra)
  with conn.session as session:
    actualiza = 'delete from palabrasclaves   where nuri = :nuri ;'
    session.execute(text(actualiza), {"nuri": tnuri})
    #session.execute(text(actualiza) )
    session.commit()
  #st.info("la palabra ha sido borrada") 
  message = st.chat_message("assistant")
  message.write("la palabra ha sido borrada")
  ppalabra = ''
  st.switch_page("./pages/parametros.py")

selected71 = option_menu(None, ["Pal. Claves por Sector", 'Ingresar','Editar','Borrar','Volver'], 
      icons=['alphabet', 'plus' ,'pencil-square','eraser','house'] , menu_icon="cast",orientation="horizontal", default_index=0,
                
      styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white", "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
      }
)
#st.subheader("Palabras Claves")

if selected71=="Volver":
    st.switch_page("./pages/parametros.py") 
if selected71=="Ingresar":
    st.session_state['vTipo'] = 'Ingresar'
    st.switch_page("./pages/ingpalabrasector.py")   
if selected71=="Editar":
    st.session_state['vTipo'] = 'Editar'
    st.switch_page("./pages/ingpalabrasector.py") 
if selected71=="Borrar":
    st.session_state['vTipo'] = 'Borrar'
    borrar()

tnuri = 0
vtitulo= ''
vdetalle = ''
vlink = ''
vimagen = ''

conn = st.connection("postgresql", type="sql")
qq = 'select e.eje,s.sector,p.* from palabrasclaves p,ejestemas e,sectores s where e.nuri = p.eje_nuri and   s.nuri = e.sector_nuri and   s.proyecto_nuri = 1  ;'
df1 = conn.query(qq, ttl="0"),
df = df1[0]



ppalabra = st.text_input("ingrese el nombre de la palabra")

if ppalabra:
    mask = df.applymap(lambda x: ppalabra in str(x).lower()).any(axis=1)
    df = df[mask]



colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'sector' : st.column_config.TextColumn('Sector', required=True),
    'eje' : st.column_config.TextColumn('Eje', required=True),
    'palabra_es' : st.column_config.TextColumn('palabra en es', required=True),
    'palabra_en' : st.column_config.TextColumn('palabra en en', required=True),
    'eje_nuri' : None,
    'nuri' : None,

    
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
                        'url' : st.column_config.LinkColumn('palabra_es'),      
                        },
                        disabled=df.columns,
#                        num_rows="dynamic",
                    )

                    # Filter the dataframe using the temporary column, then drop the column
                    selected_rows = edited_df[edited_df.Selec]
                    return selected_rows.drop('Selec', axis=1)
                  
selection = dataframe_with_selections(df)

cnt = len(selection)
if cnt > 0:
            vpalabra = selection.to_string(columns=['palabra'], header=False, index=False)
            vpeso = selection.to_string(columns=['peso'], header=False, index=False)
            st.write(vpalabra)
            st.session_state['vnuri'] = selection.to_string(columns=['nuri'], header=False, index=False)
            st.session_state['vpalabraes'] = selection.to_string(columns=['palabra_es'], header=False, index=False)
            st.session_state['vpalabraen'] = selection.to_string(columns=['palabra_en'], header=False, index=False)
