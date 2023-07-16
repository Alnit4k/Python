a, b = 0, 1 

print (a)
print (b)

for i in range(9):
    next_term = a + b 
    
    a,b = b, next_term
    
    print(next_term)