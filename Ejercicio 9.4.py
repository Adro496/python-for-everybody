entrada = input('Ingresa un nombre de archivo: ')
manejador = open(entrada)
d = dict()
for linea in manejador:
    if linea.startswith('From ') :
        palabras = linea.split()
        remitente = palabras[1]
        d[remitente] = d.get(remitente, 0) + 1

mayor_v = None
for clave in d :
    valor = d[clave]
    if mayor_v is None or valor > mayor_v :
        mayor_c = clave
        mayor_v = valor

print(mayor_c, mayor_v)
