vel = float(input('Digite a velocidade da internet em Mbps: '))

if vel <= 10:
    print('Basica')
elif vel <= 100 and vel > 10:
    print('Moderna')
elif vel > 100:
    print('Ultra Fibra')