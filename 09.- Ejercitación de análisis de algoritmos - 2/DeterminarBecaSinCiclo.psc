Proceso DeterminarBecaSinCiclo
	Definir calificacion1, calificacion2, calificacion3, calificacion4, calificacion5 Como Real
	Definir promedio Como Real
	Escribir 'Ingrese la calificación de la materia 1:'
	Leer calificacion1
	Escribir 'Ingrese la calificación de la materia 2:'
	Leer calificacion2
	Escribir 'Ingrese la calificación de la materia 3:'
	Leer calificacion3
	Escribir 'Ingrese la calificación de la materia 4:'
	Leer calificacion4
	Escribir 'Ingrese la calificación de la materia 5:'
	Leer calificacion5
	promedio <- (calificacion1+calificacion2+calificacion3+calificacion4+calificacion5)/5
	Si promedio>=8.5 Entonces
		Escribir '¡Puede solicitar la beca!'
	SiNo
		Escribir 'Lo siento, no cumple con el promedio requerido para la beca.'
	FinSi
FinProceso
