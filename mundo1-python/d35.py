salario = float(input("Digite o seu salario: "))

if salario > 1250:
    salario = salario + (salario / 100 * 10)
    print("Seu salario com aumento é:", salario)
else:
    salario = salario + (salario / 100 * 15)
    print("Seu salario com aumento é:", salario)