entrada = input('Ingresar nombre de archivo: ')
manejador = open(entrada)
palabras_distintas = []
for linea in manejador :
    palabras = linea.split()
    for palabra in palabras :
        if (palabra in palabras_distintas) == True : continue
        palabras_distintas = palabras_distintas + [palabra]
        #Supuestamente, debería haberlo hecho con el método append
palabras_distintas.sort()
print(palabras_distintas)
