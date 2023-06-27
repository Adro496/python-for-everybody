entrada = input ('Introduzca puntuación: ')
try:
    puntuacion = float(entrada)

    def calcula_calificacion(p):
        if puntuacion > 1:
            calificacion = 'Puntuación incorrecta'
        elif puntuacion >= 0.9:
            calificacion = 'Sobresaliente'
        elif puntuacion >= 0.8:
            calificacion = 'Notable'
        elif puntuacion >= 0.7:
            calificacion = 'Bien'
        elif puntuacion >= 0.6:
            calificacion = 'Suficiente'
        elif puntuacion >= 0:
            calificacion = 'Insuficiente'
        else:
            calificacion = 'Puntuación incorrecta'
        return calificacion

    print(calcula_calificacion(puntuacion))
except:
    print('Puntuación incorrecta')
