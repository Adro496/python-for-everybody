entrada = input('Ingresa un nombre de archivo: ')
manejador = open(entrada)
d = dict()
for linea in manejador:
    if linea.startswith('From ') :
        palabras = linea.split()
        horario = palabras[5].split(':')
        hora = horario[0]
        d[hora] = d.get(hora, 0) + 1

t = []
for clave, valor in d.items() :
    t.append( (clave, valor) )

t.sort()
for x, y in t :
    print(x, y)
