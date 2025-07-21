import streamlit as st
import os
import re
import sys
import psutil
import requests
import cssutils
from bs4 import BeautifulSoup
from lxml import html
import psycopg2
import json
import pandas as pd
from sqlalchemy import text
from urllib.request import urljoin
from streamlit_option_menu import option_menu
import numpy as np
import time
from re import search 
import urllib3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

import feedparser
CLEANR = re.compile('<.*?>') 


def scrapping(deje,dpeso):
  #dres = pd.DataFrame(columns=['tit','det','link','img','sel','eje','peso'], index=[0])
  dres = pd.DataFrame(columns=['tit','det','link','img','sel','eje','peso'])
  #st.write(dres)
  #st.write("inicio")
  def get_driver():
    options = webdriver.ChromeOptions()

    my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36  (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0 "
    
#    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument(f"--user-agent={my_user_agent}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument('--ignore-certificate-errors')    
#    options.add_argument("--enable-javascript")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument('--enable-logging')
    options.add_argument('--disable-infobars')  
    options.add_argument('--disable-extensions') 
    options.add_argument('--disable-popup-blocking')
    options.add_argument('disable-javascript')    
    
#     options.add_argument(f"--window-size={width}x{height}")
#    options.add_argument(f"--user-agent={my_user_agent}")
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    return webdriver.Chrome(service=service, options=options)

  def buscareje(df,tira):
    vnuri = 0
    st.session_state['vejenuri'] = ''
    index = -1
    #st.write(tira)
    for texto in df['palabraclave_es']:
       vnuri = 6
       index = tira.find(texto)
       if index > 0:
         result = df[df['palabraclave_es'] == texto]
         #st.write(result)
         vnuri = result.to_string(columns=['eje_nuri'], header=False, index=False)[0]
         st.session_state['vejenuri'] = result.to_string(columns=['eje_nuri'], header=False, index=False)[0]
         if vnuri == None:
           vnuri = 6
           #st.write("si")
         if vnuri == '':
           vnuri = 6
           #st.write("si")

         return vnuri
    for texto in df['palabraclave_en']:
       vnuri = 6
       index = tira.find(texto)
       if index > 0:
         result = df[df['palabraclave_en'] == texto]
         vnuri = result.to_string(columns=['eje_nuri'], header=False, index=False)[0]
         st.session_state['vejenuri'] = result.to_string(columns=['eje_nuri'], header=False, index=False)[0]
         if vnuri == None:
           vnuri = 6
           #st.write("si")
         if vnuri == '':
           vnuri = 6
           #st.write("si")

         return vnuri
#result = pd.DataFrame(None)



  def buscarpalabras(df,tira):
    vpeso = 0
    index = -1
    for texto in df['palabra']:
       index = tira.find(texto)
       if index > 0:
         result = df[df['palabra'] == texto]
         peso = result.to_string(columns=['peso'], header=False, index=False)[0]
         vpeso = vpeso + int(peso)
         
    return vpeso


  headers={
        'User-Agent': 'python-requests/2.31.0',
  }
  """
  headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36  (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0 "
      
  }
  """ 

  headers = {
    "authority": "www.google.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    # add more headers as needed
  }
  
  #conn = st.connection("postgresql", type="sql")
  #qq = 'select eje_nuri,palabraclave_es,palabraclave_en from palabrasclaves  ;'
  #df1 = conn.query(qq, ttl="0"),
  #st.write(df1[0])
  #qq = 'select peso,palabra from palabras_a_buscar  ;'
  #df2 = conn.query(qq, ttl="0"),

  #tira= 'Studies sedes aire plagas stress on the preparation of a sufficient carrier from egg protein and carrageenan for cellulase with optimization and application'
  #buscareje(df1[0],tira.split())

  titulodict = 'N'
  detalledict = 'N'
  separador = st.session_state['vsepa'] 
  vatrib1 = st.session_state['vatributo1'] 
  vatrib2 = st.session_state['vatributo2'] 
  xtitulo = st.session_state['vtit'] 
  xlink = st.session_state['vlink'] 
  ximage = st.session_state['vimagen'] 
  xdetalle = st.session_state['vdet'] 
  pag = st.session_state['vfuente'] 
  tipobusq = st.session_state['vtipobus'] 
  fuenteorg = st.session_state['vfuenteorg'] 
  urllink = st.session_state['vurllink'] 
  posjson = st.session_state['vposjson'] 
  vpostit = st.session_state['vpostit']
  vposdet = st.session_state['vposdet']
  vposlink = st.session_state['vposlink']
  vpos = int(posjson)
  vpostit = int(vpostit)
  vposdet = int(vposdet)
  vposlink = int(vposlink)
  ptipoimg =  st.session_state['vtipoimg'] 
  #st.write('atributo 1 ' + vatrib1)
  p = xtitulo.find("{")
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
  #   esto es para el caso del titulo que debe ser un diccionario
  if p1 > 0:
    sep1 = xdetalle[:p1-2]
    detalledict = 'S'
    sepd =sep1.replace('"','')
    #st.write(sepd)
    resto = xdetalle[p1:100]
    p1 = resto.find(":")
    atr1 = resto[:p1]
    atr1 = atr1[1:100]
    atr1 =atr1.replace('"','')
    #st.write(atr1)
    atr2 = resto[p1+1:len(resto)-1]
    atr2 =atr2.replace('"','')
    #st.write(atr2)
    pattern = re.compile(atr2 +".*")
    dictdet = {atr1:atr2}
    #dictdet = {atr1:pattern}
    #st.write(dictdet)



  tnuri = st.session_state['vnuri']
  vurl = st.session_state['vfuente']
  #st.write('Fuente a Verificar :  ' + vurl)
  #st.write(xtitulo)
  #st.write(sepd)
  newv = ''
  if vatrib1 != '':

    pattern = re.compile(vatrib2 +".*")
    newv = {vatrib1:pattern}
    #newv = {vatrib1:vatrib2}

  if tipobusq == 'feedparser':
    d = feedparser.parse(vurl)
    st.write(d['feed']['title']   )
    cnt = len(d['items'])
    st.write(len(d['items']))
    for i in range(1, cnt):
       e = d['items'][i]
       tit = e['title']
       det = e['description']
       link = e['link']
       tit = re.sub(r"<.*?>", "", tit)
       det = re.sub(r"<.*?>", "", det)
       img = ''
       eje_nuri = buscareje(deje[0],tit + ' ' + det)
       peso = buscarpalabras(dpeso[0],tit + ' ' + det)
       ap = pd.DataFrame([{'tit': tit, 'det': det, 'link': link,'img': img,'eje': eje_nuri,'peso': peso}])
       dres = pd.concat([dres,ap])            

      
  if tipobusq == 'rss':

   
    #headers={
    #    'User-Agent': 'python-requests/2.31.0',
    #}    
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0',
    }    



    resp = requests.get(vurl, headers=headers, timeout=None)
    st.write(resp)  
    #soup = BeautifulSoup(resp.text, 'html.parser')
    soup = BeautifulSoup(resp.text, 'xml')
    #st.write(soup)
    pp = soup.find_all(separador)
    #st.write(pp)
    for entry in soup.find_all(separador):
      tit = entry.find(xtitulo).text
      pref = xlink.find('href')
      if pref > 0 :
        ll = entry.find(re.compile("^link") )    
        link =  ll['href']
      else:
        link =  entry.find(xlink).text
      try:  
        det =  entry.find(xdetalle).text
      except:
        det = 'No'
      pref = ximage.find('url')
      img = ''
      if pref > 0 :
        sep = ximage[:pref-1]
        #st.write(sep)
        ll = entry.find(re.compile("^" + sep) )    
        #ll = entry.find(re.compile("^enclosure") )    
        img =  ll['url']
      else:
        if ximage != 'none':
            img =  entry.find(ximage).text

      
      #vimg =  entry.find(re.compile("^enclosure")) 
      #img =  vimg['url']  
      #det = re.sub(CLEANR, '', det)
      tit = re.sub(r"<.*?>", "", tit)
      det = re.sub(r"<.*?>", "", det)

    
      #det =  det.encode('latin-1')
      
      eje_nuri = buscareje(deje[0],tit + ' ' + det)
      peso = buscarpalabras(dpeso[0],tit + ' ' + det)
      ap = pd.DataFrame([{'tit': tit, 'det': det, 'link': link,'img': img,'eje': eje_nuri,'peso': peso}])
      dres = pd.concat([dres,ap])            


  if tipobusq == 'rsssele':

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--log-level=3')
    driver = get_driver()
    driver.implicitly_wait(10)
    driver.get(vurl)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    time.sleep(1)        
    soup = BeautifulSoup(driver.page_source, 'xml')

    
    headers={
        'User-Agent': 'python-requests/2.31.0',
    }    
    #st.write("antes")
    #resp = requests.get(vurl, headers=headers, timeout=None)
    #st.write(resp)  
    #soup = BeautifulSoup(resp.text, 'html.parser')
    #soup = BeautifulSoup(resp.text, 'xml')
    pp = soup.find_all(separador)
    #st.write(pp)
    for entry in soup.find_all(separador):
      tit = entry.find(xtitulo).text
      pref = xlink.find('href')
      if pref > 0 :
        ll = entry.find(re.compile("^link") )    
        link =  ll['href']
      else:
        link =  entry.find(xlink).text
      try:  
        det =  entry.find(xdetalle).text
      except:
        det = 'No'
      pref = ximage.find('url')
      img = ''
      if pref > 0 :
        sep = ximage[:pref-1]
        #st.write(sep)
        ll = entry.find(re.compile("^" + sep) )    
        #ll = entry.find(re.compile("^enclosure") )    
        img =  ll['url']
      else:
        if ximage != 'none':
            img =  entry.find(ximage).text

      
      #vimg =  entry.find(re.compile("^enclosure")) 
      #img =  vimg['url']  
      #det = re.sub(CLEANR, '', det)
    
      #det =  det.encode('latin-1')
      tit = re.sub(r"<.*?>", "", tit)
      det = re.sub(r"<.*?>", "", det)
      
      
      eje_nuri = buscareje(deje[0],tit + ' ' + det)
      peso = buscarpalabras(dpeso[0],tit + ' ' + det)
      ap = pd.DataFrame([{'tit': tit, 'det': det, 'link': link,'img': img,'eje': eje_nuri,'peso': peso}])
      dres = pd.concat([dres,ap])   
      
  if tipobusq== 'json':
    my_url = vurl

    cookies = {
        "Hm_lpvt_7cd4710f721b473263eed1f0840391b4": "1548175412",
        "Hm_lvt_7cd4710f721b473263eed1f0840391b4": "1548140525",
        "x5sec":"7b22617365727665722d6c617a6164613b32223a223832333339343739626466613939303562613535386138333266383365326132434c4b516e65494645495474764a322b706f6d6f6941453d227d", }


    url = vurl
    cookies = {
        "Hm_lpvt_7cd4710f721b473263eed1f0840391b4": "1548175412",
        "Hm_lvt_7cd4710f721b473263eed1f0840391b4": "1548140525",
        "x5sec":"7b22617365727665722d6c617a6164613b32223a223832333339343739626466613939303562613535386138333266383365326132434c4b516e65494645495474764a322b706f6d6f6941453d227d", }
  
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--log-level=3')
    driver = get_driver()
    driver.implicitly_wait(10)
    driver.get(url)
        #driver.implicitly_wait(40)
        #wait = WebDriverWait(driver, 10)
        #wait.until(EC.url_contains("code="))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    time.sleep(1)        
        #WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "id_of_element_present_in_all_situation")))
    #st.write(driver.page_source)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    #st.write(soup)

    

    
    ret = requests.get(my_url, cookies=cookies)
    page_soup = BeautifulSoup(ret.text, 'lxml')
    r = requests.get(my_url)
    soup1 = BeautifulSoup(r.content, 'html.parser')
    if vatrib1 =='':
      pp = page_soup.select(separador)[vpos]
      ojson = json.loads(pp.string)
    else:
      #st.write(newv)
      #data = page_soup.select(separador,newv)[vpos]
      #data = page_soup.select("[type='application/ld+json']")[2]
      data = page_soup.select(separador)[vpos]
      #st.write(data)
      ojson = json.loads(data.string)["itemListElement"]
      #st.write(ojson)
      #pp = data
      
    for product in ojson:
        try:
          titu = product[xtitulo]
        except:
          titu = ''
        try:
          det =  product[xdetalle]
        except:
          det = ''
        if det == None:
          det = ''
        link = str(product[xlink]) 
        img = ''
        if ximage != 'none':
          vimg = product[ximage]
        #st.write('Titulo  :  '  + titu)
        #st.write('Detalle :  ' +  det )
        #st.write('link' +  link )
        #st.write( vurl )
        if link != None:
          if not link.startswith('http'):
              link = "/link/" + link
              #st.write(vurl)
              #link = urljoin(vurl, link)
              link = vurl+ link
        eje_nuri = buscareje(deje[0],titu + ' ' + det)
        peso = buscarpalabras(dpeso[0],titu + ' ' + det)
        ap = pd.DataFrame([{'tit': titu, 'det': det, 'link': link,'img': img,'eje': eje_nuri,'peso': peso}])
        dres = pd.concat([dres,ap])            
      

    

  if tipobusq != 'json' and tipobusq != 'rss' and tipobusq != 'rsssel' and tipobusq != 'feedparser'  :
    url = vurl
    #st.write("aca 1")
    cookies = {
        "Hm_lpvt_7cd4710f721b473263eed1f0840391b4": "1548175412",
        "Hm_lvt_7cd4710f721b473263eed1f0840391b4": "1548140525",
        "x5sec":"7b22617365727665722d6c617a6164613b32223a223832333339343739626466613939303562613535386138333266383365326132434c4b516e65494645495474764a322b706f6d6f6941453d227d", }
  
    if tipobusq == 'sele':

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--log-level=3')
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)      
      
        driver = get_driver()
        driver.implicitly_wait(10)
        driver.get(url)
        #driver.implicitly_wait(40)
        #wait = WebDriverWait(driver, 10)
        #wait.until(EC.url_contains("code="))
        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        time.sleep(3)        
        #WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "id_of_element_present_in_all_situation")))
        #st.write(driver.page_source)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        #soup = BeautifulSoup(driver.page_source, 'html.parser')
      
        #st.write(soup)
        time.sleep(3)        
        
        #st.write("sele")
    else:
        #st.write("otro hasta aca 1")

        headers = {
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0'
        }      
        try:
           response = requests.get(url,headers=headers, timeout=2)
           #st.write("no no")
           #st.stop()
           #st.write(response)
        except:
          return dres
          #st.write("no")
        #st.write(response.status_code)
        #st.write(response)
        time.sleep(2) 
        ret = requests.get(url, cookies=cookies ,headers=headers)
        #st.write(ret)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'lxml')
        #st.write(soup)
  
    if vatrib1 != '':
        noticias = soup.find_all(separador,newv)
    if vatrib1 == '':    
        noticias = soup.find_all(separador)
    if tipobusq == 'sub':
      if vatrib2 == '':
        data1 = soup.find(vatrib1)
      else:
        data1 = soup.find(vatrib1,vatrib2)
      #st.write(data1)  
      noticias = data1.find_all(separador)
    #st.write(noticias)
    for p in noticias:
        title = p.find(xlink)
        if title==None:
            #st.write("primero")
            title= p.get("href")
            if vposlink > 0:
               title = title[vposlink].text
            href = title
        else:
            href = title.get("href") 
            if vposlink > 0:
                #st.write("segundo")
                vtitle = p.find_all(xlink)
                #st.write(vtitle)
                #title = vtitle[vposlink].text
                #st.write(vtitle[vposlink].get("href"))
                href = vtitle[vposlink].get("href")
                
          
        if titulodict == 'S':
            try:
              vtitle = p.find_all(sep,dictitu )  
              #st.write(vtitle)  
              title = vtitle[vpostit].text
            except:
              title =''
        else:                
            try:
                vtitle = p.find_all(xtitulo)
                title = vtitle[vpostit].text
            except:
                try:
                    title = p.find(xtitulo).text
                except:
                    title = ''
        det = p.find_all(xdetalle)
        if detalledict=='S':
          try:
            vdet = p.find_all(sepd,dictdet )    
            #st.write(vdet)  
            det = vdet[vposdet].text  
          except:
            det = 'no'
        else:
          try:
            vdet = p.find_all(xdetalle)
            det = vdet[vposdet].text
          except:           
            det = 'No'
        # tipo de imagen puede ser src,data-src',data-breeze
        img = ''
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

        if ximage == 'background':
          div_style = p.find(ptipoimg)['style']
          style = cssutils.parseStyle(div_style)
          img = style['background-image']
          #style.split("('", 1)[1].split("')")[0]
          img = img.replace('url(', '').replace(')', '') 
          #st.write(img)
          if img == '':
             img = style['background']
             #img = img.replace('url(', '').replace(')', '')   
             img = img.replace('url(', '')
             pp = img.find(')')
             #st.write(pp)
             img = img[0:pp]
             #st.write(img)
             #st.write(vurl)
        if not img.startswith('http'):
           img = urljoin(vurl, img)
        if href != None:
          if not href.startswith('http'):
              href = urljoin(vurl, href)

        eje_nuri = 0
        peso = 0
        title = re.sub(r"<.*?>", "", title)
        det = re.sub(r"<.*?>", "", det)
      
        eje_nuri = buscareje(deje[0],title + ' ' + det)
        peso = buscarpalabras(dpeso[0],title + ' ' + det)
        if eje_nuri == None:
          eje_nuri = 6

        if title !='':
           ap = pd.DataFrame([{'tit': title, 'det': det, 'link': href,'img': img,'eje': eje_nuri,'peso': peso}])
           dres = pd.concat([dres,ap])            
                  


  return dres      
