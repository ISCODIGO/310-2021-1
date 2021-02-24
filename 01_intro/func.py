def saludo(persona, saludo_final="que tal"):
    print('Hola', persona, saludo_final)



saludo("Francia", "como has estado")
saludo("Emilio")


def sumar(a:int, b:int):
    return a + b

def sumar2(valores:list):
    suma = 0
    for item in valores:
        suma += item
    return suma

# args -> list, kwargs -> dict
def sumar3(*args):
    suma = 0
    for item in args:
        suma += item
    return suma


print('Sumar2=',sumar2([1, 2, 3]))

print('Sumar3=',sumar3(1))
print('Sumar3=',sumar3(1, 2))
print('Sumar3=',sumar3(1, 2, 3))

print('Type sumar3:', type(sumar3))

x = sumar3
s = x(4, 5, 6)
print(s)

def check_tipo(x):
    print(type(x))

check_tipo(3)
check_tipo("Hola")
check_tipo(True)
check_tipo(sumar3)