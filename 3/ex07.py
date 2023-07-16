highest_number = float()

for i in range (5):
    number = int(input('Enter number {}' .format(i+1)))
    if number > highest_number: #Basically the function will replace the number whenever it is added
        highest_number = number