#Aumentar el sueldo de una persona en un 20%. Mostrar el sueldo antiguo y el nuevo sueldo.

#Inicio

print("Ingrese su nombre")
nombre = input()

print ("---------------")

print("Ingrese su sueldo")
sueldo = float (input())

print("------------------")

aumento = sueldo * 0.20
nuevo = sueldo + aumento

print ("El sueldo antiguo es:",sueldo)
print("El sueldo aumentado es:" ,nuevo)