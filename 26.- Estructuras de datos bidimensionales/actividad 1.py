import numpy as np

# Array original
array = np.array([1, 4, 0, 2, 7, 9, 0, 3, 0, 0, 8, 0, 5, 6])

# Encontrar los índices de los elementos igual a cero
indices_cero = np.where(array == 0)[0]

print("Array original:", array)
print("Índices de los elementos igual a cero:", indices_cero)