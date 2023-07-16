num1 = int(input("Enter a number --> "))
num2 = int(input("Enter another number --> "))

if num2 < num1:
    num1, num2 = num2, num1 #Swap position if num2 is less than num1


for i in range(num1, num2, 1):
    print(i)
