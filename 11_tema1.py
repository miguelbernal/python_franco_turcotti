'''
consonantes = 22 elementos en mayusculas
vocales = 5 elementos en mayusculas
extraer 2 bolillas de consonantes y 2 bolillas de vocales
dic de palabras de 4 letras en mayusculas
'''
import random
c='bcdfghjklmnpqrstvwxyz'
v='aeiou'
letras=['','','','']
letras[0] = random.choice(c)
letras[1] = random.choice(c)
letras[2] = random.choice(v)
letras[3] = random.choice(v)
print(letras)

i = 0
while i < 1:
    print (letras[i],letras[i+1],letras[i+2],letras[i+3])
    print (letras[i],letras[i+2],letras[i+3],letras[i+1])
    print (letras[i],letras[i+3],letras[i+1],letras[i+2])
    i = i + 1
    

