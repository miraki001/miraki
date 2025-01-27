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
                    padding-left: 2rem;
                    padding-right: 2rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)



st.subheader("Miraki - Ejes")

def borrar():
    tnuri = st.session_state['vnuri']
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
      actualiza = 'delete from ejestemas where nuri = ' +  tnuri
      session.execute(text(actualiza) )
      session.commit()

selected41 = option_menu(None, ["Ejes", "Ingresar","Editar","Borrar","Volver"], 
      icons=['list-check', 'plus' ,'pencil-square','eraser','house'] , menu_icon="cast",orientation="horizontal", default_index=0,
                
      styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"color": "white", "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
      }
)

st.header(miindex)
st.header(selected41)

if selected41=="Volver":
    st.switch_page("./pages/parametros.py") 
if selected41=="Ingresar":
    st.session_state['vTipo'] = 'Ingresar'
    st.switch_page("./pages/ingejes.py")   
if selected41=="Editar":
    st.session_state['vTipo'] = 'Editar'
    st.switch_page("./pages/ingejes.py") 
if selected41=="Borrar":
    st.session_state['vTipo'] = 'Borrar'
    borrar()



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
qq = 'select e.* ,s.sector from ejestemas e,sectores s where s.nuri = e.sector_nuri ;'
df1 = conn.query(qq, ttl="0"),
df = df1[0]



ppalabra = st.text_input("ingrese el nombre del eje")

if ppalabra:
    mask = df.applymap(lambda x: ppalabra in str(x).lower()).any(axis=1)
    df = df[mask]



colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'eje' : st.column_config.TextColumn('eje', required=True),
    'nuri' : st.column_config.NumberColumn('nuri',),
    'sector_nuri' : st.column_config.NumberColumn('sector_nuri',),
    'sector' : st.column_config.TextColumn('sector',),


    
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
                        'url' : st.column_config.LinkColumn('eje'),      
                        },
                        disabled=df.columns,
                        num_rows=10,
                    )

                    # Filter the dataframe using the temporary column, then drop the column
                    selected_rows = edited_df[edited_df.Selec]
                    return selected_rows.drop('Selec', axis=1)
                  
selection = dataframe_with_selections(df)

cnt = len(selection)
if cnt>0:
    vnuri = selection.to_string(columns=['nuri'], header=False, index=False)
    tnuri = selection.to_string(columns=['nuri'], header=False, index=False)
    veje = selection.to_string(columns=['eje'], header=False, index=False)
    vsec_nuri = selection.to_string(columns=['sector_nuri'], header=False, index=False)
    vcolor = selection.to_string(columns=['color'], header=False, index=False)
    #st.write(vnuri)
    #tnuri = vnuri
