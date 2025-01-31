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


def find_a_string(value):
    return lambda text: value in text

col1, col2 = st.columns(2)



if col1.button("Home"):
    st.switch_page("streamlit_app.py")
if col2.button("Fuentes"):
    st.switch_page("./pages/fuentes.py")

titulodict = 'N'
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
st.write(xtitulo)
p = xtitulo.find("{")
#   esto es para el caso del titulo que debe ser un diccionario
if p != 0:
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
    #st.write(noticias)    
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
                st.write('titu1' + title)
            except ValueError:
                title = p.find(xtitulo).text
        
        #st.write(title)        
        try:    
            #det = p.find(xdetalle).text
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
                
                st.write(img)
            except ValueError:
                img = ''

            
            #file_name = p.search(".*/(.*png|.*jpg)$", img_url)
            #st.write('Imagen : ' + img)
        if not href.startswith('http'):
            href = urljoin(vurl, href)
        st.write('Link : ' + href)
        st.write('Titulo :  ' + title)
        st.write('Detalle :  ' + det)
