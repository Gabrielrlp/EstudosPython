n1 = float(input('Quanto é para completar o tanque? '))

n2 = float(input('Quanto de dinheiro vc tem? '))

if n2 >= n1:
    print('Abastecimento autorizado!')
else:
    print('Saldo Insuficiente')
    