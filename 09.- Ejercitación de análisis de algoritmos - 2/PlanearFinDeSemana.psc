Proceso PlanearFinDeSemana
	Definir clima Como Cadena
	Escribir 'Ingrese el pron�stico del clima (soleado o lluvioso):'
	Leer clima
	Si clima='soleado' Entonces
		Escribir 'Recomendaci�n: Ir a la zona arqueol�gica.'
		Escribir 'Necesitar� llevar un sombrero.'
	SiNo
		Si clima='lluvioso' Entonces
			Escribir 'Recomendaci�n: Ir a la biblioteca.'
			Escribir 'Necesitar� llevar un paraguas.'
		SiNo
			Escribir 'Clima no reconocido. Intente de nuevo.'
		FinSi
	FinSi
FinProceso
