import pandas as pd

# Crear un DataFrame de ejemplo
data = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
        'Edad': [25, 30, 35, 40],
        'Puntaje': [85, 90, 95, 80]}
df = pd.DataFrame(data)

# Nombre de la columna para calcular el promedio
columna = 'Puntaje'

# Calcular el promedio de la columna dada
promedio = df[columna].mean()

print("DataFrame:")
print(df)
print("Promedio de la columna '{}': {:.2f}".format(columna, promedio))