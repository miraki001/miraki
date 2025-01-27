import streamlit as st
import pandas as pd
import os
from streamlit_option_menu import option_menu
import psycopg2
from sqlalchemy import text
import numpy as np
from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode
from streamlit_echarts import st_pyecharts
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Line

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
                    padding-left: 2rem;
                    padding-right: 2rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)


#vnuri = st.session_state['vnuri']
#st.session_state.vnuri = 0
st.subheader("Miraki - Novedades")

tab1, tab2, tab3 = st.tabs(["Por Fuentes", "Tendencias", "Relaciones"])

with tab1:
    st.subheader("Cantidad de novedades por mes y año")
    conn = st.connection("postgresql", type="sql")
    df = conn.query('select periodo,sum(value) value from nov_por_anio group by periodo ;', ttl="0")
    df['periodo'] = df['periodo'].astype(str)

    newdf=df.set_index('periodo',inplace=False).rename_axis(None)

    option = {
        "dataZoom": [
        {
          "show": 'true',
          "realtime": 'true',
          "start": 30,
          "end": 70,
          "xAxisIndex": [0, 1]
        },
        {
          "type": 'inside',
          "realtime": 'true',
          "start": 30,
          "end": 70,
          "xAxisIndex": [0, 1]
        }
        ],
        "tooltip": {
            "trigger": 'axis',
            "axisPointer": { "type": 'cross' }
        },
        "legend": {},    
        "xAxis": {
            "type": "category",
            "data": df['periodo'].to_list(),
        },
        "yAxis": {"type": "value"},
        "series": [{"data": df['value'].to_list(), "type": "line", "name": 'Cnt Novedades'}
                   ]
    }
    st_echarts(
        options=option, height="400px" ,
    )
    df1 = conn.query('select fuente,sum(value) value from nov_por_anio group by fuente ;', ttl="0")
    #df['periodo'] = df['periodo'].astype(str)
    st.subheader("Cantidad de novedades según la fuente")
    st.bar_chart(df1, x="fuente", y="value",  horizontal=True)
with tab2:
    st.header("Tendencias")
with tab3:
    st.header("Relaciones")


