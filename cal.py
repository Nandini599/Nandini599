def calculator():
    print("Welcome to the Simple Calculator!")
    
    # Get user input for the first number
    num1 = float(input("Enter the first number: "))
    
    # Get user input for the second number
    num2 = float(input("Enter the second number: "))
    
    # Display operation choices
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user choice for operation
    operation = input("Enter the operation (1/2/3/4): ")
    
    # Perform the calculation based on user choice
    if operation == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    calculator()
