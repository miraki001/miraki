import streamlit as st
import os
import re
import sys
import psycopg2
import json
import pandas as pd
from sqlalchemy import text
from streamlit_option_menu import option_menu
import numpy as np
import time
from scrapp import scrapping

dres = scrapping.scrapping() 
st.write(dres)
dres = dres.dropna()
dres = dres.mask(dres.eq('None')).dropna()
dres = dres.mask(dres.astype(object).eq('None')).dropna()

col1, col2 = st.columns(2)

for index in range(len(dres)) :
   tit = dres['tit'].iloc[index]
   det = dres['det'].iloc[index]
   link = dres['link'].iloc[index]
   img = dres['img'].iloc[index]
   eje = dres['eje'].iloc[index]
   peso = dres['peso'].iloc[index]
   st.write(link)

   with col1:
     st.write('Link : ' + link)
     st.write('Titulo :  ' + tit)
     st.write('Detalle :  ' + det)
     st.write('Imagen :  ' +  img)
     st.write('Peso :  ' +  str(peso))
     st.write('Eje :  ' +  str(eje))
     
   with col2:
        if img != '':
            st.image(
                img,
                width=200, # Manually Adjust the width of the image as per requirement
            )
