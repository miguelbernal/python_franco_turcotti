import random
'''
consonantes = 22 elementos en mayusculas
vocales = 5 elementos en mayusculas
extraer 2 bolillas de consonantes y 2 bolillas de vocales
dic de palabras de 4 letras en mayusculas
'''

consonantes = ['B','C','D','F','G']
vocales = ['A','E','I','O','U']
dic = ["ABAD","ABAR","ABES","ABEY","ABIA","ABRA","ABRE"]
letras = ['','','','']
palabra = ['','','','']

letras[0] =  random.choice(consonantes)
letras[1] = random.choice(consonantes)
letras[2] =  random.choice(vocales)
letras[3] = random.choice(vocales)
print(letras)
'''
    bcae
    baec
    beca
    b
    b
'''
for letra1 in letras:
    for letra2 in letras:
        for letra3 in letras:
            for letra4 in letras:
                palabra[0] = letra1
                palabra[1] = letra2
                palabra[2] = letra3
                palabra[3] = letra4
                if palabra.count('letra1') == 1 and palabra.count('letra2') == 1 and palabra.count('letra3') == 1 and palabra.count('letra4') == 1:
                    print(palabra)
