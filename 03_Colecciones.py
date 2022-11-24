# Colecciones
# Tupla
# indice->   0        1        2        3          4        5         6 
tupla = ('Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado')
print(tupla)
print(type(tupla))
print(dir(tupla))
print(tupla[0])
#tupla[0] = "Dom" # No se puede hacer porque las tuplas no se pueden modificar
tupla = ('DOM','LUN','MAR','MIE','JUE','VIE','SAB')
print(tupla)
# Lista (Se pueden modificar)
lista = ["Juan",18,True,5.0]
print(lista)
lista[0] = "Ana"
print(lista)
# Set
sets = {'Ana',25,False,4.5}
print(sets)
#print(sets[2]) # No se puede acceder por un indice
print('Ana Gonzalez' in sets)
# Diccionarios
diccionario = {
    "nombre": "Juan",
    "apellido": "Gonzalez",
    "edad": 25,
    "estudia": True
}
diccionario2 = {
    "nombre": "Ana",
    "apellido": "Perez",
    "edad": 35,
    "estudia": False
}
diccionario['nombre'] = "Franco"
diccionario['edad'] = 20
diccionarios = [] # Esto es una lista
print(diccionario)
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())
#diccionario.clear()
#print(diccionario)
#del diccionario
#print(diccionario)
diccionarios.append(diccionario)
diccionarios.append(diccionario2)
diccionarios.append('Pedro')
diccionarios.append(45)
print(diccionarios)
