try:
    ent1 = input('Introduzca horas: ')
    horas = float(ent1)
    ent2 = input('Introduzca tarifa: ')
    tarifa = float(ent2)
    def calculo_salario(horas, tarifa):
        if horas <= 40:
            salario = horas * tarifa
        else:
            salario = 40 * tarifa + 1.5 * tarifa * (horas - 40)
        return salario

    print('Salario: ' + str(calculo_salario(horas, tarifa)))
except:
    print('Error, por favor introduzca un número.')
