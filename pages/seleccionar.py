import streamlit as st
import psycopg2
from sqlalchemy import text

tnuri = st.session_state['vnuri']
st.write(tnuri)
conn = st.connection("postgresql", type="sql")

actualizar = 'update novedades set select_web = :estado,nro_reporte = 0 where nuri = ' + tnuri + ';'
nuri = tnuri
new = 'S'
st.write(actualizar)


with conn.session as session:
    #session.execute(f"UPDATE novedades SET select_web = '{new}' WHERE nuri='{nuri}'")
    session.execute(text("UPDATE novedades SET select_web = :val, nro_reporte = 0 WHERE nuri= :nuri"), {"val": new,"nuri": nuri})
                        
    session.commit()
    st.success("Data sent")

st.switch_page("streamlit_app.py")


#df1 = conn.execute(actualizar, ttl="0",params={"estado": "S"} ),
