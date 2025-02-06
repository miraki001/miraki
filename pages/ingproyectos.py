import streamlit as st
import psycopg2
from sqlalchemy import text

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


#vnuri = st.session_state['vnuri']
#st.session_state.vnuri = 0
st.subheader("Proyectos")




def actualizar():
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
        actualiza = "UPDATE proyectos SET proyecto = :pro"
        actualiza = actualiza + " WHERE nuri = :nuri ;"
        session.execute(text(actualiza), {"pro": vpro,"nuri": tnuri})
        session.commit()

def ingresar():
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
        actualiza = "insert into proyectos (nuri,proyecto)"
        actualiza = actualiza + " values (nextval('proyecto_seq'),:proyecto) ;"
        session.execute(text(actualiza), {"proyecto": vpro})
        session.commit()


tipo = st.session_state['vTipo'] 
if tipo == 'Editar':
    tpro = st.session_state['vpro'] 
    tnuri = st.session_state['vnuri'] 


if tipo == 'Ingresar':
    tpro = ''

vpro = st.text_input("Proyecto ", tpro)


col1, col2, = st.columns(2)
if col1.button("Grabar" ,  type='primary'):
    if tipo == 'Editar':
        actualizar()
    if tipo == 'Ingresar':
        ingresar()
    st.switch_page("./pages/proyectos.py")
if col2.button("Cancelar"):
    st.switch_page("./pages/proyectos.py")
