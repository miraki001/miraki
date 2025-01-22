import streamlit as st
from streamlit_option_menu import option_menu



selected2 = option_menu(None, ["Miraki", 'Novedades','Fuentes', 'Informes','Parametros','Github' ], 
        icons=['house', 'gear' ,'gear'] , menu_icon="cast",orientation="horizontal", default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white",  "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#604283"}
        }
  )

if selected2=="Fuentes":
  st.switch_page("./pages/fuentes.py")
if selected2=="Parametros":
  st.switch_page("./pages/parametros.py")
        
st.header("Miraki")

st.write(
    """
        
        
        Plataforma de Vigilancia Tecnologica e Inteligencia Competitiva.
        
        ornare. Morbi id ex pulvinar dui placerat congue. Suspendisse ultricies, lacus
        eget porttitor blandit, enim nisi tincidunt eros, nec varius tortor turpis et
        tortor.

        Curabitur facilisis, augue eu eleifend dictum, quam lectus ullamcorper tellus,
        auctor mollis lacus turpis id tellus. Mauris consectetur eleifend dignissim.
        Integer nulla arcu, fringilla quis finibus vel, iaculis ac massa. Cras at
        mauris a magna blandit mattis. Nam vel turpis et risus tempus congue ac quis
        lectus. Pellentesque id laoreet ex, sit amet consequat leo. Aenean commodo
        luctus tristique. Curabitur arcu urna, tempus ut lectus et, pulvinar lobortis
        urna.
    """
)
