'''
v = Vector(2)

v[0] = 10
v[1] = 5

# <10, 5>

w = Vector(3)
w[0] = 5
w[1] = 50
w[2] = 100

# <5, 50, 100>

x = v + v
# <20, 10>
'''

class Vector:
    def __init__(self, dimension:int) -> None:
        self.coordenadas = [0] * dimension

    def __str__(self) -> str:
        ''' Se comporta como el toString() de Java '''
        return str(self.coordenadas)

    # Accesors (lectura)
    def __getitem__(self, indice:int) -> int:
        return self.coordenadas[indice]

    # Mutators (modificacion)
    def __setitem__(self, indice:int, valor:int) -> None:
        self.coordenadas[indice] = valor

    def __len__(self) -> int:
        return len(self.coordenadas)

    def __add__(self, otro):
        dimension = len(self)
        if dimension != len(otro):
            raise ValueError('Las dimensiones de los vectores no concuerdan')
        # nuevo objeto Vector
        suma = Vector(dimension)
        for i in range(dimension):
            suma[i] = self[i] + otro[i]
        return suma


if __name__ == '__main__':
    v = Vector(2)
    v[0] = 1
    v[1] = 2
    print('v[0] = ', v[0])
    print('Vector v:', v)

    w = Vector(2)
    w[0] = 3
    w[1] = 4
    print('Vector w: ', w)

    z = v + w
    print('v + w = ', z)

    print('len(z) = ', len(z))

    a = v - w
    
'''
c = a + b
a.__add__(b)

a == b
a.__eq__(b)

a != b
a.__ne__(b)

len(a)
a.__len__()
'''