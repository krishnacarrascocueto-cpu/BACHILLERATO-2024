#Crear un algoritmo que calcule el promedio de 3 notas, conociendo que cada nota vale: 25%, 40% y 35% respectivamente

#Inicio
print ("Ingrese su nombre:")
nombre= input()

print ("------------------")

nota1= float (input("Ingrese Nota 1 que equivale un 25% (Ej: 4.5):"))
nota2= float (input("Ingrese Nota 2 que equivale un 40% (Ej: 4.5):"))
nota3= float (input("Ingrese Nota 3 que equivale un 35% (Ej: 4.5):"))

#Proceso
print ("----------------")

promedio = (nota1 * 0.25) + (nota2 * 0.40) + (nota3 * 0.35)

#Salida

print("El promedio de notas según los porcentajes es:",promedio)

