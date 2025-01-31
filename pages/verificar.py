import streamlit as st
import os
import re
import sys
import psutil
import requests
from bs4 import BeautifulSoup
from lxml import html
import psycopg2
import json
import pandas as pd
from sqlalchemy import text
from urllib.request import urljoin
from streamlit_option_menu import option_menu
import numpy as np
from re import search 

def buscareje(df,tira):
  vnuri = 0
  st.session_state['vejenuri'] = ''
  index = -1
  #st.write(tira)
  for texto in df['palabraclave_es']:
       index = tira.find(texto)
       if index > -1:
         result = df[df['palabraclave_es'] == texto]
         #st.write(result)
         vnuri = result.to_string(columns=['eje_nuri'], header=False, index=False)[0]
         st.session_state['vejenuri'] = result.to_string(columns=['eje_nuri'], header=False, index=False)[0]
         return vnuri
  for texto in df['palabraclave_en']:
       index = tira.find(texto)
       if index > -1:
         result = df[df['palabraclave_en'] == texto]
         vnuri = result.to_string(columns=['eje_nuri'], header=False, index=False)[0]
         st.session_state['vejenuri'] = result.to_string(columns=['eje_nuri'], header=False, index=False)[0]
         return vnuri
result = pd.DataFrame(None)

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
                    padding-left: 4rem;
                    padding-right: 2rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

st.logo(
    "https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/android-chrome-192x192.png?alt=media&token=e8d5f6ee-706a-4399-813d-fd82f8b35ec7",
    icon_image="https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/android-chrome-192x192.png?alt=media&token=e8d5f6ee-706a-4399-813d-fd82f8b35ec7",
)


def find_a_string(value):
    return lambda text: value in text

selected27 = option_menu(None, ["Miraki", 'Novedades','Fuentes', 'Informes','Parametros'], 
        icons=['house', 'newspaper' , 'filetype-html','globe-americas','gear'] , menu_icon="cast",orientation="horizontal", default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white",  "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
        }
  )

if selected27=="Fuentes":
  st.switch_page("./pages/fuentes.py")
if selected27=="Novedades":
  st.switch_page("./pages/novedades.py")       
if selected27=="Parametros":
  st.switch_page("./pages/parametros.py")        
if selected27=="Informes":
  st.switch_page("./pages/informes.py")    


col1, col2 = st.columns(2)

conn = st.connection("postgresql", type="sql")
qq = 'select eje_nuri,palabraclave_es,palabraclave_en from palabrasclaves  ;'
df1 = conn.query(qq, ttl="0"),
st.write(df1[0])


#tira= 'Studies sedes aire plagas stress on the preparation of a sufficient carrier from egg protein and carrageenan for cellulase with optimization and application'
#buscareje(df1[0],tira.split())

titulodict = 'N'
detalledict = 'N'
separador = st.session_state['vsepa'] 
vatrib1 = st.session_state['vatributo1'] 
vatrib2 = st.session_state['vatributo2'] 
#st.write(separador)
xtitulo = st.session_state['vtit'] 
xlink = st.session_state['vlink'] 
ximage = st.session_state['vimagen'] 
xdetalle = st.session_state['vdet'] 
pag = st.session_state['vfuente'] 
tipobusq = st.session_state['vtipobus'] 
fuenteorg = st.session_state['vfuenteorg'] 
urllink = st.session_state['vurllink'] 
posjson = st.session_state['vposjson'] 
vpos = int(posjson)
ptipoimg =  st.session_state['vtipoimg'] 
#st.write(xtitulo)
p = xtitulo.find("{")
#st.write(p)
#   esto es para el caso del titulo que debe ser un diccionario
if p > 0:
    sep = xtitulo[:p-2]
    titulodict = 'S'
    sep =sep.replace('"','')
    #st.write(sep)
    resto = xtitulo[p:100]
    #st.write(resto)
    p = resto.find(":")
    atr1 = resto[:p]
    atr1 = atr1[1:100]
    atr1 =atr1.replace('"','')
    #st.write(atr1)
    atr2 = resto[p+1:len(resto)-1]
    atr2 =atr2.replace('"','')
    #st.write(atr2)
    dictitu = {atr1:atr2}
    #st.write(dictitu)

p1 = xdetalle.find("{")
#st.write(p)
#   esto es para el caso del titulo que debe ser un diccionario
if p1 > 0:
    sep1 = xdetalle[:p1-2]
    detalledict = 'S'
    sepd =sep1.replace('"','')
    #st.write(sep)
    resto = xdetalle[p1:100]
    #st.write(resto)
    p1 = resto.find(":")
    atr1 = resto[:p1]
    atr1 = atr1[1:100]
    atr1 =atr1.replace('"','')
    #st.write(atr1)
    atr2 = resto[p+1:len(resto)-1]
    atr2 =atr2.replace('"','')
    #st.write(atr2)
    dictdet = {atr1:atr2}
    #st.write(dictitu)



