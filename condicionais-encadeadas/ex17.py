peso = float(input('Digite o peso do lutador: '))

if peso <= 65:
    print('Peso pena')
elif peso > 65 and peso <= 80:
    print('Peso medio')
elif peso > 81:
    print('Peso Pesado')