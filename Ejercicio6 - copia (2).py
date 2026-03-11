suma = 0
print("¿Cuantos alumnos son:")
alumnos = int(input())

for i in range(alumnos):
    print("Persona" ,i + 1)
    print("Ingrese su nombre y apellido")
    nomb_apelli = input()
    print("Ingrese su edad")
    edad = int(input())
    suma += edad
    
promedio = suma   / alumnos

print(f"El promedio de edades entre hombres y mujeres es {promedio}")