import streamlit as st
import psycopg2
from sqlalchemy import text
#from streamlit_extras.stylable_container import stylable_container
from streamlit_option_menu import option_menu

def borrar():
    tnuri = st.session_state['vnuri']
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
      actualiza = 'delete from sectores where nuri = ' +  tnuri
      session.execute(text(actualiza) )
      session.commit()
    st.info("el sector ha sido borrado") 



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
st.subheader("Miraki - Sectores")


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

selected5 = option_menu(None, ["Sectores", 'Ingresar','Editar','Borrar','Volver' ], 
      icons=['diagram-3', 'plus' ,'pencil-square','eraser','house'] , menu_icon="cast",orientation="horizontal", default_index=0,
                
      styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white", "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
      }
)


if selected5=="Volver":
    st.switch_page("./pages/parametros.py") 
if selected5=="Ingresar":
    st.session_state['vTipo'] = 'Ingresar'
    st.switch_page("./pages/ingsectores.py")   
if selected5=="Editar":
    st.session_state['vTipo'] = 'Editar'
    st.switch_page("./pages/ingsectores.py") 
if selected5=="Borrar":
    st.session_state['vTipo'] = 'Borrar'
    borrar()





conn = st.connection("postgresql", type="sql")
qq = 'select s.nuri,s.sector,s.color,p.proyecto from sectores s,proyectos p where p.nuri = s.proyecto_nuri  ;'
df1 = conn.query(qq, ttl="0"),
df = df1[0]



ppalabra = st.text_input("ingrese el nombre del sector")

if ppalabra:
    mask = df.applymap(lambda x: ppalabra in str(x).lower()).any(axis=1)
    df = df[mask]



colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'sector' : st.column_config.TextColumn('sector', required=True),
    'nuri' : st.column_config.NumberColumn('nuri',),
    'proyecto_nuri' : st.column_config.NumberColumn('proyecto_nuri',),
    'color' : st.column_config.TextColumn('color',),


    
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
                        'url' : st.column_config.LinkColumn('sector'),      
                        },
                        disabled=df.columns,
#                        num_rows="dynamic",
                    )

                    # Filter the dataframe using the temporary column, then drop the column
                    selected_rows = edited_df[edited_df.Selec]
                    return selected_rows.drop('Selec', axis=1)
                  
selection = dataframe_with_selections(df)

cnt = len(selection)

if cnt>0:
    vnuri = selection.to_string(columns=['nuri'], header=False, index=False)
    st.write(vnuri)
    tnuri = vnuri
    st.session_state['vnuri'] = tnuri
    st.session_state['vpro_nuri'] = selection.to_string(columns=['proyecto_nuri'], header=False, index=False)
    st.session_state['vsector'] = selection.to_string(columns=['sector'], header=False, index=False)
    st.session_state['vcolor'] = selection.to_string(columns=['color'], header=False, index=False)
    st.session_state['vpro'] = selection.to_string(columns=['proyecto'], header=False, index=False)
