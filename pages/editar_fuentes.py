import streamlit as st
import psycopg2
from sqlalchemy import text

st.set_page_config(layout="wide")
conn = st.connection("postgresql", type="sql")

def ingresar():
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
        actualiza = "insert into fuentes_py (nuri, fuente,, activa, xpath_titulo, descrip, proyecto_nuri,pais,separador,atributo1,atributo2,xpath_detalle,xpath_link,xpath_image,tipo,busqueda_pers,idioma,cod_pais,tipo_busq,fuente_org,posjson,urllink )"
        actualiza = actualiza + " values (nextval('fuente_py_seq'),:fuente, :activa, :xpath_titulo , :descrip, 1,:pais,:separador,:atributo1,:atributo2,:xpath_detalle,:xpath_link,:xpath_image,:tipo,busqueda_pers,:idioma,:cod_pais,:tipo_busq,:fuente_org,:posjson,:urllink  );"
        session.execute(text(actualiza), {"fuente": vurl,"activa": activa,"tit": xpath_tit,"desc": vtitle, "pais": pais,"separador": separador,"atributo1": atributo1,"atributo2": atributo2, "det": xpath_det, "link": xpath_link,"image": xpath_image, "tipo": tipo,"busq": busqueda, "idioma": idioma,"cod": codigo,"tipo_busq" : tipobus ,"fuente_org": fuenteorg,"posjson": posjson, "urllink": urllink})
        
        session.commit()    

#vtitulo = st.session_state['vtitulo']
vtitulo1 = "eeeeee"

tipo = st.session_state['vTipo'] 
if tipo == 'Editar':
    fuente = st.session_state['vdescrip'] 
    pais = st.session_state['vpais'] 
    activa = st.session_state['vactiva'] 
    tnuri = st.session_state['vnuri']
    url = st.session_state['vfuente']
    vpos = st.session_state['vposjson']    
    vpos = int(vpos)
    tipobus = st.session_state['vtipobus']
    separador = st.session_state['vsepa']
    atributo1 = st.session_state['vatributo1']
    atributo2 = st.session_state['vatributo2']
    xpath_tit =  st.session_state['vtit']
    xpath_det = st.session_state['vdet']
    xpath_link = st.session_state['vlink']
    xpath_image = st.session_state['vimagen']
    fuenteorg = st.session_state['vfuenteorg']
    urllink = st.session_state['vurllink']
    pais =  st.session_state['vpais']
    activa = st.session_state['vactiva']
    tipo = st.session_state['vtipo']
    busqueda = st.session_state['vbus']
    idioma = st.session_state['vidioma']
    codigo = st.session_state['vcod']

if tipo == 'Editar':
    fuente = ''
    pais = ''
    activa = ''
    tnuri = 0
    url = ''
    vpos = 0
    vpos = int(vpos)
    tipobus = ''
    separador = ''
    atributo1 = ''
    atributo2 = ''
    xpath_tit =  ''
    xpath_det = ''
    xpath_link = ''
    xpath_image = ''
    fuenteorg = ''
    urllink = ''
    pais =  ''
    activa = ''
    tipo = ''
    busqueda = ''
    idioma = ''
    codigo = ''

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


st.header(":blue[fuente]")

vtitle = st.text_input("fuente", fuente)
vurl = st.text_input("url ", url)
observa = st.text_input("Observaciones ",  st.session_state['vobserva'])

col = st.columns((6.5, 4.5, 2), gap='medium')


with col[0]:
    tipobus = st.text_input("Tipo de Busqueda", tipobus )
    posjson = st.number_input("Posición del Json",min_value=0,max_value=100,value=vpos)
    separador = st.text_input("Separador", separador)
    atributo1 = st.text_input("Atributo 1", atributo1)
    atributo2 = st.text_input("Atributo 2", atributo2)
    xpath_tit = st.text_input("xpath titulo", xpath_tit)
    xpath_det = st.text_input("xpath detalle", xpath_det)
    xpath_link = st.text_input("xpath link", xpath_link)
    xpath_image = st.text_input("xpath imagen", xpath_image)
with col[1]:
    fuenteorg = st.text_input("Fuente Original", fuenteorg)
    urllink = st.text_input("Url Link", urllink)
    pais =  st.text_input("pais", pais)
    activa = st.text_input("Activa", activa)
    tipo =  st.text_input("Tipo", tipo)
    busqueda = st.text_input("Busequeda Personalizada", busqueda)
    idioma = st.text_input("Idioma", idioma)
    codigo = st.text_input("Código de Pais", codigo)



col10, col20 = st.columns(2)
if col10.button(":red[**Grabar**]"):
    if tipo == 'Editar':
        with conn.session as session:
            actualiza = "UPDATE fuentes_py SET fuente = :url, activa = :activa,"
            actualiza = actualiza + "xpath_titulo = :tit, "
            actualiza = actualiza + "descrip = :desc, "
            actualiza = actualiza + "pais = :pais, "
            actualiza = actualiza + "separador = :separador, "
            actualiza = actualiza + "atributo1 = :atributo1, "
            actualiza = actualiza + "atributo2 = :atributo2, "
            actualiza = actualiza + "xpath_detalle = :det, "
            actualiza = actualiza + "xpath_link = :link, "
            actualiza = actualiza + "xpath_image = :image, "
            actualiza = actualiza + "tipo = :tipo, "
            actualiza = actualiza + "busqueda_pers = :busq, "
            actualiza = actualiza + "idioma = :idioma, "
            actualiza = actualiza + "cod_pais = :cod, "
            actualiza = actualiza + "tipo_busq = :tipo_busq, "
            actualiza = actualiza + "fuente_org = :fuente_org, "
            actualiza = actualiza + "posjson = :posjson, "
            actualiza = actualiza + "urllink = :urllink  "
            actualiza = actualiza + " WHERE nuri= :nuri"        
            session.execute(text(actualiza), {"url": vurl,"activa": activa,"tit": xpath_tit,"desc": vtitle, "pais": pais,"separador": separador,"atributo1": atributo1,"atributo2": atributo2, "det": xpath_det, "link": xpath_link,"image": xpath_image, "tipo": tipo,"busq": busqueda, "idioma": idioma,"cod": codigo,"tipo_busq" : tipobus ,"fuente_org": fuenteorg,"posjson": posjson, "urllink": urllink,  "nuri": tnuri})
                        
            session.commit()
            st.success("Data sent")
    if tipo == 'Ingresar':
        ingresar()
    
    st.switch_page("./pages/fuentes.py")
if col20.button(":red[**Cancelar**]"):
    st.switch_page("./pages/fuentes.py")
