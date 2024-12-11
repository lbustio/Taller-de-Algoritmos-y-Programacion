def celsius2fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = celsius2fahrenheit(temperatura_celsius)
print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit}")