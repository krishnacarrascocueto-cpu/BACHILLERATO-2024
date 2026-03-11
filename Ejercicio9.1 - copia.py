# Inicio
print("Ingrese su nombre y apellido:")
nom_ape = input()

print("¿Es soltera? Marque 1; ¿Es casada? Marque 2:")
estado_civil = int(input())

print("¿Cuántos hijos tiene? Si no tiene, indique 0:")
hijos = int(input())

print("¿Tiene título técnico? (S/N):")
titulo_tecnico = input().strip().lower()  # Normalizamos entrada a minúsculas

print("¿Cuál es su edad?")
edad = int(input())

# Proceso
cumple_requisito = False

if estado_civil == 1:  # Soltera
    if titulo_tecnico == "s" and hijos == 0 and edad < 24:
        cumple_requisito = True
elif estado_civil == 2:  # Casada
    if edad > 40 and hijos > 0:  # Para casadas, no importa el título técnico
        cumple_requisito = True

# Salida
if cumple_requisito:
    print(f"Estimad@ {nom_ape}, cumple con los requisitos para el puesto.")
else:
    print(f"Estimad@ {nom_ape}, NO cumple con los requisitos para el puesto.")
