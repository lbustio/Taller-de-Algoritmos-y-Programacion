Proceso CalcularPuntajeTorneo
	Definir ganados, perdidos, empatados, puntaje_total Como Entero
	Escribir 'Ingrese el número de partidos ganados:'
	Leer ganados
	Escribir 'Ingrese el número de partidos perdidos:'
	Leer perdidos
	Escribir 'Ingrese el número de partidos empatados:'
	Leer empatados
	puntaje_total <- (ganados*3)+(empatados*1)+(perdidos*0)
	Escribir 'El puntaje total del ABC club en el torneo es:', puntaje_total
FinProceso
