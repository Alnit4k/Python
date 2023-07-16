num1 = int(input('Escreva o primeiro numero: '))
num2 = int(input('Escreva o segundo numero: '))
num3 = int(input('Escreva o terceiro numero: '))

maior = num1

if num2 > maior:
    maior= num2 
if num3 > maior:
    maior= num3 
        
print(maior)