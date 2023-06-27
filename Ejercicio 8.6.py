lista_numeros = []
while True:
    entrada = input('Ingresa un número: ')
    if entrada == 'hecho' : break
    try:
        numero = float(entrada)
    except:
        print('Entrada inválida')
        continue
    lista_numeros.append(numero)

print('Máximo:', max(lista_numeros))
print('Mínimo:', min(lista_numeros))
