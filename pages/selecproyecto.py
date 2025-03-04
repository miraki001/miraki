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


admin = st.session_state['vadmin']
#st.session_state.vnuri = 0
st.subheader("Seleccionar Proyecto")
st.write(st.session_state['vproyecto'])
st.write(st.session_state['vpro'])


conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,proyecto from proyectos ;', ttl="0"),
df = df1[0]

vproyecto = st.session_state['vproyecto'] 
st.write(df)
st.write(vproyecto)
pos = df[df['proyecto']==vproyecto].index.item()






vpro = st.selectbox('Proyecto en el que desea trabajar', df.proyecto ,index= pos)
st.session_state['vpro'] = vpro

#vpro_nuri = st.number_input("Proyecto ", tpro_nuri)

if admin=='S':
    st.switch_page("./pages/novedades.py")
if admin !='S':
    st.switch_page("./pages/novedadessola.py")
