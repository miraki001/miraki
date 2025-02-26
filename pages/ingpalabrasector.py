import streamlit as st
import psycopg2
from sqlalchemy import text

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
  size='large',
)

df1 = conn.query('select nuri,eje from ejestemas ;', ttl="0"),
df = df1[0]

#vnuri = st.session_state['vnuri']
#st.session_state.vnuri = 0
st.subheader("Palabras Claves")





def actualizar():
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
        actualiza = "UPDATE palabras_a_buscar SET palabra = :palabra"
        actualiza = actualiza + " ,peso = :peso "
        actualiza = actualiza + " WHERE palabra= :palabra ;"
        session.execute(text(actualiza), {"palabra": vpalabra,"peso": vpeso})
        session.commit()

def ingresar():
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
        actualiza = "insert into palabras_a_buscar (palabra,peso)"
        actualiza = actualiza + " values (:palabra,:peso) ;"
        session.execute(text(actualiza), {"palabra": vpalabra,"peso": vpeso})
        session.commit()


tipo = st.session_state['vTipo'] 
if tipo == 'Editar':
    tpalabraes = st.session_state['vpalabraes'] 
    tpalabraen = st.session_state['vpalabraen'] 
   

if tipo == 'Ingresar':
    tpalabraes = ''
    tpalabraen = ''
   
veje = st.selectbox('Categoria ', df.eje ,index= 0)
st.session_state['veje'] = veje

vpalabraes = st.text_input("Palabra en Español", tpalabraes)
vpalabraen = st.text_input("Palabra en Ingles", tpalabraen)





col1, col2, = st.columns(2)
if col1.button("Grabar" ,  type='primary'):
    if tipo == 'Editar':
        actualizar()
    if tipo == 'Ingresar':
        ingresar()
    st.switch_page("./pages/palabrassector.py")
if col2.button("Cancelar"):
    st.switch_page("./pages/palabrassector.py")
