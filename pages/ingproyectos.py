import streamlit as st
import psycopg2
from sqlalchemy import text


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
