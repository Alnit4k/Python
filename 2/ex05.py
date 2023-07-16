nota1= float(input('NOTA 1 : '))
nota2= float(input('NOTA 2 : '))

media = (nota1+nota2)/2

if media == 10:
    print('Aprovado com distinção')
    
elif media <= 6:
    print('Reprovado')
    
elif media >= 7:
    print('Aprovado')
