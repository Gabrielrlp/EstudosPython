# Leia o nome, número de horas trabalhadas e o número de dependentes de um funcionário. Após a leitura, escreva qual o Nome, salário bruto, os valores descontados para cada tipo de imposto e finalmente qual o salário líquido do funcionário. Considerando que:
# a) A empresa paga $12 por hora e $40 por dependentes.
# b) Sobre o salário são descontados 8,5% p/ o INSS e 5% p/ IR

nome = str(input('Digite o seu nome: '))
horas = int(input('Digite a quantidade de horas trabalhadas: '))
ndependentes = int(input('Digite o numero de dependentes: '))

salarioH = horas * 12
salarioD = ndependentes * 40
salariobruto = salarioH + salarioD

desconto1 = salariobruto * 8.5 / 100
desconto2 = salariobruto * 5 / 100

dtotal = desconto1 + desconto2
salarioliquido = salariobruto - dtotal

print(f'\nSeu nome é: {nome}\n'
      f'Seu salario bruto é: {salariobruto}\n'
      f'O desconto do INSS é: {desconto1}\n'
      f'O desconto do IR é {desconto2}\n'
      f'Seu salario liquido é: {salarioliquido}'
)