usuario = str(input('Digite um nome de usuario valido e existente: '))

senha = int(input('Digite uma senha valida e existente: '))

# usuario = 'admin'

# senha = 12345

if senha == 12345 and usuario == 'admin':
    print('Acesso realizado!')
else:
    print('Acesso negado.')