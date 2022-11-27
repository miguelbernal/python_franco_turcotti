'''
1. Palabra a averiguar (python) hecho
2. Pedir una letra la cantidad de letras de la palabra * 2
3. Si la letra esta en la palabra mostar mostrar todo lo que se acertó hasta el momento
'''

palabraAAdivinar = ['p','y','t','h','o','n']
palabraAdivinada = ['_','_','_','_','_','_']
def pedirLetra():
    letra = input('Letra de la palabra: ')
    return letra

def verPalabraAdivinada():
    for letra in palabraAdivinada:
        print(letra, end='')
    print('')

def verificarLetra(letra):
    pos = 0
    while pos < len(palabraAAdivinar):
        if(palabraAAdivinar[pos] == letra):
            palabraAdivinada[pos] = letra
        pos = pos + 1

def verificarGanador():
    pos = 0
    ganador = True
    while pos < len(palabraAdivinada):
        if(palabraAdivinada[pos] == "_"):
            ganador = False
            break
        pos = pos + 1
    return ganador

gano = False
for veces in range(1, (len(palabraAAdivinar) * 2) + 1):
    letra = pedirLetra()
    verificarLetra(letra)
    verPalabraAdivinada()
    if verificarGanador():
        gano = True
        break

if(gano):
    print("Haz ganado!!!")
else:
    print("Intentalo de nuevo!!!")
