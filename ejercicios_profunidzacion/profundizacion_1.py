# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice un programa que pida por consola dos números que representen
el principio y fin de una secuencia numérica.
Realizar un bucle "for" que recorra esa secuencia armada con "range"
y cuente cuantos números ingresados hay, y la sumatoria de todos los números
Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
sino que va hasta el anterior.
'''

print('Comenzamos a ponernos serios!')
# Empezar aquí la resolución del ejercicio

inicio = int(input('Ingrese el primero número de la secuencia\n')) # inicio = ....
fin = int(input('Ingrese el ultimo número de la secuencia\n')) # fin = ....
cantidad_numeros = 0
sumatoria = 0
for numero in range(inicio,fin+1): # bucle.....
 cantidad_numeros += 1 # cantidad_numeros ....
 sumatoria += numero # sumatoria ....
promedio = sumatoria / cantidad_numeros

# Al terminar el bucle calcular el promedio como:
# promedio = sumatoria / cantidad_numeros
# Imprimir resultado en pantalla
print('El resultado de la suma de todos los números que intervienen en la secuencia es:', sumatoria)
print('La cantidad total de número que intervienen e la secuencia es:', cantidad_numeros)
print('El promedio total de los número que intervienen en la secuencia es:', promedio)