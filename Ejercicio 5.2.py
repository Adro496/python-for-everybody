suma = 0
contador = 0
mayor = None
menor = None
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
    if mayor == None or número > mayor :
        mayor = número
    if menor == None or número < menor :
        menor = número

print(suma, contador, menor, mayor)
