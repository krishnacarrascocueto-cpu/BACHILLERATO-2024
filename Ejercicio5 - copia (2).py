
hombres = 0
mujeres = 0


n = int(input("Ingrese la cantidad de personas en el grupo: "))


for i in range(n):
    print("Persona", i + 1)
    nombre = input("Ingrese el nombre: ")
    genero = input("Ingrese el género (M para masculino, F para femenino): ")

    
    if genero == "M":
        hombres = hombres + 1
    elif genero == "F":
        mujeres = mujeres + 1


print("Cantidad de hombres:", hombres)
print("Cantidad de mujeres:", mujeres)



