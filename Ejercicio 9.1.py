manejador = open('words.txt')
diccionario = dict()
for linea in manejador :
    palabras = linea.split()
    for palabra in palabras :
        diccionario[palabra] = 'No importo :/'

entrada = input('Introduzca una palabra: ')
print(entrada in diccionario)
#print(diccionario)
