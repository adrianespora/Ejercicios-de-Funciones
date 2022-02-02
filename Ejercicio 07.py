#Escribir una función que reciba una muestra de números
#en una lista y devuelva otra lista con sus cuadrados.

def muestra(lista):
    nueva_lista = []
    for i in lista:
        nueva_lista.append(i*i)
    
    print(nueva_lista)

numeros = [1,2,3,4,5]
muestra(numeros)
