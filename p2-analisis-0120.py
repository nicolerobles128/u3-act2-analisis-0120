# Importar librerías
import pandas as pd
import numpy as np

print("Analisis de datos transacciones Nicole Robles NC=0120")
transacciones = {"Id_Transaccion": ["T001", "T002", "T003", "T004", "T005", "T006"],
    "Monto": [15.50, 2500.00, 45.00, 890.00, 12.00, 3400.00],
    "Ubicacion_Inusual": [False, True, False, True, False, True],
    "Es_Fraude": [False, True, False, False, False, True]}

df = pd.DataFrame(transacciones)
print(df)

print("+-+-+-+-+-+ Agrupar por una sola columna +-+-+-+-+-+")
agrupado = df.groupby('Monto')
print(agrupado)

print("+-+-+-+-+-+ Por agregacion +-+-+-+-+-+")

# Ubicación Inusual promedio por Monto
# Se evalúa la columna 'Monto' o se calcula la media de los montos
print(agrupado['Monto'].mean())

print("+-+-+-+-+-+ Fraude Maximo +-+-+-+-+-+")

# Fraude máximo en cada Monto
print(agrupado['Es_Fraude'].max())