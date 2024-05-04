#Ejercicios

"""
1. Numero impar por teclado. Si numero par no es introducido, repetir.
"""

def numero_impar():
    while True:
        if  int(input("Odd number: ")) % 2 != 0:
            return("Numero impar introducido")
            break
        else:
            return numero_impar()
            break

print(numero_impar())