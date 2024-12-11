Proceso Decimal2Hexadecimal
	Definir numero_decimal, residuo Como Entero
	Definir numero_hexadecimal Como Cadena
	Definir hexa Como Cadena
	numero_hexadecimal <- ''
	hexa <- ''
	Escribir 'Ingrese un número decimal:'
	Leer numero_decimal // Inicializar la cadena para almacenar el número hexadecimal
	Mientras numero_decimal>0 Hacer
		residuo <- numero_decimal MOD 16
		// Convertir residuo a su representación en hexadecimal
		Si residuo<10 Entonces
			numero_hexadecimal <- Concatenar(numero_hexadecimal,ConvertirATexto(residuo))
		SiNo
			Según residuo Hacer
				10:
					numero_hexadecimal <- Concatenar(numero_hexadecimal,'A')
				11:
					numero_hexadecimal <- Concatenar(numero_hexadecimal,'B')
				12:
					numero_hexadecimal <- Concatenar(numero_hexadecimal,'C')
				13:
					numero_hexadecimal <- Concatenar(numero_hexadecimal,'D')
				14:
					numero_hexadecimal <- Concatenar(numero_hexadecimal,'E')
				15:
					numero_hexadecimal <- Concatenar(numero_hexadecimal,'F')
			FinSegún
		FinSi
		numero_decimal <- trunc(numero_decimal/16)
	FinMientras
	Dimensionar vec(Longitud(numero_hexadecimal))
	Para i<-0 Hasta Longitud(numero_hexadecimal)-1 Con Paso 1 Hacer
		vec[i] <- Subcadena(numero_hexadecimal,i,i)
	FinPara
	Para i<-Longitud(numero_hexadecimal)-1 Hasta 0 Con Paso -1 Hacer
		hexa <- Concatenar(hexa,vec[i])
	FinPara
	Escribir 'El número en sistema hexadecimal es:', hexa
FinProceso
