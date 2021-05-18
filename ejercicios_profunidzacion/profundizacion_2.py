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
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

n1 = float(input("Introduce tu primer número:\n ") )
n2 = float(input("Introduce tu segundo número:\n ") )     
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    +) Sumar los dos números
    -) Restar los dos números
    *) Multiplicar los dos números
    /) Dividir los dos numeros
    **) Potencia/exponente 
    fin) terminar el programa
    """)
    opcion = str(input("Elige una opción:\n ") ) 
    if opcion == "+":
        suma = n1 + n2
        print("La suma es", suma)
        
    elif opcion == "-":
        resta = n1 - n2
        print("La resta es", resta)
        
    elif opcion == "*":
        multiplicacion = n1 * n2
        print("La multiplicacion es", multiplicacion)
        
    elif opcion == "/":
        division = n1/n2
        if n1==0:
           print ("No se puede dividir en 0")
        print("La division es", division)
         
    elif opcion == "**":
        resultado= n1**n2
        print("el exponente es", resultado)
        
    elif opcion == "fin":
         break
    else:
        print("Opción incorrecta")