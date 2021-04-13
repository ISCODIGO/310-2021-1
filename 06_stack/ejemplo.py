'''
06-01
-----
En este ejemplo se puede ver la ejecucion de los llamados de las funciones
almacenados en una pila.

Al iniciar se llaman de la siguiente forma:
A()
B()
C()

Pero la ejecucion del print (que marca el final del llamado) es en el 
siguiente orden:
C()
B()
A()
'''

def a():
    b()
    print('A')

def b():
    c()
    print('B')

def c():
    print('C')

a()