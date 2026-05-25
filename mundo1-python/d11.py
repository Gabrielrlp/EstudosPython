n = int(input('Digite um numero para receber sua tabuada: '))

n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10

print(
    f'Tabuada do {n}:\n'
    f'{n} x 1 = {n1}\n'
    f'{n} x 2 = {n2}\n'
    f'{n} x 3 = {n3}\n'
    f'{n} x 4 = {n4}\n'
    f'{n} x 5 = {n5}\n'
    f'{n} x 6 = {n6}\n'
    f'{n} x 7 = {n7}\n'
    f'{n} x 8 = {n8}\n'
    f'{n} x 9 = {n9}\n'
    f'{n} x 10 = {n10}'
)

ext = int(input('O numero é maior que 10? Entao digite aqui o numero: '))
ext2 = int(input('Digite o multiplicador do numero: '))

resul = ext * ext2

print('O resultaado é:', resul)