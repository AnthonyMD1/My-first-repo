def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
while True:        
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    choice = int(input("Enter your choice (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): "))
    if choice == 1:
        result = add(num1, num2)
        print(f"the sum of {num1} and {num2} is: {result}")
    elif choice == 2:
        result = subtract(num1, num2)
        print(f"the difference of {num1} and {num2} is: {result}")
    elif choice == 3:
        result = multiply(num1, num2)
        print(f"the product of {num1} and {num2} is: {result}")
    elif choice == 4:   
        result = divide(num1, num2)
        print(f"the quotient of {num1} and {num2} is: {result}")
    else:
        print("Invalid choice.")
    