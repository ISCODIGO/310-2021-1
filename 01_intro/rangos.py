lista = [4, 6, 2, 65, 89, 12, 4, 55]
lista2 = [1, True, [1, 2, 3]]

for x in lista2:
    print(x, type(x))


# Imprimir los valores de 'lista' que esten en indices pares.
for i in range(len(lista)):
    if i % 2 == 0:
        print(lista[i])

 
