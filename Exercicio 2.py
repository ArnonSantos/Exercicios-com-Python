s = float (input ("Digite o seu salário bruto: "))
p = float (input ("Digite o valor da parcela do emprestimo: "))
if (p > (s * 20)/100):
    print ("Não será possivel conceder o seu emprestimo")
elif (p < (s * 20)/100):
    print ("Seu emprestimo será aprovado")
