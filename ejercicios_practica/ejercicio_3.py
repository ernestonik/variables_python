
# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo

print('Ingrese por consola su nombre/s:')
nombre = str(input("Nombre Completo: "))

print('Ingrese por consola su apellido/s:')
apellido = str(input("Primer Apellido: "))

# Imprima su nombre completo
# Almacenar su nombre completo en una variable
# nombre_completo = .....
nombre_completo = nombre + " " + apellido
print ("Su nombre es" , nombre_completo)
# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
len_apellido = len(apellido)
print ("Tu apellido tiene", len_apellido, "letras")
Mail = (nombre[0:3] + apellido[0])
print ("Su mail quedaria confirmado como: " + Mail + "@sumail.com")
print ("Gracias por tu consulta")


