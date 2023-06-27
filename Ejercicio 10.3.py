entrada = input('Ingrese un nombre de archivo: ')
man = open(entrada)
d = dict()
for linea in man :
    linea = linea.lower()
    for letra in linea :
        if letra >= 'a' and letra <= 'z' :
            d[letra] = d.get(letra, 0) + 1

t = []
for clave, valor in d.items() :
    t.append((valor, clave))

t.sort(reverse = True)

for x, y in t :
    print(x, y)
