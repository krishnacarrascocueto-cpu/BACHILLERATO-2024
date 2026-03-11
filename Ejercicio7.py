#Calcular el área total de un cilindro recto

#Inicio

print("Ingrese el radio de la base:")
radio= float (input())

print("Ingrese la altura de la base:")
altura= float (input())

print ("--------------------")

#Proceso
pi= 3.14

area_lateral= 2 * pi * radio * altura

area_total=  2 * pi * radio  * (radio + altura )

#Salida 

print("El área lateral del cilindro recto es:"  ,area_lateral)
print("El área total del cilindro recto es:" ,area_total)