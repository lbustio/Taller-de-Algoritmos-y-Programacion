def calcular_imc(peso, altura):
    try:
        imc = peso / (altura ** 2)
        return imc
    except ZeroDivisionError:
        return None

def categorizar_imc(imc):
    if imc is None:
        return "Altura inválida. No se puede calcular el IMC."
    elif imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def consejos_salud(categoria):
    if categoria == "Bajo peso":
        return "Consume alimentos ricos en nutrientes y aumenta la ingesta de calorías."
    elif categoria == "Peso normal":
        return "Sigue manteniendo un estilo de vida activo y equilibrado."
    elif categoria == "Sobrepeso":
        return "Considera una dieta balanceada y ejercicios regulares para bajar de peso."
    else:
        return "Busca asesoramiento médico para iniciar un plan de pérdida de peso y mejorar tu salud."

try:
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))
        
    imc = calcular_imc(peso, altura)
    categoria = categorizar_imc(imc)
        
    print(f"Tu IMC es: {imc:.2f}")
    print(f"Estás en la categoría de: {categoria}")
    print("Recomendaciones de salud:")
    print(consejos_salud(categoria))
except ValueError:
    print("Por favor, ingresa valores numéricos válidos para peso y altura.")