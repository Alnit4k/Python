sal = float(input('Qual seu salario? '))

if sal <= 280.00:    
    sal = (sal*0.20)+ sal
    print(f'Seu novo salario é {sal}')    

elif sal > 281.00  and sal <= 700.00  :
    sal = (sal*0.15)+ sal
    print(sal)
    
elif sal <= 1500.00 and sal >700.00:
    sal = (sal*0.10)+ sal
    print(sal)

elif sal >= 1500.01:
    sal = (sal*0.05)+ sal
    print(sal)
    
    