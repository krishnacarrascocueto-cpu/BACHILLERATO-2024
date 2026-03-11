#Inicio 

#Variables
niños = 3000
adultos = 5000
adulto_mayor = 2000

#Entrada y proceso
costo_total = 0 


print("¿Cuantas personas son?")
n = int(input())
for i in range(n):
    print("Persona" ,i + 1)
    print("Ingrese su edad")
    edad = int(input())
    
    if edad <= 9: #Niños menores e iguales de 9 años
        costo_total += niños 
    elif 9 < edad < 65: #Adultos mayor a 9 años
        costo_total += adultos
    else: #Adulto mayor
         costo_total += adulto_mayor

#Salida 

print(f"El costo total de las entradas es {costo_total}")



