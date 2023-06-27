str = 'X-DSPAM-Confidence:0.8475'
dospuntospos = str.find(':')
numero = str[dospuntospos + 1:]
numerof = float(numero)
print(numerof,type(numerof))
