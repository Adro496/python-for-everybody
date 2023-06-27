import urllib.request

entrada = input('Ingrese URL: ')
man_a = urllib.request.urlopen('http://' + entrada)
contador = 0

for linea in man_a:
    linea = linea.decode().rstrip()
    contador = contador + len(linea)
    if contador <= 3000:
        print(linea)

print('\nCaracteres totales: ', contador)
