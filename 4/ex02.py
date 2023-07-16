import random

lista=[]

for i in range(10):
    lista.append(input('Numero '+ str(i+1) + ':\n'))

lista.reverse()
print (lista)