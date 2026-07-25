# Crie um sistema de processo seletivo. Primeiro, verifique se o candidato possui formação na área de TI. Se tiver, pergunte quantos anos de experiência ele possui. Se for maior que 2 anos, exiba "Candidato Avança para Entrevista", senão "Candidato para Banco de Talentos". Se não tiver formação, printe "Perfil incompatível".

formacao = int(input('Voce tem formação em TI? \nCaso sim digite: 1\nCaso não digite: 2\n'))

if formacao == 1:
    experiencia = int(input('Quantos anos de experiencia vc tem? '))
    if experiencia > 2:
        print('Candidato Avança para Entrevista')
    else:
        print('Candidato para Banco de Talentos')


if formacao == 2:
    print('Perfil incompatível')
elif formacao < 1 or formacao > 2:
    print('Numeros diferentes de 1 e 2')