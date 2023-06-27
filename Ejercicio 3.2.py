try:
    ent1 = input('Introduzca horas: ')
    horas = int(ent1)
    ent2 = input('Introduzca tarifa: ')
    tarifa = int(ent2)
    if horas <= 40 :
        salario = horas*tarifa
    else :
        salario = 40*tarifa+1.5*tarifa*(horas-40)

    print('Salario: ' + str(salario))
except:
    print('Error, por favor introduzca un número.')
