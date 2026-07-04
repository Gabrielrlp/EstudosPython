nota = float(input('Digite sua nota: '))

if nota >= 9:
    print('A')
elif nota >= 7 and nota < 9:
    print('B')
elif nota >= 5 and nota < 7:
    print('C')
elif nota < 5:
    print('D')