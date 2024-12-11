Proceso CalcularPuntaje
	Definir correctas, incorrectas, blanco, puntaje_final Como Entero
	Escribir 'Ingrese el número de respuestas correctas:'
	Leer correctas
	Escribir 'Ingrese el número de respuestas incorrectas:'
	Leer incorrectas
	Escribir 'Ingrese el número de respuestas en blanco:'
	Leer blanco
	puntaje_final <- (correctas*3)+(incorrectas*(-1))
	Escribir 'El puntaje final del postulante es:', puntaje_final
FinProceso
