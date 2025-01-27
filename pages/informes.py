import streamlit as st
import pandas as pd
import os
from streamlit_option_menu import option_menu
import psycopg2
from sqlalchemy import text
import numpy as np

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
    st.header("Por Fuentes")
with tab2:
    st.header("Tendencias")
with tab1:
    st.header("Relaciones")


