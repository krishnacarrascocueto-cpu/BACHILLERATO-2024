# Inicializar las variables
total_ventas = 0
num_clientes = 0

# Preguntar al usuario cuántos clientes han sido atendidos
while True:
    # Leer el monto de la compra de cada cliente
    try:
        monto_compra = float(input(f"Ingrese el monto de la compra del cliente {num_clientes + 1} (o ingrese 0 para finalizar): "))
        
        # Verificar si el monto es 0, lo que indica el fin de las ventas
        if monto_compra == 0:
            break
        
        # Sumar el monto de la compra a las ventas totales
        total_ventas += monto_compra
        num_clientes += 1  # Incrementar el número de clientes atendidos

    except ValueError:
        print("Por favor, ingrese un monto válido.")
        
# Mostrar los resultados finales
print(f"\nTotal de ventas: {total_ventas:.2f}")
print(f"Número de clientes atendidos: {num_clientes}")
