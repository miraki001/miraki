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

st.subheader("Miraki ")

st.logo(
    "https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/android-chrome-192x192.png?alt=media&token=e8d5f6ee-706a-4399-813d-fd82f8b35ec7",
    icon_image="https://firebasestorage.googleapis.com/v0/b/miraki-7ca50.appspot.com/o/android-chrome-192x192.png?alt=media&token=e8d5f6ee-706a-4399-813d-fd82f8b35ec7",
)

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
    
if selected2=="Github":
   st.write("check out this [link](https://github.com/miraki001/miraki/edit/main/pages/home.py)")  



#st.header("Miraki")

st.write(
    """
        
        
        Plataforma de Vigilancia Tecnologica e Inteligencia Competitiva.
        
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
#st.write(wordcloud)   
fig, plt = plt.subplots(figsize = (8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
#fig = plt.figure(figsize=(8,8))
plt.axis("off")
#plt.show()
st.pyplot(fig)

