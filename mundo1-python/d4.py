n1 = int(input('Digite um numero: '))

n2 = int(input('Digite outro numero: '))

n3 = n1 + n2

# dua formas diferentes de fazer a mesma coisa, mas o .format é mais facil

#print('A soma de', n1, 'mais', n2, 'é:', n3)

print('A soma de {0} com {1} é igual a {2}'.format(n1,n2,n3))