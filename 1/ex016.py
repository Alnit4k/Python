size = float(input('Qual o tamanho da parede em m³? '))
litro = (1*size)/(3*1)
latas = round((litro/18)+0.5)
gasto = latas*80.00

if litro <= 18:
        print('Você só vai precisar 1 lata')
else:
    print(f'Você vai precisar usar {latas} latas o gasto vai ser de R${gasto}')