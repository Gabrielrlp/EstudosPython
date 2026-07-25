# Um aplicativo de entrega precisa taxar pedidos. Pergunte se o pedido é feito em dia de semana ou final de semana. Se for final de semana, pergunte se está chovendo. Se estiver chovendo, adicione uma taxa extra de R$10.00. Se não estiver chovendo, a taxa é de apenas R$5.00.

dia = int(input('Digite 1 para entrega de segunda a sexta\nDigite 2 para entrega em fins de semana \n'))

if dia == 2:
    chuva = str(input('Esta chovendo? '))
    if chuva == 'sim' or chuva == 'Sim' or chuva == 'SIM':
        print('Seu frete é 10 reais')
    else:
        print('Seu frete é de 5 reais')
else:
    print('Seu frete é de 5 reais')