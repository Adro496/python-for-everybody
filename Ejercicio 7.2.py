entrada = input('Ingresa un nombre de archivo: ')
manejador = open(entrada)
contador = 0
suma = 0
for linea in manejador :
    if linea.find('X-DSPAM-Confidence: ') == -1 : continue
    contador = contador + 1
    str_valor = linea[20:]
    valor = float(str_valor)
    suma = suma + valor

print('Promedio spam confidence:', suma / contador)
