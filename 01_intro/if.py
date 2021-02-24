# Corto-circuito
# and / or

x = 10
y = 0

if x > 0 or x/y == 1:
    print('Ambas condiciones se evaluaron')
else:
    print('No se ha evaluado la segunda condicion')


# Evaluar un rango de valores numericos:
# Que un numero este entre 0 y 5

x = 3
if x <= 5 and x >= 0:
    print('Esta en el rango')

if 0 <= x <= 5:
    print('Esta en el rango (v2)')
