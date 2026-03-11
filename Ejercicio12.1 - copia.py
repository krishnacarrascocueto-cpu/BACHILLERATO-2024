print("Ingrese las horas de trabajo:")
horas = int(input())

print("¿Tiene horas extras? (S/N):")
horas_extras = input()


salario_base = 8900 * horas
salario_total = salario_base


if horas_extras.lower() == "s":
    print("¿Cuántas horas extras hace?")
    horas_extra_trabajadas = int(input())
    salario_extras = 15000 * horas_extra_trabajadas
    salario_total += salario_extras  


if horas <= 40:
    print(f"El sueldo mensual por 40 horas o menos es: ${salario_total}")
else:
    print(f"El sueldo mensual con más de 40 horas y horas extras es: ${salario_total}")
