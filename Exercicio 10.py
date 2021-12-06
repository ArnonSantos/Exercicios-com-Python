p1 = str(input('Qual o seu produto? '))
v1 = float (input('Digite o valor do produto: '))
q1 = int(input ('Digite a quantidade do produto: '))

p2 = str(input('Qual o seu produto? '))
v2 = float (input('Digite o valor do produto: '))
q2 = int(input ('Digite a quantidade do produto: '))

p3 = str(input('Qual o seu produto? '))
v3 = float (input('Digite o valor do produto: '))
q3 = int(input ('Digite a quantidade do produto: '))

total = ((v1 * q1) + (v2 * q2) + (v3 * q3))
print (total)

pagamento = float(input('Digite quanto irá pagar: '))
if (pagamento > total):
    print ("Seu troco é de: ", pagamento - total)
elif (pagamento < total):
    print ("Saldo insuficiente")
elif (pagamento):
    print ('Pagamento efetuado')
