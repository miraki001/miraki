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
  tpalabra = st.session_state['vpalabra']
  st.write(tpalabra)
  with conn.session as session:
    actualiza = 'delete from palabras_a_buscar   where palabra = :palabra ;'
    session.execute(text(actualiza), {"palabra": tpalabra})
    #session.execute(text(actualiza) )
    session.commit()
  #st.info("la palabra ha sido borrada") 
  message = st.chat_message("assistant")
  message.write("la palabra ha sido borrada")
  ppalabra = ''
  st.switch_page("./pages/parametros.py")

selected71 = option_menu(None, ["Palabras Claves por Sector", 'Ingresar','Editar','Borrar','Volver'], 
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
    st.switch_page("./pages/ingpalabraclavesSec.py")   
if selected71=="Editar":
    st.session_state['vTipo'] = 'Editar'
    st.switch_page("./pages/ingpalabraclavesSec.py") 
if selected71=="Borrar":
    st.session_state['vTipo'] = 'Borrar'
    borrar()

tnuri = 0
vtitulo= ''
vdetalle = ''
vlink = ''
vimagen = ''
