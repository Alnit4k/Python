lista=[]

for nota in range(4):
    lista.append(input('Nota ' + str(nota + 1) + ':\n'))
    
soma=sum(lista)
qtd=len(lista)

media=soma/qtd

print(media)
