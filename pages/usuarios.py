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

st.subheader("Usuarios")

def borrar():
  conn = st.connection("postgresql", type="sql")
  tusuario = st.session_state['vusuario']
  with conn.session as session:
    actualiza = 'delete from usuarios   where usuario = :usuario ;'
    session.execute(text(actualiza), {"usuario": tusuario})
    #session.execute(text(actualiza) )
    session.commit()
  #st.info("la palabra ha sido borrada") 
  message = st.chat_message("assistant")
  message.write("el usuario ha sido borrado")
  ppalabra = ''
  st.switch_page("./pages/parametros.py")

selected7 = option_menu(None, ["Usuarios", 'Ingresar','Editar','Borrar','Volver'], 
      icons=['people-fill', 'plus' ,'pencil-square','eraser','house'] , menu_icon="cast",orientation="horizontal", default_index=0,
                
      styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white", "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
      }
)

if selected7=="Volver":
    st.switch_page("./pages/parametros.py") 
if selected7=="Ingresar":
    st.session_state['vTipo'] = 'Ingresar'
    st.switch_page("./pages/ingusuarios.py")   
if selected7=="Editar":
    st.session_state['vTipo'] = 'Editar'
    st.switch_page("./pages/ingusuarios.py") 
if selected7=="Borrar":
    st.session_state['vTipo'] = 'Borrar'
    borrar()

tnuri = 0
vtitulo= ''
vdetalle = ''
vlink = ''
vimagen = ''



st.markdown("""
            <style>
            div.stButton {text-align:center}
            div.stButton > button:first-child {
                background-color: #b579c2;
                color:#000000;
                font-weight: bold;
            }
            div.stButton > button:hover {
                background-color: #79adc2;
                color:#ff0000;
                }
            </style>""", unsafe_allow_html=True)






conn = st.connection("postgresql", type="sql")
qq = 'select u.usuario,u.clave,u.administrador,u.proyecto_nuri,p.proyecto from usuarios u, proyectos p where p.nuri = u.proyecto_nuri ;'
df1 = conn.query(qq, ttl="0"),
df = df1[0]



ppalabra = st.text_input("ingrese el nombre del usuario")

if ppalabra:
    mask = df.applymap(lambda x: ppalabra in str(x).lower()).any(axis=1)
    df = df[mask]



colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'usuario' : st.column_config.TextColumn('usuario', required=True),
    'clave' : st.column_config.TextColumn('clave',disable = True),
    'administrador' : st.column_config.TextColumn('adminstrador',),
    'proyecto_nuri' : st.column_config.NumberColumn('proyecto_nuri',),


    
}
#result = st.data_editor(df, column_config = config, num_rows='dynamic')
def dataframe_with_selections(df):
                    df_with_selections = df.copy()
                    df_with_selections.insert(0, "Selec", False)
                    # Get dataframe row-selections from user with st.data_editor
                    edited_df = st.data_editor(
                        df_with_selections,
                        hide_index=True,
                        column_config=
                        {"Select": st.column_config.CheckboxColumn(required=True),
                        'url' : st.column_config.LinkColumn('usuario'),      
                        },
                        disabled=df.columns,
#                        num_rows="dynamic",
                    )

                    # Filter the dataframe using the temporary column, then drop the column
                    selected_rows = edited_df[edited_df.Selec]
                    return selected_rows.drop('Selec', axis=1)
                  
selection = dataframe_with_selections(df)

cnt = len(selection)
if cnt > 0:
            vusuario = selection.to_string(columns=['usuario'], header=False, index=False)
            vclave = selection.to_string(columns=['clave'], header=False, index=False)
            st.write(vusuario)
            st.session_state['vusuario'] = selection.to_string(columns=['usuario'], header=False, index=False)
            st.session_state['vclave'] =  selection.to_string(columns=['clave'], header=False, index=False)
            st.session_state['vadmin'] =  selection.to_string(columns=['administrador'], header=False, index=False)
            st.session_state['vproyecto'] =  selection.to_string(columns=['proyecto'], header=False, index=False)
