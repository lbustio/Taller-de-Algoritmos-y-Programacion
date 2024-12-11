Proceso CalcularMedia
	Definir numero Como Real
	Definir suma Como Real
	Definir media Como Real
	Definir contador Como Entero
	Repetir
		Escribir 'Ingrese el número ', contador, ':'
		Leer numero
		suma <- suma+numero
		contador <- contador+1
	Hasta Que contador=50
	media <- suma/50
	Escribir 'La media de los 50 números es:', media
FinProceso
