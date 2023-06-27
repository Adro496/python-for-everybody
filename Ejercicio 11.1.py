import re
entrada = input('Ingresa una expresión regular: ')
man = open('mbox.txt')
contador = 0
for linea in man:
    linea = linea.rstrip()
    if re.search(entrada, linea):
        contador += 1

print('mbox.txt tiene', contador, 'líneas que coinciden con', entrada)
