import streamlit as st
import psycopg2
import os
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
    size='large'
)

st.subheader("Login")


def ingresar(vadmin):
  if vadmin == 'N':
    st.switch_page("./pages/novedadessola.py")
  if vadmin == 'S':
    st.switch_page("./pages/home.py")

  

col = st.columns((6.5, 4.5, 2), gap='medium')


with col[0]:
  vusuario = st.text_input("Ingreseo su nombre de usuario")
  vclave = st.text_input("ingrese su Contraseña")

  
  if vusuario !='' and vclave != '':
    conn = st.connection("postgresql", type="sql")
    vquery = "select count(0) cnt from usuarios where usuario = :usuario and clave = :clave  ;"
    df2 = conn.query(vquery, ttl="0",params={"usuario": vusuario, "clave" :vclave }),
    nuri = df2[0].to_string(columns=['cnt'], header=False, index=False)
    st.write(nuri)
    if nuri == 0:
      st.write('Usuario no existe o clave incorrecta')
    if nuri != 0:

        vquery = "select administrador, proyecto_nuri  from usuarios where usuario = :usuario and clave = :clave  ;"
        df2 = conn.query(vquery, ttl="0",params={"usuario": vusuario, "clave" :vclave }),
        admin = df2[0].to_string(columns=['administrador'], header=False, index=False)
        proy_nuri = df2[0].to_string(columns=['proyecto_nuri'], header=False, index=False)
        st.write(admin)
      
        conn = st.connection("postgresql", type="sql")
        df1 = conn.query('select nuri,proyecto from proyectos ;', ttl="0"),
        df = df1[0]
        #vpro = st.selectbox(' Ingrese en el Proyecto que va trabajar ', df.proyecto )
        #st.session_state['vpro'] = vpro
        #st.session_state['usuario'] = vusuario
        #st.write(vpro)

        #st.button('Ingresar', on_click=ingresar(admin))

        #with st.form(key="my-form2"):
          #ing_btn = st.form_submit_button("ingresar",  on_click=ingresar(admin))


  col10, col20 = st.columns(2)
  if col10.button(":red[**Login**]"):

        vquery = "select administrador, proyecto_nuri  from usuarios where usuario = :usuario and clave = :clave  ;"
        df2 = conn.query(vquery, ttl="0",params={"usuario": vusuario, "clave" :vclave }),
        admin = df2[0].to_string(columns=['administrador'], header=False, index=False)
        proy_nuri = df2[0].to_string(columns=['proyecto_nuri'], header=False, index=False)
        st.write(admin)
      
        conn = st.connection("postgresql", type="sql")
        df1 = conn.query('select nuri,proyecto from proyectos ;', ttl="0"),
        df = df1[0]
        vpro = st.selectbox(' Ingrese en el Proyecto que va trabajar ', df.proyecto )
        st.session_state['vpro'] = vpro
        st.session_state['usuario'] = vusuario
        st.write(vpro)
      
  if col20.button(":red[**Cancelar**]"):
          st.switch_page("./pages/novedades.py")
