print('Linea 1')
print('Linea 2')
# operador de asignacion
edad = 15
# Estructura if (Bifurcacion)
# Si
# (condicion)
#       operador de comparacion (>,<, >=, <=, ==)
if(edad >= 18):
    # Se ejecuta todo el bloque si se cumple la condicion
    print('Eres mayor de edad')

# Estructura if else
if(edad >= 18):
    # Se ejecuta todo el bloque si se cumple la condicion
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

print("Fuera del bloque del If")

# if else anidado
dia = 3
if dia == 1:
    print('Domingo')
else: 
    if dia == 2:
        print('Lunes')
    else: 
        if dia == 3:
            print('Martes')

# if else if (switch)
if dia == 1:
    print('Domingo')
elif dia == 2:
        print('Lunes')
elif dia == 3:
    print('Martes')

# Ciclicos
dias = ('Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado')
# for (automatico)
for dia in dias:
    print(dia)

print('Continuando fuera del ciclo...')

# while (manual)
i = 1 # inicializa la variable
#     condicion 
while i < 6:
  print(i)
  i += 1 # incremento












