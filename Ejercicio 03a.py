def factorial(numero):
    if numero > 0:          ## si el numero es mayor que 0
        i = 1               ## a la variable i le asigno el numero 1
        factoriales = []    ## creo una lista para guardar los factoriales que se crearan
        multiplo = 1        ## le doy valor 1 a la variable que la usare en el bucle for
        while i <= numero:   ## Cuando i sea menor o igual que numero ejecuto esto
            factoriales.append(i)      ## agrego a la lista factoriales los valores que van surgiendo
            i += 1                      ## le sumo 1 a i
        for f in factoriales:           ## recorro la lista de factoriales para multiplicarlos
            multiplo = f * multiplo     ## guardo en multiplo la multiplicacion de multiplo con el valor recorrido
        print(multiplo)

factorial(5)