#Implementando bibliotecas necessarias para multiplicação
from functools import reduce
from operator import mul

nums = []

for i in range (5):
    num = int(input('insira o {}° numero: ' .format(i+1)))
    nums.append(num)

#fazendo a redução da multiplicação 
produto = 1

for numero in nums:
    produto *= numero

   
print(nums)#Os numeros usados
print(sum(nums))#A soma deles
print(produto)#O resultado da multiplicação
