#Componente aislado que reliza los cálculos de la estimación del inventario futuro
import pandas as pd
import numpy as np

#Crear la clase principal del motor de predicción
class MotorPrediccion:
    """Componente analítico para estimar la demanda futura del inventario"""
    def __init__(self,incremento_simulado=0.15):
        self.incremento = incremento_simulado
        
    def predecir_demanda(self, df_historico:pd.DataFrame) -> pd.DataFrame:
        """
        Toma datos historicos y estima el stock necesario para el proximo mes
        Logioca de componente aislada de la UI
        """
        if df_historico.empty:
            return pd.DataFrame()
        
        #Agrupamos por producto para ver el promedio de ventas mensuales
        ventas_promedio = df_historico.groupby('producto')['cantidad'].mean().reset_index()
        
        # aplicamos la fórmula matematica de stock segurido(Demanda + Margen de Seguridad)
        ventas_promedio['stock.sugerido'] = np.ceil(ventas_promedio['cantidad']*(1+self.incremento)).astype(int)
        ventas_promedio.rename(columns={'cantidad':'promedio_historico'}, inplace=True)
        return round(ventas_promedio, 2)