import math

pi = math.pi

radio = float(input("Ingrese el radio de la circunferencia: "))

area = pi * radio ** 2
perimetro = 2 * pi * radio

print(f"El área de la circunferencia es: {area}")
print(f"El perímetro de la circunferencia es: {perimetro}")
