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
    print(letra)

for veces in range(1, (len(palabraAAdivinar) * 2) + 1):
    letra = pedirLetra()
    verificarLetra(letra)
    verPalabraAdivinada()

