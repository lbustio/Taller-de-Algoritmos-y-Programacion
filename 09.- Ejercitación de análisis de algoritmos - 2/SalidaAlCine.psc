Proceso SalidaAlCine
	Definir pelicula Como Cadena
	Definir cantidad_boletos Como Entero
	Definir precio_boleto Como Real
	Definir total_pagar Como Real
	Escribir 'Bienvenido al cine. Por favor, elija una película:'
	Leer pelicula
	Escribir 'Ingrese la cantidad de boletos a comprar:'
	Leer cantidad_boletos
	// Precio del boleto dependerá de la película y políticas del cine
	// Supongamos precios fijos para diferentes películas
	Si pelicula='A' Entonces
		precio_boleto <- 10
	SiNo
		Si pelicula='B' Entonces
			precio_boleto <- 12
		SiNo
			Si pelicula='C' Entonces
				precio_boleto <- 8
			SiNo
				Escribir 'Lo siento, película no reconocida. Intente de nuevo.'
			FinSi
		FinSi
	FinSi
	total_pagar <- cantidad_boletos*precio_boleto
	Escribir 'Ha elegido la película ', pelicula, ' y comprará ', cantidad_boletos, ' boleto(s).'
	Escribir 'Total a pagar: ', total_pagar, 'pesos. ¡Disfrute su película!'
FinProceso
