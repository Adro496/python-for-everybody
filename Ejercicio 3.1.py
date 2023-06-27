horas = int(input('Introduzca horas: '))
tarifa = int(input('Introduzca tarifa: '))
if horas <= 40 :
    salario = horas*tarifa
else :
    salario = 40*tarifa+1.5*tarifa*(horas-40)

print('Salario: ' + str(salario))
