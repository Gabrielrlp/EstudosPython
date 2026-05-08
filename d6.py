#exercicio calculando  media de ota anual

nome = input('Qual seu nome? ')
n1 = float(input('Digite a nota do primeiro bimestre: '))
n2 = float(input('Digite a nota do segundo bimestre: '))
n3 = float(input('Digite a nota do terceiro bimestre: '))
n4 = float(input('Digite a nota do quarto bimestre: '))

soma = n1 + n2 + n3 + n4
media = soma / 4

if(media >= 15):
    situacao = 'Aprovado'
else:   
    situacao = 'Reprovado'

print(
    f'Nome: {nome}\n'
    f'media {media}\n'
    f'Situação: {situacao}'
)