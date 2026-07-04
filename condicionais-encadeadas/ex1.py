nome = str(input('Digite seu nome: '))

idade = int(input('Digite sua idade: '))

salario = float(input('Digite seu salario: '))

salario = salario + salario/100 * 12

print(
    f'\nSeu nome é: {nome}\n'
    f'Vc tem {idade} anos de idade\n'
    f'Seu salario com 12% de aumento é: {salario}'
)