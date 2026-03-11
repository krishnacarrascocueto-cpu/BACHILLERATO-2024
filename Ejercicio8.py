#Un individuo desea invertir su capital en un banco y desea saber cuánto dinero ganará después de un n meses si el banco paga a razón de 2% mensual. Mostrar el resultado.

#Inicio 

print("Ingrese su capital inicial del dinero:")
capital_del_dinero= float (input())

print("Ingrese el número de meses:")
numero_de_meses= int (input())

print("---------------")

#Proceso

tasa_mensual= 0.02
monto_final= capital_del_dinero * (1 + tasa_mensual) * numero_de_meses

#Salida 

print("El monto final después de", numero_de_meses, "meses es:", monto_final)