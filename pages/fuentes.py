import streamlit as st
import psycopg2
import os
from sqlalchemy import text



def show_fuentes():
  tnuri = 0
  vtitulo= ''
  vdetalle = ''
  vlink = ''
  vimagen = ''


