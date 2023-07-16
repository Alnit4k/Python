import random

nums = []

while True:
    
    random.seed()
    numbers = random.sample(range(10), k=5) 
    
    numbers.append(nums)      
       
    lower_number = nums
    for num in nums:
        if num < lower_number:
        
            print(f"The lower number is {lower_number}")
    
    higger_number = nums
    for num in nums:
        if num > higger_number:
            
            print(f"The lower number is {higger_number}")
            
    sum = 0
    for num in nums:
        sum += num 
        
    print(f"The sum of numbers is {sum}")
        
        
        