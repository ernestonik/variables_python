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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''
print ("Ingresa el primer numero:")
numero1 = float(input())

print ("Ingresa el segundo numero:")
numero2 = float(input())

Suma = (numero1 + numero2)
print ("El resultado de la suma entre", numero1, "y" , numero2 , "es" , Suma)
Resta = (numero1 - numero2)
print ("El resultado de la resta entre", numero1, "y" , numero2 , "es" , Resta)
Multip = (numero1 * numero2)
print ("El resultado de la multiplicacion entre", numero1, "y" , numero2 , "es" , Multip)
Division = (numero1 / numero2)
print ("El resultado de la division entre", numero1, "y" , numero2 , "es" , Division)
Exponente = (numero1 ** numero2)
print ("El resultado de la potencia entre", numero1, "y" , numero2 , "es" , Exponente)


print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio