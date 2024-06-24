# Simple Calculator App in Python

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

# Main function to run the calculator
def main():
    print("Welcome to Simple Calculator App!")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Take user input for operation choice
    choice = input("Enter your choice (1/2/3/4): ")
    
    # Take user input for two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = 0
    
    # Perform the selected operation
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    else:
        print("Invalid input. Please enter a valid operation choice (1/2/3/4).")
        return
    
    # Display the result
    print(f"Result: {result}")

# Run the calculator
if __name__ == "__main__":
    main()
