# Faça um programa que leia o login de um usuário. Se o login for válido, peça a senha. Se a senha também for correta, dê as boas-vindas. Mostre erros específicos para cada etapa caso o usuário falhe.

usuario = 'Gabriel'
senha = 1234

usuario = str(input('Qual o nome de usuario? '))
if usuario == usuario:
    print('O usuario esta correto!')
else:
    print('Usuario incorreto.')

senha = int(input('Digite a senha de usuario: '))

if senha == senha:
    print('login feito com suesso! boas vindas')
else:
    print('Senha incorreta, tente novamente')