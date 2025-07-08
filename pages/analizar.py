import streamlit as st
import psycopg2
import os
from sqlalchemy import text
from streamlit_option_menu import option_menu

conn = st.connection("postgresql", type="sql")
qq = 'select nuri,fuente as url,activa,fecha_act,descrip as fuente,pais,fuente_org,urllink,tipo_busq,posjson,tipo_img,postit,posdet from fuentes_py where proyecto_nuri = 1   and activa = ' +  '"S";'
df1 = conn.query(qq, ttl="0"),
df = df1[0]
st.write(df.len)
