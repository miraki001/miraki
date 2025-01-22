import streamlit as st
import psycopg2
from sqlalchemy import text

st.set_page_config(layout="wide")
conn = st.connection("postgresql", type="sql")
tnuri = st.session_state['vnuri']
st.write(tnuri)
tnuri = int(tnuri)


with conn.session as session:
    actualiza = "INSERT INTO fuentes_py( nuri, fuente, fecha_act, activa, tipo, descrip, proyecto_nuri, limite, tema, busqueda_pers, pais, idioma, separador, xpath_titulo, xpath_detalle, xpath_autores, sep_autores, cnt_noticias, utfdecode, xpath_publica, act_url_fecha, urlencode, cnt_encontradas, baja_def, observa, cod_pais, xpath_link, xpath_image, atributo1, atributo2, tipo_busq, fuente_org, urllink, posjson)"
    actualiza = actualiza  + " select nextval('fuentes_py_seq')  , fuente, fecha_act, activa, tipo, descrip, proyecto_nuri, limite, tema, busqueda_pers, pais, idioma, separador, xpath_titulo, xpath_detalle, xpath_autores, sep_autores, cnt_noticias, utfdecode, xpath_publica, act_url_fecha, urlencode, cnt_encontradas, baja_def, observa, cod_pais, xpath_link, xpath_image, atributo1, atributo2, tipo_busq, fuente_org, urllink, posjson  " 
    actualiza = actualiza + " from fuentes_py where nuri = :nuri ;"
    session.execute(text(actualiza), {"nuri": tnuri})
    session.commit()
    
st.switch_page("./pages/fuentes.py")
