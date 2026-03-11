# Ingrese el año de nacimiento de una persona. Determine la edad aproximada a la fecha de hoy y además si es un menor, adulto o adulto mayor según la ley.

#Inicio 

input("Ingrese el año actual: (Ej:2024)")
año_actual= int(input())

input("Ingrese el año de nacimiento (Ej:2024)")
año_nacimiento= int(input())

#Proceso

edad = int(año_actual - año_nacimiento) 
if edad >= 18:
    print(f"Su edad es {edad} y corresponde ser mayor de edad")
else:
    print(f"Su edad es {edad} y corresponde ser menor de edad")