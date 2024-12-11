Proceso PlanearFinDeSemana
	Definir clima Como Cadena
	Escribir 'Ingrese el pronóstico del clima (soleado o lluvioso):'
	Leer clima
	Si clima='soleado' Entonces
		Escribir 'Recomendación: Ir a la zona arqueológica.'
		Escribir 'Necesitará llevar un sombrero.'
	SiNo
		Si clima='lluvioso' Entonces
			Escribir 'Recomendación: Ir a la biblioteca.'
			Escribir 'Necesitará llevar un paraguas.'
		SiNo
			Escribir 'Clima no reconocido. Intente de nuevo.'
		FinSi
	FinSi
FinProceso
