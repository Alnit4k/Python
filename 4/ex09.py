a = [] #List with sum only
b = [] #List with numbers used



for i in range(10):
    nums = int(input('{}st number: ' .format(i+1)))
    b.append(nums)
    expo = nums**2
    a.append(expo)
    
print(sum(a))   
print(a)
print(b)   

