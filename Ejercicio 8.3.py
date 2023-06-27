manejador = open('Ejercicio 8.2.txt')
contador = 0
for linea in manejador:
    palabras = linea.split()
    # print 'Depuración:', palabras
    if palabras[0] != 'From' or len(palabras) < 3 : continue
    print(palabras[2])
