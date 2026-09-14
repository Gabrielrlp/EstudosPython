# Leia o preço de um produto e o percentual de desconto. Calcule o valor do desconto e o preço final do
# produto

preco = float(input('Digite o preço do produto: '))
perc = int(input('Digite o percentual de deesconto: '))

desc = (preco / 100) * perc

resul = preco - desc

print('O valor com {}% de desconto é: {}'.format(perc, resul))