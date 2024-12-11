Proceso VerificarNumeroPrimo
	Definir numero Como Entero;
	Definir divisores Como Entero;
	Definir i Como Entero;
	Escribir 'Ingrese un número (mayor que 1) para verificar si es primo:';
	Leer numero;
	divisores <- 0;
	Si numero<=1 Entonces
		Escribir 'El número debe ser mayor que 1.';
	SiNo
		Para i<-1 Hasta numero Con Paso 1 Hacer
			Si numero MOD i==0 Entonces
				divisores <- divisores+1;
			FinSi
		FinPara
		Si divisores==2 Entonces
			Escribir numero, ' es un número primo.';
		SiNo
			Escribir numero, ' no es un número primo.';
		FinSi
	FinSi
FinProceso
