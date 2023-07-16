size = float(input('Quantos metros quadrados? '))

qnt_latas = round((size/6)/18)
qnt_galoes = round((size/6)/3.6)

sobra18 = (size/6)-18

resto = size%6


if size <=108 :
    print(f'Você precisa comprar apenas uma lata de 18L no final da pintura sobrara {cal2}L')
    print(f'Ou também pode comprar {qnt_galoes} galões de 3.6L')
else:
    print(f'Você precisara comprar {qnt_latas} latas de 18L')
    print(f'Ou também pode comprar {qnt_galoes} galões de 3.6L')
    
if el <= 1:

    print('A opção mais barata é comprar uma lata de 3.6L')
elif el < 1 and el >= 3:
    
    print ('A melhor opção é comprar 3 latas de 3.6L')
elif resto >= 3:
    
     
