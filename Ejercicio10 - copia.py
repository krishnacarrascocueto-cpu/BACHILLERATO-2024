print("Ingrese el stock de los productos")
stock_de_productos = int(input())

if stock_de_productos >= 100:
    print("Ingrese el valor del producto")
    valor_producto = int(input())

    descuento = valor_producto * 0.15
    valor_final = valor_producto - descuento 

    print(f"El nuevo valor del producto con descuento es {valor_final}")
else:
    print("El valor del descuento no aplica porque el stock es menor a 100")