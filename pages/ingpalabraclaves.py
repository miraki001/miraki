import streamlit as st
import psycopg2
from sqlalchemy import text


def actualizar():
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
        actualiza = "UPDATE palabras_a_buscar SET palabra = :palabra"
        actualiza = actualiza + " ,peso = :peso "
        actualiza = actualiza + " WHERE palabra= :palabra ;"
        session.execute(text(actualiza), {"palabra": vpalabra,"peso": vpeso})
        session.commit()

def ingresar():
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
        actualiza = "insert into palabras_a_buscar (palabra,peso)"
        actualiza = actualiza + " values (:palabra,:peso) ;"
        session.execute(text(actualiza), {"palabra": vpalabra,"peso": vpeso})
        session.commit()


tipo = st.session_state['vTipo'] 
if tipo == 'Editar':
    tpalabra = st.session_state['vpalabra'] 
    tpeso = st.session_state['vpeso'] 
    tpeso = int(tpeso)

if tipo == 'Ingresar':
    tpalabra = ''
    tpeso = 0


vpalabra = st.text_input("Palabra", tpalabra)

vpeso = st.number_input("Peso", tpeso)



col1, col2, = st.columns(2)
if col1.button("Grabar" ,  type='primary'):
    if tipo == 'Editar':
        actualizar()
    if tipo == 'Ingresar':
        ingresar()
    st.switch_page("./pages/palabrasclaves.py")
if col2.button("Cancelar"):
    st.switch_page("./pages/palabrasclaves.py")
