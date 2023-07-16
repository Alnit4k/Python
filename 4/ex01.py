import random
#Usamos o import random para importar a propiedade append

listaNumeros = []
print ('Informe os 5 numeros')

for o in range(5):
    listaNumeros.append(input('Numero '+ str(o+1) + ':\n'))
    #O append serve para adicionarmos alguma informação a lista
    #O str i+1 seria para adcionarmos outro numeral até o termino da estrutura de repetição
    
print (listaNumeros) 