import streamlit as st
import psycopg2
import os
from sqlalchemy import text
from streamlit_option_menu import option_menu
from scrapp import scrapping

conn = st.connection("postgresql", type="sql")

def buscar_not(vtitu,vfuente,vproyecto):
  with conn.session as session:
    buscar = "select count(nuri) as cnt from novedades "
    buscar = buscar  + " where titulo = :titu  " 
    buscar = buscar + " and fuente_nuri = :fuente"
    buscar = buscar + " and proyecto_nuri = :proyecto ;"
    df2 = conn.query(buscar, ttl="0",params={"titu": vtitu,"fuente": vfuente,"proyecto": vproyecto}),
    #st.write(df2)
    #vcnt = df2['cnt']
    #st.write(vcnt)
    cnt = df2[0].to_string(columns=['cnt'], header=False, index=False)
    #st.write(cnt)
    return cnt

def ingresar(vtitu,vfuente,vproyecto,vfuente_nuri,vdet,vlink,veje,vimg,vpeso,vtipo):
      with conn.session as session:
        actualiza = "INSERT INTO novedades( nuri, fuente, titulo,detalle,tipo,fecha,selec,origen,link,tema,proyecto_nuri,select_web,selec_alerta,imagen,fuente_nuri,eje_nuri,orden,leido,puntaje) "
        actualiza = actualiza + "VALUES (nextval('novedades_seq'), :fuente, :titulo,:detalle,:tipo,current_date,:selec,:origen,:link,:tema,:proyecto_nuri,:web,:alerta,:imagen,:fuente_nuri,:eje_nuri,:nro,:leido,:puntaje);"
        session.execute(text(actualiza), {"fuente": vfuente,"titulo": vtitu,"detalle": vdet,"tipo": vtipo,"selec": 'N',"origen": 'A',"link": vlink,"tema": '',"proyecto_nuri": vproyecto,"web": 'N',"alerta": 'N',"imagen": vimg,"fuente_nuri": vfuente_nuri,"eje_nuri": veje,"nro": 5,"leido": 'N',"puntaje": vpeso})
        session.commit()
activa = "S"
qq = 'select * from fuentes_py where proyecto_nuri = 1 and nuri = 6073 ;'
df1 = conn.query(qq, ttl="0"),
df = df1[0]
st.write(df)
vpro = st.session_state['vpro']
df["activa"] = df["activa"].astype(str)
df = df[df['activa'] == 'S']
#df = df[df['activa'] 
#st.write(len(df))
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
   fuente = df['descrip'].iloc[index]
   tipo = df['tipo'].iloc[index]
  

   tnuri = st.session_state['vnuri']
   dres = scrapping.scrapping()
   vcnt = len(dres)
   vcnt1 = 0
   for index in range(len(dres)) :
      tit = dres['tit'].iloc[index]
      tit = tit[0:600]
      det = dres['det'].iloc[index]
      det = det[0:40000]
      link = dres['link'].iloc[index]
      link = link[0:1500]
      img = dres['img'].iloc[index]
      img = img[0:800]
      eje = dres['eje'].iloc[index]
      peso = dres['peso'].iloc[index]
      encontrada = buscar_not(tit,int(fnuri),int(vpro))
      st.write("encontrada :" + str(encontrada))
      if buscar_pers == 'S' and peso > 3:
        ingresar(tit,fuente,int(vpro),int(fnuri),det,link,eje,img,peso,tipo)
        vcnt1 = vcnt1 + 1
      if buscar_pers == 'N':
        ingresar(tit,fuente,int(vpro),int(fnuri),det,link,eje,img,peso,tipo)
        vcnt1 = vcnt1 + 1


   with conn.session as session:
      actualiza = "UPDATE fuentes_py SET  fecha_act = current_date,cnt_noticias = :cnt, cnt_encontradas = :cnt1"
      actualiza = actualiza + " WHERE nuri= :nuri"  
      session.execute(text(actualiza), {"cnt": vcnt,"cnt1": vcnt1, "nuri": str(fnuri)} )
      session.commit()
      dres = scrapping.scrapping()  
      st.write(dres)
st.write("Listo")
