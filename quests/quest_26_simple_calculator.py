def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()

if operation == "add":
    result = add(num1, num2)
    print(f"The result is: {result}")
elif operation == "subtract":
    result = subtract(num1, num2)
    print(f"The result is: {result}")
elif operation == "multiply":
    result = multiply(num1, num2)
    print(f"The result is: {result}")
elif operation == "divide":
    result = divide(num1, num2)
    print(f"The result is: {result}")
else:
    print("Technical Wrong Doing! Please choose add, subtract, multiply, or divide.")
