
while True:
    t = str(input('Qual turno você trabalha? \n Digite:\n M para matuino\n V para vespertino\n N para noturno\n')).upper()
    
    if t == 'M':
        print('Bom dia!')
        
    elif t == 'V':
        print('Boa tarde!')
    elif t== 'N':
        print('Boa noite')
    else:
        print('Opção invalida!!!\n FAVOR DIGITAR OPÇÕES ABAIXO')