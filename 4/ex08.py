age = []
height = []

for i in range (5):
    a = int(input('Age of {}st person: ' .format(i+1)))
    h = int(input('Height of {}st person in cm: ' .format(i+1)))
    age.append(a)
    height.append(h)
    
    
print(age)
print(height)

#Inverting the list
age.reverse()
height.reverse()

print(age)
print(height)