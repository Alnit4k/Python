vetor = []
pares = []
impares = []

for i in range(5):
    num = int(input('Digite o {}° numeoro ' .format(i+1)))
    vetor.append(num)
   

for num in vetor:
    if num % 2 ==0:
        pares.append(num)
    else:
        impares.append(num)
    
print(vetor)
print(pares)
print(impares)