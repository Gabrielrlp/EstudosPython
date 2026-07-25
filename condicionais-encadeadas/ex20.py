dia = int(input("Digite um numero para receber o dia da semana correspondente: "))

if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda')
elif dia == 3:
    print('Terça')
elif dia == 4:
    print('Quarta')
elif dia == 5:
    print('Quinta')
elif dia == 6:
    print('Sexta')
elif dia == 7:
    print('Sabado')
elif dia < 1 or dia > 7:
    print('Numero não aceito')