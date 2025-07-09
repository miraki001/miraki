import streamlit as st
import psycopg2
import os
from sqlalchemy import text
from streamlit_option_menu import option_menu
from scrapp import scrapping

conn = st.connection("postgresql", type="sql")

def buscar_not(vtitu,vfuente,vproyecto):
  with conn.session as session:
    buscar = "count(nuri) as cnt from novedades "
    buscar = buscar  + " where titulo = :titu  " 
    buscar = buscar + " and fuente_nuri = :fuente"
    buscar = buscar + " and proyecto_nuri = :proyecto ;"
    df2 = conn.query(buscar, ttl="0",params={"titu": vtitu,"fuente": vfuente,"proyecto": vproyecto})
    vcnt = df2[0].to_string(columns=['cnt'], header=False, index=False)
    return vcnt

activa = "S"
qq = 'select * from fuentes_py where proyecto_nuri = 1 and nuri = 6073 ;'
df1 = conn.query(qq, ttl="0"),
df = df1[0]
st.write(df)
vpro = st.session_state['vpro']
df["activa"] = df["activa"].astype(str)
df = df[df['activa'] == 'S']
#df = df[df['activa'] 
st.write(len(df))
for index in range(len(df)) :
   fnuri = df['nuri'].iloc[index]
   st.session_state['vsepa'] = df['separador'].iloc[index]
   st.session_state['vtit'] = df['xpath_titulo'].iloc[index]
   st.session_state['vdet'] = df['xpath_detalle'].iloc[index]
   st.session_state['vlink'] = df['xpath_link'].iloc[index]
   st.session_state['vtipo'] = df['tipo'].iloc[index]
   st.session_state['vbus'] = df['busqueda_pers'].iloc[index]
   st.session_state['vidioma'] = df['idioma'].iloc[index]
   st.session_state['vcod'] = df['cod_pais'].iloc[index]
   st.session_state['vobserva'] = df['observa'].iloc[index]
   st.session_state['vimagen'] = df['xpath_image'].iloc[index]
   st.session_state['vdet'] = df['xpath_detalle'].iloc[index]
   st.session_state['vatributo1'] = df['atributo1'].iloc[index]
   st.session_state['vatributo2'] = df['atributo2'].iloc[index]
   st.session_state['vtipobus'] = df['tipo_busq'].iloc[index]
   st.session_state['vfuenteorg'] = df['fuente_org'].iloc[index]
   st.session_state['vurllink'] = df['urllink'].iloc[index]
   st.session_state['vposjson'] = df['posjson'].iloc[index]
   st.session_state['vtipoimg'] = df['tipo_img'].iloc[index]
   st.session_state['vpostit'] = df['postit'].iloc[index]
   st.session_state['vposdet'] = df['posdet'].iloc[index]
   st.session_state['vfuente'] = df['fuente'].iloc[index]
   st.session_state['vdescrip'] = df['descrip'].iloc[index]
   st.session_state['vnuri'] =  df['nuri'].iloc[index]
   st.session_state['vpais'] = df['pais'].iloc[index]
   st.session_state['vactiva'] = df['activa'].iloc[index]
   st.session_state['vbuscapers'] = df['busqueda_pers'].iloc[index]
   buscar_pers =  df['busqueda_pers'].iloc[index]

   tnuri = st.session_state['vnuri']
   dres = scrapping.scrapping()
   vcnt = len(dres)
   for index in range(len(dres)) :
      tit = dres['tit'].iloc[index]
      det = dres['det'].iloc[index]
      link = dres['link'].iloc[index]
      img = dres['img'].iloc[index]
      eje = dres['eje'].iloc[index]
      peso = dres['peso'].iloc[index]
      encontrada = buscar_not(tit,int(fnuri),int(vpro))
      st.write("encontrada " + encontrada)
   
   vcnt1 = 1

   with conn.session as session:
      actualiza = "UPDATE fuentes_py SET  fecha_act = current_date,cnt_noticias = :cnt, cnt_encontradas = :cnt1"
      actualiza = actualiza + " WHERE nuri= :nuri"  
      session.execute(text(actualiza), {"cnt": vcnt,"cnt1": vcnt1, "nuri": str(fnuri)} )
      session.commit()
      dres = scrapping.scrapping()  
      st.write(dres)
st.write("Listo")
