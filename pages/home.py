import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import nltk
import wordcloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem.porter import * 
from gensim.models import word2vec 
from sklearn.manifold import TSNE 
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()  

st.set_page_config(layout="wide",page_title="Miraki")

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


st.markdown("""
<style>
:root {
  --header-height: 40px;
  --header-height-padded: 40px;
}

[data-testid="stHeader"] {
    background-image: url(ic_launcher44.png);
    background-repeat: no-repeat;
    background-size: 20px;
    background-orgin: content-box;
    background-color: grey;
    padding-top: var(--header-height);
}


}
</style>
""", unsafe_allow_html=True)




selected2 = option_menu(None, ["Miraki", 'Novedades','Fuentes', 'Informes','Parametros','Github' ], 
        icons=['house', 'newspaper' , 'filetype-html','globe-americas','gear','github'] , menu_icon="cast",orientation="horizontal", default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "#604283"},
        "icon": {"color": "red", "font-size": "14px"}, 
        "nav-link": {"color": "white",  "font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#B3D3F0"},
        "nav-link-selected": {"background-color": "#604283"}
        }
  )

if selected2=="Fuentes":
  st.switch_page("./pages/fuentes.py")
if selected2=="Parametros":
  st.switch_page("./pages/parametros.py")
        
st.header("Miraki")

st.write(
    """
        
        
        Plataforma de Vigilancia Tecnologica e Inteligencia Competitiva.
        
        ornare. Morbi id ex pulvinar dui placerat congue. Suspendisse ultricies, lacus
        eget porttitor blandit, enim nisi tincidunt eros, nec varius tortor turpis et
        tortor.

        Curabitur facilisis, augue eu eleifend dictum, quam lectus ullamcorper tellus,
        auctor mollis lacus turpis id tellus. Mauris consectetur eleifend dignissim.
        Integer nulla arcu, fringilla quis finibus vel, iaculis ac massa. Cras at
        mauris a magna blandit mattis. Nam vel turpis et risus tempus congue ac quis
        lectus. Pellentesque id laoreet ex, sit amet consequat leo. Aenean commodo
        luctus tristique. Curabitur arcu urna, tempus ut lectus et, pulvinar lobortis
        urna.
    """
)

conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,select_web selec,fecha,titulo,detalle,imagen,link from novedades order by nuri desc limit 2000;', ttl="0"),
df = df1[0]
#st.write(df1[0])


df = df[pd.notnull(df['titulo'])]

nltk.download('stopwords')
stop_words = stopwords.words('english')
stopword_es = nltk.corpus.stopwords.words('spanish')
stop_words = stop_words + stopword_es

def cleaning(df, stop_words):
    df['titulo'] = df['titulo'].apply(lambda x:' '.join(x.lower() for x in x.split()))
    # Replacing the digits/numbers
    df['titulo'] = df['titulo'].str.replace('^\d+\s|\s\d+\s|\s\d+$', '')
    # Removing stop words
    df['titulo'] = df['titulo'].apply(lambda x:' '.join(x for x in x.split() if x not in stop_words))
    # Lemmatization
#    df['titulo'] = df['titulo'].apply(lambda x:' '.join([Word(x).lemmatize() for x in x.split()]))
    return df

data_v1 = cleaning(df, stop_words)
data_v1.head()


# Create and generate a word cloud image:
#wordcloud = WordCloud().generate(text)

common_words=''
for i in data_v1.titulo:  
    i = str(i)
    tokens = i.split()
    common_words += " ".join(tokens)+" "
wordcloud = wordcloud.WordCloud().generate(common_words)
plt.imshow(wordcloud, interpolation='bilinear')
#fig = plt.figure(figsize=(8,8))
plt.axis("off")
plt.show()
#st.pyplot()

