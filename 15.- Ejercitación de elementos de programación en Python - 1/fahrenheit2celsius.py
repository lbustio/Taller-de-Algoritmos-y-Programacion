def fahrenheit2celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temperatura_fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
temperatura_celsius = fahrenheit2celsius(temperatura_fahrenheit)
print(f"La temperatura en grados Celsius es: {temperatura_celsius}")