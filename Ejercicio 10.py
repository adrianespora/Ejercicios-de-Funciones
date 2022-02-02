#Escribir una función que convierta un número decimal en binario
# y otra que convierta un número binario en decimal.

def a_binario(lista1):
    bin(lista1)
    binario = int(bin(lista1)[2:])
    print(binario)
def a_decimal(lista2):
    b = (lista2)
    decimal = int(str(b),2)
    print(decimal)

a_binario(11)
a_binario(2)
a_decimal(1011)
a_decimal(10)