print('Olá, vamos calcular seu consumo de mensal de energia eletrica em KWh')
cm = float(input('Insira seu consumo mensal de energia: '))
if(cm < 100):
    print ('Seu consumo é de: ', cm * 0.90, 'reais')
if(cm > 100):
    print ('Seu consumo é de: ', cm * 1.874, 'reais')
if(cm == 100):
    print ('Seu consumo é de: ', cm * 0.90, 'reais')
