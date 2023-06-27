def cuenta(letra, cadena) :
    contador = 0
    for i in cadena :
        if i == letra :
            contador = contador + 1
    print(contador)

cuenta('o', '¿Cuántas "o" tengo?')
