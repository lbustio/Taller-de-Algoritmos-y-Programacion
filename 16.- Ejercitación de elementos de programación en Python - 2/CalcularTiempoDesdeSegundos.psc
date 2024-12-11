Proceso CalcularTiempoDesdeSegundos
	Definir segundos Como Entero
	Definir segundos_restantes Como Entero
	Definir dias Como Entero
	Definir horas Como Entero
	Definir minutos Como Entero
	Escribir 'Ingrese la cantidad de segundos:'
	Leer segundos
	dias <- Trunc(segundos/(24*3600))
	segundos_restantes <- segundos MOD (24*3600)
	horas <- Trunc(segundos_restantes/3600)
	segundos_restantes <- segundos_restantes MOD 3600
	minutos <- Trunc(segundos_restantes/60)
	segundos_restantes <- segundos_restantes MOD 60
	segundos <- segundos_restantes
	Escribir 'Equivalente a: ', dias, ' dias, ', horas, ' horas, ', minutos, ' minutos y ', segundos, ' segundos.'
FinProceso
