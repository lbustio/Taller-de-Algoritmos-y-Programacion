Proceso Fibonacci
	Definir n, i, a, b, c Como Entero
	Escribir 'Ingrese la cantidad de números de la serie de Fibonacci a calcular:'
	Leer n
	a <- 0
	b <- 1 // Primer número de la serie
	Si n>=1 Entonces // Segundo número de la serie
		Escribir 'Los primeros ', n, ' números de la serie de Fibonacci son:'
		Escribir a
		Si n>=2 Entonces // Mostrar el primer número de la serie
			Escribir b
			Para i<-3 Hasta n Con Paso 1 Hacer // Mostrar el segundo número de la serie
				c <- a+b
				Escribir c
				a <- b // Mostrar el siguiente número de la serie
				b <- c
			FinPara
		FinSi
	FinSi
FinProceso
