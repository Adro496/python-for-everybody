entrada = input('Ingresa un nombre de archivo: ')
manejador = open(entrada)
contador = 0
for linea in manejador:
    if linea.startswith('From ') :
        palabras = linea.split()
        contador = contador + 1
        print(palabras[1])

print('Hay', contador, 'líneas en el archivo con la palabra From al inicio')
