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
import requests
import pandas as pd
from sqlalchemy import text

col1, col2 = st.columns(2)



if col1.button("Home"):
    st.switch_page("streamlit_app.py")
if col2.button("Fuentes"):
    st.switch_page("./pages/fuentes.py")


separador = st.session_state['vsepa'] 
vatrib1 = st.session_state['vatributo1'] 
vatrib2 = st.session_state['vatributo2'] 
st.write(separador)
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



tnuri = st.session_state['vnuri']
vurl = st.session_state['vfuente']
st.write(vurl)
st.write(xtitulo)
st.write(xdetalle)
newv = {vatrib1:vatrib2}
st.write(newv)
        
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
        st.write(product[xtitulo])
        st.write(product[xdetalle])

    

if tipobus != 'json':
    url = vurl
    response = requests.get(url)
    html_content = response.content
    tree = html.fromstring(html_content)
    soup = BeautifulSoup(html_content, 'lxml')
    if vatrib1 != '':
        noticias = soup.find_all(separador,newv)
    if vatrib1 == '':    
        noticias = soup.find_all(separador)
    for p in noticias:
        title = p.find(xlink)
        href = title.get("href")
        title = p.find(xtitulo).get_text()
        det = p.find(xdetalle).get_text()
        if ximage !='none':
            img = p.find(ximage).get('data-src')
            st.write(img)
        st.write(href)
        st.write(title)
        st.write(det)
