# Leer el número de vendedores
n = int(input("Ingrese el número de vendedores: "))

# Bucle para procesar cada vendedor
for i in range(1, n + 1):
    # Leer el nombre del vendedor
    nombre = input(f"Ingrese el nombre del vendedor {i}: ")
    
    # Inicializar las variables de ventas y sueldo base
    ventas_totales = 0
    sueldo_base = 450000
    
    # Bucle para ingresar las 3 ventas
    for j in range(1, 4):
        venta = float(input(f"Ingrese el monto de la venta {j} de {nombre}: "))
        ventas_totales += venta  # Sumar el monto de cada venta
    
    # Calcular la comisión (10% de las ventas)
    comisiones = ventas_totales * 0.10
    
    # Calcular el sueldo total (sueldo base + comisiones)
    sueldo_total = sueldo_base + comisiones
    
    # Mostrar los resultados
    print(f"\nVendedor: {nombre}")
    print(f"Comisiones: {comisiones:.2f}")
    print(f"Sueldo total (base + comisiones): {sueldo_total:.2f}\n")

