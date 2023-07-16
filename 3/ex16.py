a, b = 0, 1

print (a)
print(b)

while True:
    next_term = a + b
    
    if next_term > 500:
        break
    print(next_term)
    a, b = b, next_term
