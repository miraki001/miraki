import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None,page_title="Miraki")

vtitulo = st.session_state['vtitulo']

tnuri = st.session_state['vnuri']
ttitulo = st.session_state['vtitulo']

st.markdown("""
<style>
    .stTextInput input[aria-label="**Titulo**"] {
        background-color: #0066cc;
        color: #33ff33;
    }
    .stTextInput input[aria-label="test color2"] {
        background-color: #cc0066;
        color: #ffff33;
    }
</style>
""", unsafe_allow_html=True)

col = st.columns((14.5, 4.5, 2), gap='medium')


with col[0]:
  vtitle = st.text_input("**Titulo**", ttitulo)
  vtitle_es = st.text_input("**Titulo en Castellano** ", st.session_state['vtitulo_es'])

  vdet= st.text_input("**Detalle**", st.session_state['vdetalle'])
  vdet_es = st.text_input(":red[Detalle en Castellano] ", st.session_state['vdetalle_es'])

  vlink = st.text_input("**Link** ", st.session_state['vlink'])
  vimg = st.text_input("**Imagen** ", st.session_state['vimagen'])
with col[1]:
  st.image(
            vimg,
            width=400, # Manually Adjust the width of the image as per requirement
     )



col10, col20 = st.columns(2)
if col10.button(":red[**Grabar**]"):
    st.switch_page("streamlit_app.py")
if col20.button(":red[**Cancelar**]"):
    st.switch_page("streamlit_app.py")
