counter1 = 0
counter2 = 0

for i in range (10):
    num= int(input(f"Enter {i+1}° number --> " ))
    
    if num % 2 == 0:
        counter1 += 1       
       
        
    if num % 2 != 0:
        counter2 += 1
        
        
print (f"The number of even numbers is {counter1}")
print (f"The number of odd numbers is {counter2}")