# -*- coding: utf-8 -*-
"""Cant_dias.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EpL8EqMMnTv4ke-UPE0L9P8RCwfCdRZw

Este es un ejemplo de como escribir un pequeño script de python que haga cualquier cosa para demostrar su uso.
"""

nombre = input("Dime tu nombre: ") #input en Python es el equivalente a Escribir y Leer en pseint
print(f"Hola {nombre}, qué tal estas?") # print es el equivalente en pseint de Escribir

"""Se va a calcular la cantidad de dias que una persona ha vivido a partir de su fecha de nacimiento."""

from datetime import datetime

#date_str = '25/09/2023'
date_format = '%d/%m/%Y'

nac = input(f"{nombre} dime tu fecha de nacimiento en el formato dd/mm/aaaa: ")
date_obj = datetime.strptime(nac, date_format)
days = (datetime.now() - date_obj).days

print(f"{nombre} has vivido por {days} días")

"""Script para sumar n numeros"""

n = int(input("Dime cuantos numeros vas a sumar: "))
suma = 0

for numero in range(n):
  valor = int(input(f"Dame el numero {numero} a sumar: "))
  suma = suma + valor
  print(f"hasta ahora, la suma total es de {suma}")

print(f"La suma final es de {suma}")