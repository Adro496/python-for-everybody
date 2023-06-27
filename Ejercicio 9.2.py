entrada = input('Ingresa un nombre de archivo: ')
manejador = open(entrada)
d = dict()
for linea in manejador:
    if linea.startswith('From ') :
        palabras = linea.split()
        dia = palabras[2]
        d[dia] = d.get(dia, 0) + 1

print(d)
