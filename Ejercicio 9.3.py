entrada = input('Ingresa un nombre de archivo: ')
manejador = open(entrada)
d = dict()
for linea in manejador:
    if linea.startswith('From ') :
        palabras = linea.split()
        remitente = palabras[1]
        d[remitente] = d.get(remitente, 0) + 1

print(d)
