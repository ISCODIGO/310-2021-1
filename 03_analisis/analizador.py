import time

N = 40_000_000
lista = [1] + [0] * (N // 2) + [2] + [0] * (N // 2) + [3]

def iniciar_lista_doble(lista_doble):
    for _ in range(N):
        lista_doble.append([0, 0, 0])
    lista_doble += [1,2,3], [3,5,6], [7,4,5]
    #print(lista_doble)

def calcular_tiempo(func, n):
    ''' 
    Funcion que calcula el tiempo de ejecucion
    de una funcion 'func' con una entrada n
    '''
    t_inicio = time
    func(n)
    t_final = time.time()
    dif = t_final - t_inicio
    print('Tiempo transcurrido=', dif)


def asignar(n):
    a = n

def suma(n):
    a = 60000
    c = a + n

def acceder(n):
    return lista[n]


# Estos valores dependen de N

def linear_search(valor):
    posicion = -1
    indice = 0
    for x in lista:
        if x == valor:
            posicion = indice
            break
        indice += 1
    return posicion

def valor_maximo_matriz(lista_doble):
    maximo = 0
    for x in lista_doble:
        for y in x:
            if maximo < y:
                maximo = y            
    return maximo


if __name__ == '__main__':
    ld = []
    iniciar_lista_doble(ld)
    t1 = time.time()
    v = valor_maximo_matriz(ld)
    t2 = time.time()
    print('Valor maximo:', v)
    print(f'Transcurrido: {t2 - t1}')
    
    #print(len(lista))