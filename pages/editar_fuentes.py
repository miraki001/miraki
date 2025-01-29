import streamlit as st
import psycopg2
from sqlalchemy import text
from streamlit_option_menu import option_menu

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
                    padding-left: 4rem;
                    padding-right: 2rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

st.logo(
    "https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/android-chrome-192x192.png?alt=media&token=e8d5f6ee-706a-4399-813d-fd82f8b35ec7",
    icon_image="https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/android-chrome-192x192.png?alt=media&token=e8d5f6ee-706a-4399-813d-fd82f8b35ec7",
)
#vnuri = st.session_state['vnuri']
#st.session_state.vnuri = 0
st.subheader("Miraki - Fuentes")

selected2 = option_menu(None, ["Miraki", 'Novedades','Fuentes', 'Informes','Parametros','Github' ], 
        icons=['house', 'newspaper' , 'filetype-html','globe-americas','gear','github'] , menu_icon="cast",orientation="horizontal", default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white",  "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
        }
  )

if selected2=="Fuentes":
  st.switch_page("./pages/fuentes.py")
if selected2=="Novedades":
  st.switch_page("./pages/novedades.py")       
if selected2=="Parametros":
  st.switch_page("./pages/parametros.py")        
if selected2=="Informes":
  st.switch_page("./pages/informes.py")    


conn = st.connection("postgresql", type="sql")



def ingresar():
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
        actualiza = "insert into fuentes_py (nuri, fuente,, activa, xpath_titulo, descrip, proyecto_nuri,pais,separador,atributo1,atributo2,xpath_detalle,xpath_link,xpath_image,tipo,busqueda_pers,idioma,cod_pais,tipo_busq,fuente_org,posjson,urllink )"
        actualiza = actualiza + " values (nextval('fuente_py_seq'),:fuente, :activa, :xpath_titulo , :descrip, 1,:pais,:separador,:atributo1,:atributo2,:xpath_detalle,:xpath_link,:xpath_image,:tipo,busqueda_pers,:idioma,:cod_pais,:tipo_busq,:fuente_org,:posjson,:urllink  );"
        session.execute(text(actualiza), {"fuente": vurl,"activa": activa,"tit": xpath_tit,"desc": vtitle, "pais": pais,"separador": separador,"atributo1": atributo1,"atributo2": atributo2, "det": xpath_det, "link": xpath_link,"image": xpath_image, "tipo": tipo,"busq": busqueda, "idioma": idioma,"cod": codigo,"tipo_busq" : tipobus ,"fuente_org": fuenteorg,"posjson": posjson, "urllink": urllink})
        
        session.commit()    
def borrar():
    tnuri = st.session_state['vnuri']
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
      actualiza = 'delete from fuentes_py where nuri = ' +  tnuri
      session.execute(text(actualiza) )
      session.commit()
def actualizar():
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
      actualiza = 'delete from fuentes_py where nuri = ' +  tnuri
      session.execute(text(actualiza) )
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
    observa = st.session_state['vobserva']

if tipo == 'Ingresar':
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
    observa = ''

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


#st.header(":blue[fuente]")

col = st.columns((6.0, 5.0, 4.0,2), gap='medium')


with col[0]:
    vtitle = st.text_input("fuente", fuente)
    vurl = st.text_input("url ", url)
    observa = st.text_input("Observaciones ",  observa)
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
with col[2]:
    xpath_tit = st.text_input("xpath titulo", xpath_tit)
    xpath_det = st.text_input("xpath detalle", xpath_det)
    xpath_link = st.text_input("xpath link", xpath_link)
    xpath_image = st.text_input("xpath imagen", xpath_image)
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

