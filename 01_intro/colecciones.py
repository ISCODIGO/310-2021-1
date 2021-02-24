# Listas
lista = [1, 2, 3]
lista.append(4)
print(lista)

#Tupla
tupla = (1, [1, 2, 3])
#tupla.append(2) Esto no es posible
print(type(tupla))
tupla[1][0] = 100
tupla[1].append(45)
print(tupla)

# Convertir a tupla y a listas
l1 = list('Hola mundo')
t1 = tuple('Hola mundo')

print(l1)
print(t1)

l2 = list(tupla)
print(l2)