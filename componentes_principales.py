import pandas  as pd

class IngestorDatos:
    def __init__(self):
        pass
    
    def cargar_datos(self, archivo) -> pd.DataFrame:
        '''Carga un archivo y valida que con la interfaz requerida'''
        
        #El bloque try, se usa junto con expcept para manerjar errores
        #y excepciones de forma controlada, evitando que el codigo
        #se rompa abruptamente al suceder un error,definiendo
        #acciones alternativas.
        try:
            df = pd.read_csv(archivo, sep=None, engine='python', encoding='utf-8-sig')
            #usamos sep=None y el motor de python para que pandas detecte automaticamente 
            #si el archivo usa comas (,) puntos y comas(;) o tabuladores ()
            
            #Validamos el contrato de la interfaz(Columnas requeridas)
            columnas_requeridas = {'fecha', 'producto', 'cantidad', 'precio_unitario'}
            
            if not columnas_requeridas.issubset(df.columns):
                raise ValueError(f"El archivo no cumple con el contrato. Columnas requeridas:{columnas_requeridas}")
            
            #Limpieza y conversion de tipos de datosç
            df['fecha'] = pd.to_datetime(df['fecha'])
            df['total_venta'] = df['cantidad'] * df['precio_unitario']
            return df
        except Exception as e:
            raise IOError(f"Error al procesar el componene de datos: {e}")