narchivo = input('Ingresa un nombre de archivo: ')
if narchivo == 'na na boo boo' :
    print('NA NA BOO BOO PARA TI - ¡Te he atrapado!')
    exit()
try:
    man_a = open(narchivo)
except:
    print('No se puede abrir el archivo:', narchivo)
    exit()
contador = 0
for linea in man_a:
    if linea.startswith('Subject:'):
        contador = contador + 1
print('Hay', contador, 'líneas de asunto (subject) en', narchivo)
