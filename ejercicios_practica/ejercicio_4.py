# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
# Si desea puede modificar el código para ingresar más palabras
print('Ingrese palabra 1:')
palabra_1 = str(input())
l_p1 = len(palabra_1)

print('Ingrese palabra 2:')
palabra_2 = str(input())
l_p2 = len(palabra_2)

print('Ingrese palabra 3:')
palabra_3 = str(input())
l_p3 = len(palabra_3)

print ("Tu acronimo es: " + palabra_1[0] + palabra_2[0] + palabra_3 [0])
print ("Muchas gracias por tu consulta")

# De cada palabra debe tomar la primera letra y armar el acrónimo
# Ejemplo: Alumbrado, barrido y limpieza --> ABL
# Imprimir el resultado en pantalla