def diccionario(cadena):
    lista = cadena.split()
    frecuenciapalab = []
    diccio = {}

    for palabra in lista: ## recorro las palabras de la lista
        frecuenciapalab.append(lista.count(palabra)) ## agrego a la lista frecuenciapalab las veces que esta repetida la palabra
    n = 0 ## La variable n va fuera del bucle para que la tome en cuenta solo al comienzo del bucle
    for clave in lista:
        diccio[clave] = frecuenciapalab[n] ## Asigno la cantidad de veces que se repitio la palabra a su diccionario
        n += 1

    return diccio


def tupla(diccio):

    listaparatupla = []
    maximo_repetido = max(diccio.values())
    listaparatupla.append(maximo_repetido)
    for key, value in diccio.items():
        if maximo_repetido == value:
            listaparatupla.append(key)

    return tuple(reversed(listaparatupla))

frase = "Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"
print(diccionario(frase))
print(tupla(diccionario(frase)))