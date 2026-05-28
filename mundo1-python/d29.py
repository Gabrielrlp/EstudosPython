import random

num = random.randint(0, 5)

# teste 
print(num)

num1 = int(input('Tente acertar o numero de 0 a 5: '))
if num == num1:
    print('Voce acertou!')
else:
    print('Voce errou.')