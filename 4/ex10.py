a = []
b = []

for i in range(3):
    valA = int(input('Enter the {}st number: '.format(i+1)))
    valB = int(input('Enter another number: '))
    a.append(valA)
    b.append(valB)

#setA = set(a)
#setB = set(b)

c =  a + b #Interleaved lists

print("List A:", a)
print("List B:", b)
print("Intersection:", c)

print(a)
print(b)
print(c)