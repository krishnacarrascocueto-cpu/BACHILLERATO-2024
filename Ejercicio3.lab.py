#Inicio
#Entrada
print("Ingrese el nombre del alumn@: ")
nombre_apell = input()
print("Ingrese la cantidad de asistensias: ")
asistencias = int(input())

total_clases = 30
#Proceso
inasistencias = total_clases - asistencias
porcen_asistencias = (asistencias / total_clases) * 100
porce_inasistencias = (inasistencias / total_clases) * 100

#Salida
if porce_inasistencias > 60:
    print(f"El alumn@ {nombre_apell} reprobado")
    print(f"Porcentaje de inasistencias:{porce_inasistencias}%")
else:
    print(f"El alumn@ {nombre_apell} cumple con lo exigido")
    print(f"Porcentaje de asistencias:{porcen_asistencias}%")