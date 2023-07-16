mult_result= 0
num=int(input("Enter a number --> "))
print('Multiplication table')

for i in range(11):  
    mult_result = i * num  
 
    print(f"5 x {i} = {mult_result}" .format(i+1))