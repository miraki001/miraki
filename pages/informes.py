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
#import streamlit-wordcloud as wordcloud
from st_wordcloud import st_wordcloud
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components


st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None,page_title="Miraki🖼")


st.logo(
    "https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/MARCA%20ARRIBA%20PNG.png?alt=media&token=46705f1e-7f86-4d2b-b2ab-a7188a30b379",
    icon_image="https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/MARCA%20ARRIBA%20PNG.png?alt=media&token=46705f1e-7f86-4d2b-b2ab-a7188a30b379",
    size='large',
)

#https://github.com/drogbadvc/st-wordcloud
#https://github.com/minimaxir/stylecloud/blob/master/README.md
#https://ellibrodepython.com/dashboard-streamlit
st.markdown(
    """
        <style>
                .stAppHeader {
                    background-color: rgba(255, 255, 255, 0.0);  /* Transparent background */
                    background-position: 20px 20px;
                    visibility: visible;  /* Ensure the header is visible */
                }

               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 2rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

#st.image("./pages/favicon-32x32.png")
#vnuri = st.session_state['vnuri']
#st.session_state.vnuri = 0
st.subheader("Informes")

selected2 = option_menu(None, ["Miraki", 'Novedades','Fuentes', 'Informes','Parametros','Github' ], 
        icons=['house', 'newspaper' , 'filetype-html','globe-americas','gear','github'] , menu_icon="cast",orientation="horizontal", default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "#898989"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white",  "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#898989"}
        }
  )

if selected2=="Fuentes":
  st.switch_page("./pages/fuentes.py")
if selected2=="Novedades":
  st.switch_page("./pages/novedades.py")       
if selected2=="Parametros":
  st.switch_page("./pages/parametros.py")        
if selected2=="Informes":
  st.s

tab1, tab2, tab3,tab4 = st.tabs(["Por Fuentes", "Tendencias", "Relaciones","Otros"])

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

  
    df2 = conn.query('select categoria,sum(value) value from nov_cat_anio group by categoria ;', ttl="0")
    #df['periodo'] = df['periodo'].astype(str)
    st.subheader("Cantidad de novedades según la Categoria")
    st.bar_chart(df2, x="categoria", y="value",  horizontal=True)


with tab2:
    st.header("Tendencias")
    conn = st.connection("postgresql", type="sql")
    df = conn.query('select palabra as text,cnt as value from tag_words() ;', ttl="0")
    words = df.to_dict('records')
    #st.write(words)
    #words = [{"text": "Python", "value": 500, "topic": "lol"}, {"text": "Streamlit", "value": 80},{"text": "Streamlit", "value": 80},{"text": "Streamlit", "value": 80},{"text": "Streamlit", "value": 80},{"text": "Streamlit", "value": 80},{"text": "Streamlit", "value": 80}]

    st_wordcloud(words, width=800, height=600)


with tab3:
    st.header("Relaciones")
    conn = st.connection("postgresql", type="sql")
    df = conn.query('select titulo || detalle detalle,categoria from nov limit 100 ;', ttl="0")
    G = nx.from_pandas_edgelist(df,source='detalle', target='categoria' )

    drug_net = Network(
                       height='800px',
                       width='100%',
                       bgcolor='#222222',
                       font_color='white'
                      )

    # Take Networkx graph and translate it to a PyVis graph format
    drug_net.from_nx(G)

    # Generate network with specific layout settings
    drug_net.repulsion(
                        node_distance=420,
                        central_gravity=0.33,
                        spring_length=110,
                        spring_strength=0.10,
                        damping=0.95
                       )

    # Save and read graph as HTML file (on Streamlit Sharing)

    try:
        path = '/tmp'
        drug_net.save_graph(f'{path}/pyvis_graph.html')
        HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

    # Save and read graph as HTML file (locally)
    except:
        path = '/html_files'
        drug_net.save_graph(f'{path}/pyvis_graph.html')
        HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=635)

with tab4:
    st.header("Relaciones")
    conn = st.connection("postgresql", type="sql")
    df = conn.query('select titulo || detalle detalle,categoria from nov limit 100 ;', ttl="0")
    G = nx.from_pandas_edgelist(df,source='categoria', target='detalle' )

    drug_net = Network(
                       select_menu = False,
                       height='800px',
                       width='100%',
                       bgcolor='#222222',
                       font_color='white'
                      )

    # Take Networkx graph and translate it to a PyVis graph format
    drug_net.from_nx(G)

    # Generate network with specific layout settings
    drug_net.repulsion(
                        node_distance=420,
                        central_gravity=0.33,
                        spring_length=110,
                        spring_strength=0.10,
                        damping=0.95
                       )

    #drug_net.toggle_physics(False)
  
    # Save and read graph as HTML file (on Streamlit Sharing)

    try:
        path = '/tmp'
        drug_net.save_graph(f'{path}/pyvis_graph.html')
        HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

    # Save and read graph as HTML file (locally)
    except:
        path = '/html_files'
        drug_net.save_graph(f'{path}/pyvis_graph.html')
        HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=635)




