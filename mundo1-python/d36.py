# (a + b > c)
#(a + c > b)
#(b + c > a)

r1 = float(input("Digite o tamanho da primeira reta em metros: "))
r2 = float(input("Digite o tamanho da segunda reta em metros: "))
r3 = float(input("Digite o tamanho da terceira reta em metros: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("È possivel criar um triangulo com essas 3 retas!")
else:
    print("Não é possivel criar um triangulo")