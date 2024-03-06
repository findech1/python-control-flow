#Python program for basic arithmetic operations:
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Test the functions
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Sum:", add_numbers(num1, num2))
print("Difference:", subtract_numbers(num1, num2))
print("Product:", multiply_numbers(num1, num2))
print("Quotient:", divide_numbers(num1, num2))
