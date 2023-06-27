import socket

entrada = input('Ingrese URL: ')
host = entrada.split('/')
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    misock.connect((host[0], 80))
except:
    print('Página inexistente, comprobar URL')
    exit()
cmd = ('GET http://' + entrada + ' HTTP/1.0\r\n\r\n').encode()
misock.send(cmd)
contador = 0
archivo = b''

while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    contador = contador + len(datos)
    archivo = archivo + datos
    if not contador > 3000:
        print(datos.decode(), end = '')
        continue
    if contador - len(datos) < 3000:
        diferencia = 3000 - (contador - len(datos))
        print(datos.decode()[:diferencia], end = '')

misock.close()

if len(archivo) < 3000:
    if archivo[-1] == '\n':
        print('Caracteres totales:', contador)
    else:
        print('\nCaracteres totales:', contador)
else:
    if archivo[2999] == '\n':
        print('\nCaracteres totales:', contador)
    else:
        print('\n\nCaracteres totales:', contador)

#Revisar la consigna, esto podría estar mal.
