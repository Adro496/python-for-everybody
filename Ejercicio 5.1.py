suma = 0
contador = 0
while True:
    entrada = input('Introduzca un número: ')
    if entrada == 'fin':
        break
    try:
        número = int(entrada)
    except:
        print('Entrada inválida')
        continue
    suma = suma + número
    contador = contador + 1

print(suma, contador, suma/contador)
