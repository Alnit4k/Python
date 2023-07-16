def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mult(a, b):
    return a * b

def exp(a):
    return a ** 2

def recall_memory(memory):
    print('Memory:', memory)

memory = 0

while True:
    print("\nWhat operation do you want to perform?\n")
    print("Enter '+' to sum")
    print("Enter '-' to subtract")
    print("Enter '/' to divide")
    print("Enter '*' to multiply")
    print("Enter 'R' to recall memory")
    print("Enter 'Q' to quit")

    choice = input().upper()

    if choice == '+':
        a = float(input('Enter a number: '))
        result = sum(memory, a)
        memory = result
        print('Accumulator:', result)
    elif choice == '-':
        a = float(input('Enter a number: '))
        result = sub(memory, a)
        memory = result
        print('Accumulator:', result)
    elif choice == '/':
        a = float(input('Enter a number: '))
        result = div(memory, a)
        memory = result
        print('Accumulator:', result)
    elif choice == '*':
        a = float(input('Enter a number: '))
        result = mult(memory, a)
        memory = result
        print('Accumulator:', result)
    elif choice == 'R':
        recall_memory(memory)
    elif choice == 'Q':
        break
    else:
        print("Invalid choice. Please try again.")

