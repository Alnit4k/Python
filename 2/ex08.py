p1 = float(input('Qual o preço do primeiro produto? '))
p2 = float(input('Qual o preço do segundo produto? '))
p3 = float(input('Qual o preço do terceiro produto? '))

menor = p1

if p2 < menor:
    menor = p2
if p3 < menor:
    menor = p3
    
print(menor)