n1 = int(input("Digite a distancia da sua viagem: "))

if n1 >= 200:
    n2 = n1 / 0.45
    print("O valor é: {:.2f}R$".format(n2))
else:
    n3 = n1 / 0.50
    print("O valor é : {:.2f}R$".format(n3))
