print("Ingrese su nombre")
nomb1 = input()
print("Ingrese su edad")
edad1 = int(input())
print("Ingrese su nombre")
nomb2 = input()
print("Ingrese su edad")
edad2 = int(input())

if edad1 < edad2:
    print(f"El menor de edad es {nomb1}, y el mayor es {nomb2}")
else:
    if edad1 > edad2:
        print(f"El menor de edad es {nomb2}, y el mayor es {nomb1}")