Proceso VerificarNumeroPrimo
	Definir numero Como Entero;
	Definir divisores Como Entero;
	Definir i Como Entero;
	Escribir 'Ingrese un n�mero (mayor que 1) para verificar si es primo:';
	Leer numero;
	divisores <- 0;
	Si numero<=1 Entonces
		Escribir 'El n�mero debe ser mayor que 1.';
	SiNo
		Para i<-1 Hasta numero Con Paso 1 Hacer
			Si numero MOD i==0 Entonces
				divisores <- divisores+1;
			FinSi
		FinPara
		Si divisores==2 Entonces
			Escribir numero, ' es un n�mero primo.';
		SiNo
			Escribir numero, ' no es un n�mero primo.';
		FinSi
	FinSi
FinProceso
