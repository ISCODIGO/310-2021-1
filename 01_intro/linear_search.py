'''
JAVA
[tipo de dato] [nombre funcion]
void linearSearch()

PHP
function [nombre funcion]
function linear_search()

PYTHON
def [nombre funcion]
def linear_search()

'''

import time

def linear_search(coleccion, valor):
    posicion = -1
    indice = 0
    for x in coleccion:
        if x == valor:
            posicion = indice
            break
        indice += 1
    return posicion


l1 = [2, 4, 6, 8, 3, 9, 5, 7]
l2 = [0] * 100
l3 = l1 + l2
#print(l3)
t_inicio = time.time()
a = linear_search(l3, 3)
print(a)
t_final = time.time()
diferencia = t_final - t_inicio
print(diferencia)