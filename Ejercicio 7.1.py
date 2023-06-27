entrada = input('Ingresa un nombre de archivo: ')
manejador = open(entrada)

for lx in manejador :
    ly = lx.rstrip()
    print(ly.upper())

# entrada = input('Ingresa un nombre de archivo: ')
# manejador = open(entrada)
# archivo = manejador.read()
# print(archivo.upper())
