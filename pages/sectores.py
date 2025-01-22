import streamlit as st
import psycopg2
from sqlalchemy import text
#from streamlit_extras.stylable_container import stylable_container
from streamlit_option_menu import option_menu


st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None)


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

selected5 = option_menu(None, ["Home", 'Ingresar','Editar','Borrar' ], 
      icons=['house', 'gear' ,'gear','eraser'] , menu_icon="cast",orientation="horizontal", default_index=-1,
                
      styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white", "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
      }
)
st.header("Sectores")

if selected5=="Home":
    st.switch_page("./pages/parametros.py") 
if selected5=="Ingresar":
    st.session_state['vTipo'] = 'Ingresar'
    st.switch_page("./pages/ingsectores.py")   
if selected5=="Editar":
    st.session_state['vTipo'] = 'Editar'
    st.switch_page("./pages/ingsectores.py") 
if selected5=="Editar":
    st.session_state['vTipo'] = 'Editar'
    st.switch_page("./pages/borrarsectores.py") 





conn = st.connection("postgresql", type="sql")
qq = 'select proyecto_nuri,nuri,sector,color from sectores  ;'
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
