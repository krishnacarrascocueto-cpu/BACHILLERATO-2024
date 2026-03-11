print("Ingrese la cantidad de estudiantes")
n = int(input())

for i in range(n):
    print("Persona" ,i + 1)
    print("Ingrese su nombre y apellido")
    nombre = input()
    print("Ingrese su nota 1. Ej: 4.0")
    n1 = float(input())
    print("Ingrese su nota 2. Ej: 4.0")
    n2 = float(input())
    print("Ingrese su nota 3. Ej: 4.0")
    n3 = float(input())
    notas = (n1 + n2 + n3) / 3

    print(f"El promedio del estudiante es {notas}")

    if notas < 4:
        print(f"Alumno/a {nombre} queda reprobado/a")

    if notas > 4:
        print(f"Alumno/a {nombre} queda aprobado/a")
