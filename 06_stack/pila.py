''' 
06-03
-----
Clase de Pila. Tiene las funciones basicas de una pila y utiliza un list como
elemento interno de almacenamiento.
'''
class Pila:
    def __init__(self):
        self.__datos = []
        self.__size = 0

    def push(self, elemento):
        ''' 
        Funcion para insertar un elemento en la pila.
        Cambia la cima actual.
        '''
        self.__datos.append(elemento)
        self.__size += 1

    def pop(self):
        ''' 
        Funcion para remover la cima de la pila.
        '''
        self.__size -= 1
        return self.__datos.pop()

    def top(self):
        '''
        Funcion que devuelve la cima sin eliminarla.
        '''
        return self.__datos[-1]

    def clear(self):
        '''
        Funcion que elimina todos los elementos de la pila.
        '''
        self.__datos = []
        self.__size = 0

    def is_empty(self) -> bool:
        '''
        Funcion determina si la pila esta o no vacia.
        '''
        return self.__size == 0

    def __len__(self):
        return self.__size

    def __str__(self) -> str:
        cadena = ''
        for i in range(self.__size - 1, -1, -1):
            cadena += str(self.__datos[i]) + '-'
        return cadena
        
        
if __name__ == '__main__':
    s = Pila()
    s.push(10)
    s.push(20)
    s.push(30)

    print('Cima=', s.top())
    print('len=', len(s))
    print('pop=', s.pop())
    print('Pila=', s)