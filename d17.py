km = float(input('Quantos Km você rodou com o carro? '))
dias = int(input('Quantos Dias vc alugou o carro? '))

resul = km * 0.15
resul2 = dias * 60

total = resul + resul2

print(
    f'O valor a ser pagado por Km rodado é: {resul}R$\n'
    f'O valor a ser pagado de aluguel é: {resul2}R$\n'
    f'O valor total é: {total}R$'
)