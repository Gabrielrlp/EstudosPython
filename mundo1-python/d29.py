import random

num = random.randint(0, 5)

print('-=-' * 20)
num1 = int(input('Tente acertar o numero de 0 a 5: '))
print('-=-' * 20)
if num == num1:
    print('Voce acertou!')
else:
    print('Voce errou.')