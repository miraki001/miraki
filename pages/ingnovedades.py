import streamlit as st
import psycopg2
import os
from sqlalchemy import text
import pandas as pd

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
st.subheader("Novedades")


vtitulo = ''
veje1 = ''
votro_nuri =0
#st.write(veje1)
#st.write(votro_nuri)
conn = st.connection("postgresql", type="sql")




df1 = conn.query('select nuri,eje from ejestemas ;', ttl="0"),
df = df1[0]


#pos = df[df['eje']==veje1].index.item()
#st.write(pos)
tnuri = 0
#st.write(tnuri)
ttitulo = ''



def ingresar():
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
        actualiza = "insert into novedades (nuri,proyecto_nuri,sector,color)"
        actualiza = actualiza + " values (nextval('sectores_seq'),:proyecto_nuri,:sector,:color) ;"
        session.execute(text(actualiza), {"proyecto_nuri": vpro_nuri,"sector": vsector,"color": vcolor})
        session.commit()



st.markdown("""
<style>
    .stTextInput input[aria-label="**Titulo**"] {
        background-color: #0066cc;
        color: #33ff33;
    }
    .stTextInput input[aria-label="test color2"] {
        background-color: #cc0066;
        color: #ffff33;
    }
</style>
""", unsafe_allow_html=True)

col = st.columns((14.5, 4.5, 2), gap='medium')


with col[0]:
  
  vtitle_es = st.text_input("**Titulo en Castellano** ", '')

  
  vdet_es = st.text_input(":red[Detalle en Castellano] ", '')

  vlink = st.text_input("**Link** ", '')
  vimg = st.text_input("**Imagen** ",'')

  
with col[1]:
  
  veje = st.selectbox('Categoria ', df.eje ,index= pos)
  st.session_state['veje'] = veje
  st.write('')
  st.write('')
  #st.write(veje)
  #st.write(veje.index)
  if vimg != '':
    st.image(
            vimg,
            width=600, # Manually Adjust the width of the image as per requirement
     )



col10, col20 = st.columns(2)
if col10.button(":red[**Grabar**]"):
    actualizar()
    st.switch_page("./pages/novedades.py")
if col20.button(":red[**Cancelar**]"):
    st.switch_page("./pages/novedades.py")
