def sumar(numero1,numero2):
    return numero1 + numero2

def restar(numero1,numero2):
    return numero1 - numero2

def multiplicar(numero1,numero2):
    return numero1 * numero2

def dividir(numero1,numero2):
    return numero1 / numero2

print(sumar(5,10))
print(restar(50,8))
print(multiplicar(10,15))
print(dividir(150,2))
print(sumar(250,375))

def saludar(saludo, nombre = ", como te llamas?"):
    return saludo + " " + nombre

print(saludar("Hola"))
print(saludar("Hola","Juan"))
print(saludar(nombre = "Ana",saludo = "Hola"))




