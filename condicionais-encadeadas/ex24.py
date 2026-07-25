# Crie um validador de cupons de frete grátis. Primeiro veja se o valor total da compra é maior que R$100. Se for, pergunte o estado do cliente. Se o estado for "SP", o frete é grátis. Se não for de "SP", informe que o frete grátis não se aplica àquela região geográfica.

compra = float(input('Digite o valor total da compra: '))

if compra > 100:
    estado = str(input('Digite a sigla do seu estado: '))
    if estado == 'SP' or estado == 'sp':
        print('O seu frete é gratis!')
    else:
        print('Apesar de sua compra ser mais que 100 reais, seu frete não é gratis')
else:
    print('O frete não é gratis')