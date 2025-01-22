import streamlit as st
import psycopg2
from sqlalchemy import text


def actualizar():
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
        actualiza = "UPDATE sectores SET proyecto_nuri = :pro_nuri"
        actualiza = actualiza + " ,sector = :sector "
        actualiza = actualiza + " ,color = :color "
        actualiza = actualiza + " WHERE nuri = :nuri ;"
        session.execute(text(actualiza), {"pro_nuri": vpro_nuri,"sector": vsector,"color": vcolor,"nuri": tnuri})
        session.commit()

def ingresar():
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
        actualiza = "insert into sectores (nuri,proyecto_nuri,sector,color)"
        actualiza = actualiza + " values (nextval('sectores_seq'),:proyecto_nuri,:sector,:color) ;"
        session.execute(text(actualiza), {"proyecto_nuri": vpro_nuri,"sector": vsector,"color": vcolor})
        session.commit()


tipo = st.session_state['vTipo'] 
if tipo == 'Editar':
    tsector = st.session_state['vsector'] 
    tpro_nuri = st.session_state['vpro_nuri'] 
    tcolor = st.session_state['vcolor'] 
    tnuri = st.session_state['vnuri'] 
    tpro_nuri = int(tpro_nuri)

if tipo == 'Ingresar':
    tsector = ''
    tcolor = ''
    tpro_nuri = 0

vpro_nuri = st.number_input("Proyecto ", tpro_nuri)

vsector = st.text_input("Sector ", tsector)
vcolor  = st.text_input("Color ", tcolor)


col1, col2, = st.columns(2)
if col1.button("Grabar" ,  type='primary'):
    if tipo == 'Editar':
        actualizar()
    if tipo == 'Ingresar':
        ingresar()
    st.switch_page("./pages/sectores.py")
if col2.button("Cancelar"):
    st.switch_page("./pages/sectores.py")
