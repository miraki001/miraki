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
                    padding-left: 2rem;
                    padding-right: 2rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)


#vnuri = st.session_state['vnuri']
#st.session_state.vnuri = 0
st.subheader("Miraki - Ejes")




def actualizar():
    conn = st.connection("postgresql", type="sql")
    vsec1 = st.session_state['vsec1']
    #st.write(veje1)
    vquery = "select nuri,sector from sectores where sector = :sector  ;"
    df2 = conn.query(vquery, ttl="0",params={"eje": veje1}),
    vsec_nuri = df2[0].to_string(columns=['nuri'], header=False, index=False)


    
    with conn.session as session:
        actualiza = "UPDATE ejestemas SET sector_nuri = :sec_nuri"
        actualiza = actualiza + " ,eje = :eje "
        actualiza = actualiza + " WHERE nuri = :nuri ;"
        session.execute(text(actualiza), {"sec_nuri": vsec_nuri,"eje": eje,"nuri": tnuri})
        session.commit()

def ingresar():
    conn = st.connection("postgresql", type="sql")
    vquery = "select nuri,sector from sectores where sector = :sector  ;"
    df2 = conn.query(vquery, ttl="0",params={"eje": veje1}),
    vsec_nuri = df2[0].to_string(columns=['nuri'], header=False, index=False)
  
    with conn.session as session:
        actualiza = "insert into ejestemas (nuri,sector_nuri,eje)"
        actualiza = actualiza + " values (nextval('ejestemas_seq'),:sec_nuri,:eje) ;"
        session.execute(text(actualiza), {"sec_nuri": vsec_nuri,"eje": veje})
        session.commit()




tipo = st.session_state['vTipo'] 
if tipo == 'Editar':
    tsec = st.session_state['vsec'] 
    teje = st.session_state['veje'] 
    conn = st.connection("postgresql", type="sql")
    df1 = conn.query('select nuri,sector from sectores ;', ttl="0"),
    df = df1[0]
    pos = df[df['sector']==tsec].index.item()

    
    tsec_nuri = st.session_state['vsec_nuri'] 
    tnuri = st.session_state['vnuri'] 

if tipo == 'Ingresar':
    teje = ''
    tsec_nuri = 0
    pos = 0

vsector = st.selectbox('Sector ', df.sector ,index= pos)
st.session_state['vsec1'] = vsector
veje = st.text_input("Eje ", teje )


col1, col2, = st.columns(2)
if col1.button("Grabar" ,  type='primary'):
    if tipo == 'Editar':
        actualizar()
    if tipo == 'Ingresar':
        ingresar()
    st.switch_page("./pages/ejes.py")
if col2.button("Cancelar"):
    st.switch_page("./pages/ejes.py")
