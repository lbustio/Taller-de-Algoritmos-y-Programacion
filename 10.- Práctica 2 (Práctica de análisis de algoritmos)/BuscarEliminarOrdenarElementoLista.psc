Proceso BuscarEliminarOrdenarElementoLista
	Definir longitud_lista Como Entero
	Definir elemento Como Entero
	Definir encontrado Como Lógico
	Definir temp Como Entero
	Dimensionar lista(10)
	// Inicialización de la lista con valores
	lista[1] <- 5 // Definir un arreglo para simular una lista con un máximo de 10 elementos
	lista[2] <- 2
	lista[3] <- 9
	lista[4] <- 1
	lista[5] <- 7
	lista[6] <- 3
	longitud_lista <- 6
	Escribir 'Ingrese el elemento a buscar y eliminar de la lista:' // Longitud actual de la lista
	Leer elemento
	encontrado <- Falso
	// Búsqueda y eliminación del elemento de la lista
	Para i<-1 Hasta longitud_lista Con Paso 1 Hacer // Inicializar la bandera de encontrado como falso
		Si lista[i]==elemento Entonces
			// Si se encuentra el elemento, se procede a eliminarlo
			Para j<-i Hasta longitud_lista-1 Con Paso 1 Hacer
				lista[j] <- lista[j+1]
			FinPara // Desplazar elementos para llenar el espacio vacío
			longitud_lista <- longitud_lista-1
			encontrado <- Verdadero // Disminuir la longitud de la lista
			i <- longitud_lista // Cambiar el estado a encontrado
		FinSi // Salir del bucle, ya se eliminó el elemento
	FinPara
	Si encontrado==Falso Entonces
		Escribir 'El elemento no se encuentra en la lista.'
	FinSi
	// Ordenamiento de la lista de menor a mayor
	Para i<-1 Hasta longitud_lista-1 Con Paso 1 Hacer
		Para j<-i+1 Hasta longitud_lista Con Paso 1 Hacer
			Si lista[i]>lista[j] Entonces
				// Intercambiar elementos para ordenar de menor a mayor
				temp <- lista[i]
				lista[i] <- lista[j]
				lista[j] <- temp
			FinSi
		FinPara
	FinPara
	// Mostrar lista modificada
	Escribir 'Lista modificada (ordenada de menor a mayor):'
	Para i<-1 Hasta longitud_lista Con Paso 1 Hacer
		Escribir lista[i]
	FinPara
FinProceso
