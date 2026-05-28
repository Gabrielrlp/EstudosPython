# teste 1

tempo = int(input('Quantos anos tem seu carro? '))

if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('---FIM---')

# teste 2

nome = str(input('Qual é seu nome? '))

if nome == 'Gustavo':
    print('Que nome lindo voce tem!')
else:
    print('Seu nome é tao normal!')
print('Bom dia, {}'.format(nome))

# teste 3

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite sua seguda nota: '))

m = (n1 + n2)/2
print('A sua media foi {}'.format(m))

if m >= 6.0:
    print('Voce tirou azul')
else:
    print('Voce tirou vermelho')