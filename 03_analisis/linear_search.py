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

n = 1000000
l1 = [2, 4, 6, 8, 3, 9, 5, 7]
l2 = [0] * n
l3 = l2 + l1

# Medicion de tiempo
t_inicio = time.time()
a = linear_search(l3, 3)
t_final = time.time()
dif = t_final - t_inicio
print('Tiempo= ', dif)

'''
Tiempo=  0.11121511459350586
Tiempo=  0.07894706726074219
Tiempo=  0.09076690673828125
Tiempo=  0.09628438949584961
'''


a = 1
a = 100000000
