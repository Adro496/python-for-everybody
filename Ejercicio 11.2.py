import re
entrada = input('Ingresa nombre de archivo: ')
man = open(entrada)
total = 0
contador = 0
for linea in man:
    x = re.findall('New Revision: ([0-9]+)', linea)
    if len(x) > 0:
        numero = int(x[0])
        total += numero
        contador += 1
        print(x)

print(total / contador)
