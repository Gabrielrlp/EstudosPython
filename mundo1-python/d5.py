a = input('Digite algo: ')

# esse aqui serve para saber o tipo, stringe(str), inteiro(int), decimal(float) ou boleano (boll) 
print('O tipo primitivo é ', type(a))

# esse aqui serve para saber se ha espaços nas palavras
print('Só tem espaços? ', a.isspace())

# esse aqui serve para saber se é feito somente com numeros
print('é um numero? ', a.isnumeric())

# esse aqui serve para saber se é letras
print('é alfabetico? ', a.isalpha())

# esse aqui serve para saber se é alfanumerico
print('é alfanumerico? ', a.isalnum())

# esse aqui serve para saber se é letras maiusculas
print('Esta em maiusculas? ', a.isupper())

# esse aqui serve para saber se é letras minusculas
print('Esta em minusculas? ', a.islower())

# esse aqui serve para saber se é uma palavra capitalizada
print('Esta capitalizada? ', a.istitle())