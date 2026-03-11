#Un vendedor que recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta que su sueldo base es de 480000. Mostrar el resultado.

#Inicio 

print("Ingrese la primera venta")
primera_venta= float (input())

print("Ingrese la segunda venta")
segunda_venta= float (input())

print("Ingrese la tercera venta")
tercera_venta= float (input())

print("------------")

#Proceso

comisiones = (primera_venta * 0.10 + segunda_venta * 0.10 + tercera_venta * 0.10)
sueldo_final= comisiones + 480000

#Salida 

print("Las comisiones de las ventas son " ,comisiones)
print("El sueldo con las comisiones agregadas es de " ,sueldo_final)