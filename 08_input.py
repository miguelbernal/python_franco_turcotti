edad = input('¿Qué edad tienes? -> ')
print(type(edad))
print("Tú tienes " + edad + " años.")
if int(edad) > 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")