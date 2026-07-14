valor = float(input('Digite o valor a ser calculado o desconto: '))

desconto = int(input('Digite 1 para: Dinheiro (15% de desconto)\nDigite 2 para: Cartão de Crédito (Preço Normal)\nDigite 3 para: Pix (10% de desconto) '))

if desconto == 1:
    valor = valor - valor / 100 * 15
    print('\nCom desconto no dinheiro: ', valor)
elif desconto == 2:
    print('\nNo credito náo há desconto: ', valor)
elif desconto == 3:
    valor = valor - valor / 100 * 10
    print('\nCom desconto no pix: ', valor)
elif desconto != 1 and desconto != 2 and desconto != 3:
    print('Opção invalida')