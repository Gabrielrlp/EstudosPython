# Desenvolva um script para uma loja de veículos: pergunte se o cliente quer comprar um carro ou uma moto. Se for carro, pergunte se prefere Sedan ou Hatch. Se for moto, pergunte se prefere Street ou Trail. Exiba a resposta final do modelo escolhido.

print('Bem vindo a minha loja de veiculos!')
modelo = int(input('Digite 1 se deseja um carro\nDigite 2 se deseja uma moto\n'))

if modelo == 1:
    typecarro = int(input('Digite 1 para prefencia na marca Sedan\nDigite 2 para preferencia em Hatch\n'))
    if typecarro == 1:
        print('Certo! sua escolha foi um Carro da marca Sedan.')
    elif typecarro == 2:
        print('Certo! sua escolha foi um Carro da marca Hatch.')
    elif typecarro < 1 or typecarro > 2:
        print('Não há opcoes com esse numero')
elif modelo == 2:
    typemoto = int(input('Digite 1 para prefencia na marca Street\nDigite 2 para preferencia em Trail\n'))
    if typemoto == 1:
        print('Certo! sua escolha foi uma moto da marca Street.')
    elif typemoto == 2:
        print('Certo! sua escolha foi uma moto da marca Trail.')
    elif typemoto < 1 or typemoto > 2:
        print('Não há opcoes com esse numero')
elif modelo < 1 or modelo > 2:
    print('Não há opcoes com esse numero')