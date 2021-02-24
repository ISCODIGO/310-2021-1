'''
Un programa que pida una edad      [input]
revise si la persona es menor de edad, ciudadano o mayor de edad  [if]
e imprima el resultado              [print]
'''

edad = int(input('Escriba una edad: '))
if edad < 18:
    print('Menor de edad')
elif edad < 21:
    print('Ciudadano')
else:
    print('Mayor de edad')
 
