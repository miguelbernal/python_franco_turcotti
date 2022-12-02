# Adivinar el numero
# Generar un numero aleatorio de 1 al 5
# Hacer el programa para preguntar al usuario el numero
# El programa deber decirle al usuario si el numero que él introdujo es mayor o menor al numero
# generado por la computadora
# Imprimir el numero adivinado y la cantidad de veces en la que se adivinó

import random
adivinar = random.randint(1,5)
adivinado = False
intentos = 0
while adivinado == False:
    intentos += 1
    numero = int(input("Cuál es el numero? "))
    if adivinar == numero:
        adivinado = True
    elif adivinar > numero:
        print("El número a adivinar es mayor")
    else:
        print("El número a adivinar es menor")

print(f"""Haz adivinado, el número es: {adivinar},  y lo haz hecho en {intentos} intentos.""" )