tnuri = st.session_state['vnuri']
vurl = st.session_state['vfuente']
st.write('Fuente a Verificar :  ' + vurl)
#st.write(xtitulo)
#st.write(xdetalle)
pattern = re.compile(vatrib2 +".*")
newv = {vatrib1:pattern}
#st.write(newv)
        
if tipobusq== 'json':
    my_url = vurl

    cookies = {
        "Hm_lpvt_7cd4710f721b473263eed1f0840391b4": "1548175412",
        "Hm_lvt_7cd4710f721b473263eed1f0840391b4": "1548140525",
        "x5sec":"7b22617365727665722d6c617a6164613b32223a223832333339343739626466613939303562613535386138333266383365326132434c4b516e65494645495474764a322b706f6d6f6941453d227d", }

    ret = requests.get(my_url, cookies=cookies)
    page_soup = BeautifulSoup(ret.text, 'lxml')
    r = requests.get(my_url)
    soup1 = BeautifulSoup(r.content, 'html.parser')
    #pp = soup1.find_all('script')[14].text.strip()[48:-1]
    #pp = soup1.find_all('script')[14].text.strip()
    pp = soup1.find_all(separador)[14]
    #st.write(pp)
    #st.write('fffffff')
    #data = page_soup.select("[type='application/json']")[vpos]
    #data = page_soup.select(separador,newv)[vpos]
    #json.parse(data)
    #data = page_soup.select(separador)[vpos]
    #st.write(data)
    #pos1 = data.str.find('[')
    #st.write('pos1')
    #st.write(pos1)
    #pos2 = data.find(']')
    #st.write(pos2)

    ojson = json.loads(pp.string)
    #st.write(ojson)
    for product in ojson:
        st.write('Titulo  :  '  + product[xtitulo])
        st.write('Detalle :  ' + product[xdetalle])

    

if tipobusq != 'json':
    url = vurl
    #st.write(separador)
    response = requests.get(url)
    html_content = response.content
    tree = html.fromstring(html_content)
    soup = BeautifulSoup(html_content, 'lxml')
    #noticias = soup.find_all(string=re.compile("dg_news_hl_news_"))
    #st.write(noticias)
    if vatrib1 != '':
        noticias = soup.find_all(separador,newv)
    if vatrib1 == '':    
        noticias = soup.find_all(separador)

    if st.checkbox('Ver contenido extraido'):
        st.write(noticias)
    st.write(len(noticias))    
    for p in noticias:
        title = p.find(xlink)
        if title==None:
            title= p.get("href")
            href = title
        else:
            href = title.get("href") 
        #st.write(title)
        #href = title.get("href")
        if titulodict == 'S':
            title = p.find(sep,dictitu ).text     
        else:                
            try:
                title = p.find(xtitulo).get_text()
            except ValueError:
                title = p.find(xtitulo).text
        #st.write(title)        
        try:    
            #det = p.find(xdetalle).text
            if detalledict=='S':
                det = p.find(sepd,dictdet ).text    
            else:
                det = p.find(xdetalle).get_text()
        except ValueError:
            det = p.find(xdetalle).text
        # tipo de imagen puede ser src,data-src',data-breeze
        if ximage !='none':
            #img = p.find(ximage).get('data-src')
            img = ''
            try:
              img = p.find(ximage).get(ptipoimg)
              if img== None:
                img = p.find(ximage).get('src')
              if not img.startswith('http'):
                img = urljoin(vurl, img)                
            except:
              img = ''

            
            #file_name = p.search(".*/(.*png|.*jpg)$", img_url)
            #st.write('Imagen : ' + img)
        if not href.startswith('http'):
            href = urljoin(vurl, href)

        col1, col2 = st.columns(2)
      
        with col1:
          st.write('Link : ' + href)
          st.write('Titulo :  ' + title)
          st.write('Detalle :  ' + det)
          st.write('Imagen :  ' +  img)
          eje_nuri = 0
          eje_nuri = buscareje(df1[0],title)
          #eje_nuri = st.session_state['vejenuri'] 
          st.write('Eje')
          st.write(eje_nuri)
          st.session_state['vejenuri'] = 0


      
        with col2:
          if img != '':
                st.image(
                  img,
                  width=200, # Manually Adjust the width of the image as per requirement
                 )
