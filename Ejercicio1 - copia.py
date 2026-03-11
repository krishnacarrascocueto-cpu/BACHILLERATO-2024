 #Introducir un número por teclado y decir si es par o impar

#Inicio

input("Ingrese un número")
num= int(input())

if num % 2 == 0:
    print ("El número ingresado es par")
else:
    print ("El número ingresado es impar")