vel = int(input('Digite a velocidade do carro em Km: '))

if vel >= 81:
    print('Voce foi multado!')
    mul = vel * 7
    print('A multa foi de {}R$'.format(mul))
else:
    print('Voce estava na velocidade permitida, continue assim!')