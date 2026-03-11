#Inicio

print("Ingrese el total de la compra:")
total_de_compra= float (input())


#Proceso 

descuento= total_de_compra * 0.15
total_de_final_de_compra= total_de_compra - descuento 

#Salida 

print("Se ha aplicado un descuento de $",descuento)
print("El monto tal a pagar es de $" ,total_de_final_de_compra)
