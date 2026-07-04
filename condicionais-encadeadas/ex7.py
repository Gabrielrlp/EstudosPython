distancia = float(input('Digite a distancia em Km que o carro ira percorrer: '))
preco = float(input('Digite o valor do litro da gasolina em real: '))

kml = 12

litros = distancia / kml

gasto = litros * preco

print(
    f'\nO carro ira consumir {litros:.2f}L de combustivel\n'
    f'O carro ira gastar {gasto:.2f}R$ de gasolina'
)