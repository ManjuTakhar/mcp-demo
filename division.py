# Python program to perform division operation

def divide_numbers(a, b):
    if b == 0:
        return 'Division by zero is not allowed'
    return a / b

result = divide_numbers(10, 2)
print('Result of division:', result)