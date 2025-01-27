
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
                    padding-left: 2rem;
                    padding-right: 2rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)


#vnuri = st.session_state['vnuri']
#st.session_state.vnuri = 0
st.subheader("Miraki - Sectores")




def actualizar():
    conn = st.connection("postgresql", type="sql")
    vpro = st.session_state['vpro']
    #st.write(veje1)
    vquery = "select nuri,proyecto from proyectos where proyecto = :proyecto  ;"
    df2 = conn1.query(vquery, ttl="0",params={"proyecto": vpro}),
    vpro_nuri = df2[0].to_string(columns=['nuri'], header=False, index=False)
  
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
