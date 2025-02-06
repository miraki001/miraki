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


vtitulo = st.session_state['vtitulo']
veje1 = st.session_state['veje']
votro_nuri = st.session_state['vnuri1']
#st.write(veje1)
#st.write(votro_nuri)
conn = st.connection("postgresql", type="sql")




df1 = conn.query('select nuri,eje from ejestemas ;', ttl="0"),
df = df1[0]


pos = df[df['eje']==veje1].index.item()
#st.write(pos)
tnuri = st.session_state['vnuri1']
#st.write(tnuri)
ttitulo = st.session_state['vtitulo']

def actualizar():
    conn1 = st.connection("postgresql", type="sql")
    veje1 = st.session_state['veje']
    st.write(veje1)
    vquery = "select nuri,eje from ejestemas where eje = :eje  ;"
    
  
    
    df2 = conn1.query(vquery, ttl="0",params={"eje": veje1}),
    ejenuri = df2[0].to_string(columns=['nuri'], header=False, index=False)

  
    with conn.session as session:
        actualiza = "UPDATE novedades SET titulo = :titulo"
        actualiza = actualiza + " ,detalle = :detalle "
        actualiza = actualiza + " ,link = :link "
        actualiza = actualiza + " ,titulo_es = :titulo_es "
        actualiza = actualiza + " ,detalle_es = :detalle_es "
        actualiza = actualiza + " ,imagen = :imagen "
        actualiza = actualiza + " ,ejenuri = :ejenuri "
        actualiza = actualiza + " WHERE nuri = :nuri ;"
        session.execute(text(actualiza), {"titulo": vtitle,"detalle": vdet,"titulo_es": vtitle_es,"detalle_es": vdet_es, "link": vlink,"imagen": vimg,"ejenrui": ejenuri, "nuri": tnuri})
        session.commit()

def ingresar():
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
        actualiza = "insert into novedades (nuri,proyecto_nuri,sector,color)"
        actualiza = actualiza + " values (nextval('sectores_seq'),:proyecto_nuri,:sector,:color) ;"
        session.execute(text(actualiza), {"proyecto_nuri": vpro_nuri,"sector": vsector,"color": vcolor})
        session.commit()


def borrar():
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
      actualiza = 'delete from novedades where nuri = ' +  tnuri
      session.execute(text(actualiza) )
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
  vtitle = st.text_input("**Titulo**", ttitulo)
  vtitle_es = st.text_input("**Titulo en Castellano** ", st.session_state['vtitulo_es'])

  vdet= st.text_input("**Detalle**", st.session_state['vdetalle'])
  vdet_es = st.text_input(":red[Detalle en Castellano] ", st.session_state['vdetalle_es'])

  vlink = st.text_input("**Link** ", st.session_state['vlink'])
  vimg = st.text_input("**Imagen** ", st.session_state['vimagen'])

  
with col[1]:
  #veje = st.selectbox('Categoria ', df.eje , df.columns.tolist().index('nuri'),placeholder="Enoturismo")
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
