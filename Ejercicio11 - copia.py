print("Ingrese la primera nota que equivale un 30% (N1) Ej:5.0")
nota1 = float(input())
print("Ingrese la segunda nota que equivale un 30% (N2) Ej:5.0")
nota2 = float(input())
print("Ingrese la tercera nota que equivale un 40% (N3) Ej:5.0")
nota3 = float(input())


nota_final = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.40)


if nota_final >= 5.0:
    print("El estudiante quedó aprobado del ramo")
elif 3.5 <= nota_final < 5.0:
    print("El estudiante debe rendir un examen")
else:
    print("El estudiante quedó reprobado")
