# Para ejecutar este programa descarga BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# O descarga el archivo
# http://www.py4e.com/code3/bs4.zip
# y descomprimelo en el mismo directorio que este archivo

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduzca página: ')
html = urllib.request.urlopen(url, context=ctx).read()
sopa = BeautifulSoup(html, 'html.parser')
contador = 0

# Recuperar todas las etiquetas de párrafo
etiquetas = sopa('p')
for etiqueta in etiquetas:
    contador += 1

print('Total de párrafos:', contador)
