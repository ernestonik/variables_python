# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
Realice un programa que consulte por consola:
- El nombre completo de la persona
- El DNI de la persona
- La edad de la persona
- La altura de la persona

Finalmente el programa debe imprimir dos líneas de texto por separado
- En una línea imprimir el nombre completo y el DNI, aclarando de que
  campo se trata cada uno
        Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
- En la segunda línea se debe imprimir el nombre completo, edad y
  altura de la persona
  Nuevamente debe aclarar el campo de cada uno, para el que lo lea
  entienda de que se está hablando.
'''
print ("Ingrese su nombre completo:")
nombre = str (input())
print ("Ingrese su apellido")
apellido = str(input())
print ("Ingrese su numero de documento sin puntos:")
dni = int (input ())
print ("Ingrese su edad:")
edad = int(input())
print ("Ingrese su altura:")
alto = float (input())

print ("Para el registro su nombre completo es", nombre.upper(), apellido.upper(), "y su numero de DNI es" , dni)
print ("Su nombre completo es", nombre.upper(), apellido.upper(), "cuya edad es" , edad, "y su altura es de", alto, "mtrs")
print('Sistema de ingreso de datos')
# Empezar aquí la resolución del ejercicio
