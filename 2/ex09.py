n1 = int(input('Digete o primeiro numero: '))
n2 = int(input('Digete o segundo numero: '))
n3 = int(input('Digete o terceiro numero: '))
n4 = int(input('Digete o quarto numero: '))

if n4 < n3:
    aux = n4
    n4 = n3
    n3 = aux   
  

if n3 < n2 :
    aux = n3
    n3 = n2
    n2 = aux
    

if n2 < n1:
    aux = n2
    n2 = n1
    n1 = aux 



if n4 < n3:
    aux = n4
    n4 = n3
    n3 = aux  

if n3 < n2 :
    aux = n3
    n3 = n2
    n2 = aux

     

print(n1, n2, n3, n4)
    