'''
06-02
-----
En este codigo se intuye que puede utilizarse la coleccion list para la 
manipulacion de una pila
'''

lista = []
# Prueba de operacion PUSH
lista.append(10)
lista.append(20)
lista.append(30)

# Prueba de operacion TOP
print(lista[-1])

# Prueba de operacion POP
eliminado = lista.pop()
print('Eliminado=', eliminado)
print(lista)

eliminado = lista.pop()
print('Eliminado=', eliminado)
print(lista)