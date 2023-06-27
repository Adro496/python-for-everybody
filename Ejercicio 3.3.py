entrada = input ('Introduzca puntuación: ')
try:
    puntuacion = float(entrada)
    if puntuacion > 1 :
        print('Puntuación incorrecta')
    elif puntuacion >= 0.9 :
        print('Sobresaliente')
    elif puntuacion >= 0.8 :
        print('Notable')
    elif puntuacion >= 0.7 :
        print('Bien')
    elif puntuacion >= 0.6 :
        print('Suficiente')
    elif puntuacion >= 0 :
        print('Insuficiente')
    else:
        print('Puntuación incorrecta')
except:
    print('Puntuación incorrecta')
