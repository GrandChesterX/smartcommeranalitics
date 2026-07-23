# Este modulo permite ensamblar el resto de componentes en la UI
import streamlit as st
import pandas as pd

# Importar los componentes que van a ser reutilizables como si fueras librerias locales
from componente_datos import IngestorDatos
from componente_prediccion import MotorPrediccion

#Configuramos la página de nuestra app web
st.set_page_config(page_title="Consola de Componentes Comerciales", layout="wide")
st.title(" 📦Ensamblador de componentes: Inteligencia de Negocio ")

#Instanciamos los componentes de forma local
ingestor = IngestorDatos()
predictor = MotorPrediccion(incremento_simulado=0.20)

#Inicializar el estado de la sesión (Session State)
if 'datos_negocio' not in st.session_state:
    st.session_state.datos_negocio = pd.DataFrame()
    
# RENDERIZADO VISUAL
archivo_cargado = st.file_uploader("Cargar archivo de ventas (CSV)", type="csv") 

if archivo_cargado:
    try:
        #Usamos el componente de datos para cargar el archivo en el estado de la memoria
        st.session_state.datos_negocio = ingestor.cargar_datos(archivo_cargado)
        st.success(f"Componente de Datos: Ingesta y Validacion exitosas")
    except Exception as e:
        st.error(f"Fallo de interfaz de datos: {e}")
        
#Si hay datos en la sesión, los componentes visuales e interactivos se activan
if not st.session_state.datos_negocio.empty:
    col_tabla, col_prediccion = st.columns(2)
    
    with col_tabla:
        st.subheader("🗒️ Registro de Ventas")
        st.dataframe(st.session_state.datos_negocio, width="stretch")
        
    with col_prediccion:
        st.subheader("Prediccion de Stock Requerido")
        #Pasamos los datos limpios de un componente al otro de forma directa
        df_prediccion = predictor.predecir_demanda(st.session_state.datos_negocio)
        st.dataframe(df_prediccion, width="stretch")        