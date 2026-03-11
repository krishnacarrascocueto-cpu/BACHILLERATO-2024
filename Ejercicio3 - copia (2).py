inicio = 50
paso = -2
numeros = 20

suma = 0
for i in range(numeros):
    suma += inicio
    inicio += paso

print(f"La suma de los números es {suma}")