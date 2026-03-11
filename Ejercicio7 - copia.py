print ("Ingrese un número")
numero = int(input())

#Variables 

posi = numero + 3
negativo = numero + 6
sumneg = numero + 6

if 0 <= posi and numero < 0:
    print(f"El número {numero}, con suma de 3, da resultado {posi}")

if negativo <= 0 and numero  < 0:
    print(f"El número {numero}, con suma de 6, da resultado {negativo}")
else:
    if sumneg >= 0 and numero < 0:
        print(f"El número {numero}, con suma de 6, da resultado {sumneg}")
        
    if posi > 0 and -1 < numero:
        print(f"El número {numero}, con suma de 3, da resultado {posi}")