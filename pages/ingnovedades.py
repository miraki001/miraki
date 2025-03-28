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


df11 = conn.query('select nuri,descrip from fuentes_py ;', ttl="0"),
df2 = df11[0]

tnuri = 0
ttitulo = ''



def ingresar():

    eje =  st.session_state['veje'] 
    fuente =  st.session_state['vfuente'] 
    vquery = "select nuri from ejestemas where eje = :eje  ;"
    df4 = conn.query(vquery, ttl="0",params={"eje": veje}),
    veje_nuri = df4[0].to_string(columns=['nuri'], header=False, index=False)

    vquery = "select nuri from fuentes_py where descrip = : fuente  ;"
    df44 = conn.query(vquery, ttl="0",params={"fuente": vfuente}),
    vfuente_nuri = df44[0].to_string(columns=['nuri'], header=False, index=False)

  
    conn = st.connection("postgresql", type="sql")
    fuente = st.session_state['vfuente']
    with conn.session as session:
        actualiza = "insert into novedades (nuri,proyecto_nuri,fuente,titulo,detalle,titulo_es,detalle_es,link,imagem,fecha,nro_reporte,eje_nuri,fuente_nuri)"
        actualiza = actualiza + " values (nextval('novedades_seq'),1,:fuente,:titulo,:detalle,:titulo_es,:detalle_es,:link,:imagem,current_date,0,:eje_nuri,:fuente_nuri) ;"
        session.execute(text(actualiza), {"fuente": fuente,"titulo": vtitle_es,"detalle": vdet_es,"titulo_es":vtitle_es,"detalle_es":vdet_es,"link": vlink,"imagen": vimg,"eje_nuri" : eje,"fuente_nuri" : fuente_nuri  })
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
  
  veje = st.selectbox('Categoria ', df.eje ,index= 0)
  st.session_state['veje'] = veje

  vfuente = st.selectbox('Fuente ', df2['descrip'].unique() ,index= 0)
  st.session_state['vfuente'] = vfuente




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
