import streamlit as st
import psycopg2
import os
from sqlalchemy import text
from streamlit_option_menu import option_menu

conn = st.connection("postgresql", type="sql")
activa = "S"
qq = 'select nuri,fuente as url,activa,fecha_act,descrip as fuente,pais,fuente_org,urllink,tipo_busq,posjson,tipo_img,postit,posdet from fuentes_py where proyecto_nuri = 1 ;'
df1 = conn.query(qq, ttl="0"),
df = df1[0]
st.write(df)
df["activa"] = df["activa"].astype(str)
df = df[df['activa'] == 'S']
#df = df[df['activa'] 
st.write(len(df))
for index in range(len(df)) :
   fnuri = df['nuri'].iloc[index]
   vquery = 'select * from fuentes_py where nuri = ' + str(fnuri) + ';'
   df2 = conn.query(vquery, ttl="0"),
   df3 = df2[0]
   st.session_state['vsepa'] = df3.to_string(columns=['separador'], header=False, index=False)
   st.session_state['vtit'] = df3.to_string(columns=['xpath_titulo'], header=False, index=False)
   st.session_state['vdet'] = df3.to_string(columns=['xpath_detalle'], header=False, index=False)
   st.session_state['vlink'] = df3.to_string(columns=['xpath_link'], header=False, index=False)
   st.session_state['vtipo'] = df3.to_string(columns=['tipo'], header=False, index=False)
   st.session_state['vbus'] = df3.to_string(columns=['busqueda_pers'], header=False, index=False)
   st.session_state['vidioma'] = df3.to_string(columns=['idioma'], header=False, index=False)
   st.session_state['vcod'] = df3.to_string(columns=['cod_pais'], header=False, index=False)
   st.session_state['vobserva'] = df3.to_string(columns=['observa'], header=False, index=False)
   st.session_state['vimagen'] = df3.to_string(columns=['xpath_image'], header=False, index=False)
   st.session_state['vdet'] = df3.to_string(columns=['xpath_detalle'], header=False, index=False)
   st.session_state['vatributo1'] = df3.to_string(columns=['atributo1'], header=False, index=False)
   st.session_state['vatributo2'] = df3.to_string(columns=['atributo2'], header=False, index=False)
   st.session_state['vtipobus'] = df3.to_string(columns=['tipo_busq'], header=False, index=False)
   st.session_state['vfuenteorg'] = df3.to_string(columns=['fuente_org'], header=False, index=False)
   st.session_state['vurllink'] = df3.to_string(columns=['urllink'], header=False, index=False)
   st.session_state['vposjson'] = df3.to_string(columns=['posjson'], header=False, index=False)
   st.session_state['vtipoimg'] = df3.to_string(columns=['tipo_img'], header=False, index=False)
   st.session_state['vpostit'] = df3.to_string(columns=['postit'], header=False, index=False)
   st.session_state['vposdet'] = df3.to_string(columns=['posdet'], header=False, index=False)
   st.session_state['vfuente'] = df3.to_string(columns=['url'], header=False, index=False)
   st.session_state['vdescrip'] = df3.to_string(columns=['fuente'], header=False, index=False)
   st.session_state['vnuri'] = df3.to_string(columns=['nuri'], header=False, index=False)
   st.session_state['vpais'] = df3.to_string(columns=['pais'], header=False, index=False)
   st.session_state['vactiva'] = df3.to_string(columns=['activa'], header=False, index=False)

   tnuri = st.session_state['vnuri']

   with conn.session as session:
      actualiza = "UPDATE fuentes_py SET  fecha_act = current_date,cnt_noticias = :cnt, cnt_encontradas = :cnt1"
      actualiza = actualiza + " WHERE nuri= :nuri"  
      session.execute(text(actualiza), {"cnt": 1,"cnt1": 1, "nuri": tnuri})
     

