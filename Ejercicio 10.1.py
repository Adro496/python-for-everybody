entrada = input('Ingresa un nombre de archivo: ')
manejador = open(entrada)
d = dict()
for linea in manejador:
    if linea.startswith('From ') :
        palabras = linea.split()
        remitente = palabras[1]
        d[remitente] = d.get(remitente, 0) + 1

t = list()
for email, contador in d.items() :
    t.append( (contador, email) )

t.sort(reverse = True)
x, y = t[0]
print(y, x)
