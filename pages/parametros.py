import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None)


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
                    padding-left: 5rem;
                    padding-right: 2rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

st.logo(
    "https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/MARCA%20ARRIBA%20PNG.png?alt=media&token=46705f1e-7f86-4d2b-b2ab-a7188a30b379",
    icon_image="https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/MARCA%20ARRIBA%20PNG.png?alt=media&token=46705f1e-7f86-4d2b-b2ab-a7188a30b379",
    size="large",
)

#vnuri = st.session_state['vnuri']
#st.session_state.vnuri = 0
st.subheader("    Parametros")

selected3 = option_menu(None, ["Parametros", "Palabras Claves","Excluidas","Sectores","Ejes","Palabras por Sector","Proyectos" ,"Home"], 
      icons=['house', 'alphabet' ,'x-circle','diagram-3','list-check','alphabet-uppercase','building-fill' ] , menu_icon="cast",orientation="horizontal", default_index = 0,
                
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
    st.switch_page("./pages/palabrassector.py")
if selected3=="Proyectos":
    st.switch_page("./pages/proyectos.py")

#pfuente = st.text_input("ingrese el nombre de la fuente")

st.write('<p style="font-size:22px; color:red;">Parametros</p>',
unsafe_allow_html=True)
#st.write('##')


#st.write('**Palabras claves :** Son usadas en las busqueda individuales de las paginas, en el caso que la novedades no estemos seguros que cumplen todas las condiciones de los temas que queremos ubicar. n  Por ejemplo en las busquedas de noticias en los diarios. ')

st.write(         
    """
        **Palabras claves :** Son usadas en las busqueda individuales de las paginas, en el caso que la novedades no
        estemos seguros que cumplen todas las condiciones de los temas que queremos ubicar.          
        Por ejemplo en las busquedas de noticias en los diarios.
        
        **Palabras excluidas :**  son aquellas palabras o frases que hacen excluir la novedad por completo.

        **Sectores :** se deben definir los sectores a vigilar.

        **Ejes :** Categorias dentro de los sectores que forman parte del árbol de busqueda o árbol tecnólogico.

        **Palabras por sector :**  Se deben defini las palabras claves por eje y por sectores que nos ayudan a clasificar las 
        novedades según a la categoria que represetan.  
        Se deben definir en todos los idiomas en los que se vayan a realizar las busquedas.

        **Proyectos :**  se pueden definir tanto proyectos u objetos de analisis como se desen.
        
        
    """
)

