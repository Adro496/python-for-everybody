entrada = input('Ingresa un nombre de archivo: ')
manejador = open(entrada)
d = dict()
for linea in manejador:
    if linea.startswith('From ') :
        palabras = linea.split()
        remitente = palabras[1]
        dominio = remitente[remitente.find('@') + 1:]
        if dominio not in d :
            d[dominio] = 1
        else:
            d[dominio] += 1

print(d)
