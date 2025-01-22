import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None)


st.markdown(
    """
    <style>
      [data-testid="collapsedControl"] {
          display: none
      }
    </style>
    """,
  unsafe_allow_html=True,
)


st.subheader("Parametros")

selected3 = option_menu(None, ["Home", "Palabras","Excluidas","Sectores","Ejes","PalabrasporSector","Proyectos" ], 
      icons=['house', 'gear' ,'gear'] , menu_icon="cast",orientation="horizontal", default_index = 0,
                
      styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white", "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
      }
)

if selected3=="Home":
    st.switch_page("miraki.py") 
if selected3=="Palabras Claves":
    st.switch_page("./pages/palabrasclaves.py")  
if selected3=="Excluidas":
    st.switch_page("./pages/editar_fuentes.py")  
if selected3=="Sectores":
    st.switch_page("./pages/sectores.py")  
if selected3=="Ejes":
    st.switch_page("./pages/ejes.py")
if selected3=="Palabras por Sector":
    st.switch_page("./pages/ejes.py")
if selected3=="Proyectos":
    st.switch_page("./pages/fuentes.py")

pfuente = st.text_input("ingrese el nombre de la fuente")

