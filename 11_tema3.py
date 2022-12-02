# Solicitar notas para 5 alumnos

NOTAS = []
N = int(input("Ingrese la cantidad de alumnos: "))
for i in range(N*3):
    NOTAS.append(int(input("Inserte la nota del alumno: ")))

print(NOTAS)
sec = [1,2,3]
proms = []
des = []

# seccion 1
sumnot1 = 0
c = 0
not1 = []
for i in range(N):
    not1.append(NOTAS[i])
    sumnot1 += not1[c]
    c += 1
prom1 = sumnot1 / N
proms.append(prom1)
miu1 = 0
for i in range(N):
    miu1 += (not1[i]-prom1)**2
de1 = (miu1/(N-1)**(1/2))
des.append(de1)

# seccion 2
sumnot2 = 0
c = 0
not2 = []
for i in range(N, 2*N):
    not2.append(NOTAS[i])
    sumnot2 += not2[c]
    c += 1
prom2 = sumnot2 / N
proms.append(prom2)
miu2 = 0
for i in range(N):
    miu2 += (not2[i]-prom2)**2
de2 = (miu2/(N-1)**(1/2))
des.append(de2)

# seccion 3
sumnot3 = 0
c = 0
not3 = []
for i in range(2*N, 3*N):
    not3.append(NOTAS[i])
    sumnot3 += not3[c]
    c += 1
prom3 = sumnot3 / N
proms.append(prom3)
miu3 = 0
for i in range(N):
    miu3 += (not3[i]-prom3)**2
de3 = (miu3/(N-1)**(1/2))
des.append(de3)

print("Seccion 1: ", not1)
print("Seccion 2: ", not2)
print("Seccion 3: ", not3)

for i in range(3):
    for j in range(i+1,3):
        if proms[i] > proms[j]:
            proms[i], proms[j] = des[j], des[i]
            sec[i], sec[j] = sec[j], sec[i]

print("Sección\t\tPromedio\t\tDesviación Típica\t\t")
for i in range(3):
    print("\t", sec[i], "\t\t", proms[i], "\t\t\t", des[i])