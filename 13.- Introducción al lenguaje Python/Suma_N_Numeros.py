x = 0
total = 0
n = 0
suma = 0

total = input("Cuántos números se van a sumar:\n")
total = int(total)
for x in range(0, total, 1):
  n = input("Dame un numero:\n")
  suma = suma + int(n)
  
print("La suma de los  ", total, " numeros es: ", suma)