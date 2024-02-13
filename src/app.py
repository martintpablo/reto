import streamlit as st
import pandas as pd
from pinecone import Pinecone
# from io import StringIO


# Define tus credenciales de API de Pinecone
api_key = "ecd9d0da-316a-46c5-ad95-919541600f79"  
pinecone_index_name = "reto"  # Reemplaza "NOMBRE_DE_TU_ÍNDICE" con el nombre de tu índice en Pinecone

# Inicializa el cliente de Pinecone
pinecone = Pinecone(api_key=api_key)

# Verifica la conexión con Pinecone intentando listar los índices
try:
    pinecone.list_indexes()
    st.success("Conexión exitosa con Pinecone.")
except Exception as e:
    st.error(f"Error al conectar con Pinecone: {e}")


st.title('Reto - Chatbot - Grupo 1')

col1, col2 = st.columns(2)

with col1:
    # st.write('Dime tu pregunta sobre el archivo')
    pregunta = txt = st.text_area("Text to analyze", placeholder='Introduzca su pregunta aquí')

with col2:
    archivo_subido = st.file_uploader("Suba su archivo a utilizar")
    # if archivo_subido is not None:
    #     # To read file as bytes:
    #     # bytes_data = archivo_subido.getvalue()
    #     # st.write(bytes_data)

    #     # To convert to a string based IO:
    #     stringio = StringIO(archivo_subido.getvalue().decode("utf-8"))
    #     st.write(stringio)

    #     # To read file as string:
    #     string_data = stringio.read()

if st.button('Realizar pregunta'):
    if archivo_subido is not None:
        st.write('Funciona todo, tanto el botón como el subir archivos')
        
    else:
        st.write('Funciona el botón')