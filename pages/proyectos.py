import streamlit as st
import psycopg2
from sqlalchemy import text
from streamlit_option_menu import option_menu

st.set_page_config(initial_sidebar_state="collapsed",
                  layout="wide",menu_items=None ,page_title="Miraki")


selected6 = option_menu(None, ["Home", 'Ingresar','Editar','Borrar'], 
      icons=['house', 'plus' ,'pencil-square','eraser'] , menu_icon="cast",orientation="horizontal", default_index=-2,
                
      styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white", "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
      }
)
st.subheader("Proyectos")

if selected6=="Home":
    st.switch_page("./pages/parametros.py") 
if selected6=="Ingresar":
    st.session_state['vTipo'] = 'Ingresar'
    st.switch_page("./pages/ingproyectos.py")   
if selected6=="Editar":
    st.session_state['vTipo'] = 'Editar'
    st.switch_page("./pages/ingproyectos.py") 


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
qq = 'select nuri,proyecto from proyectos  ;'
df1 = conn.query(qq, ttl="0"),
df = df1[0]




ppalabra = st.text_input("ingrese el nombre del proyecto")


if ppalabra:
    mask = df.applymap(lambda x: ppalabra in str(x).lower()).any(axis=1)
    df = df[mask]


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'proyecto' : st.column_config.TextColumn('proyecto', required=True),
    'nuri' : st.column_config.NumberColumn('nuri',),



    
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
    st.session_state['vpro'] = selection.to_string(columns=['proyecto'], header=False, index=False)
    
