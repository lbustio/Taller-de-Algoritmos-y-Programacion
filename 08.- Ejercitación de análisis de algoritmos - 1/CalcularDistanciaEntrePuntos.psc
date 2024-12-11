Proceso CalcularDistanciaEntrePuntos
	Definir xA, yA, xB, yB, distancia Como Real
	Escribir 'Ingrese la coordenada x del punto A:'
	Leer xA
	Escribir 'Ingrese la coordenada y del punto A:'
	Leer yA
	Escribir 'Ingrese la coordenada x del punto B:'
	Leer xB
	Escribir 'Ingrese la coordenada y del punto B:'
	Leer yB
	distancia <- ((xB-xA)^2+(yB-yA)^2)^(0.5)
	Escribir 'La distancia entre los puntos A y B es:', distancia
FinProceso
