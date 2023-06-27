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

while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(),end='')

misock.close()
