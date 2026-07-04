nota1 = float(input('Digite a primeira nota: '))

mediaP1 = int(input('Digite o peso 1: '))

nota2 = float(input('Digite a segunda nota: '))

mediaP2 = int(input('Digite o peso 2: '))

total = nota1 * mediaP1 + nota2 * mediaP2
pesototal = mediaP1 + mediaP2
result = total / pesototal

print(f'A media ponderada é:', result)