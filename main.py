# Simple Calculator in Python

print("=== Simple Calculator ===")

# Ask the user for two numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Show menu of operations
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Power (^)")

choice = input("Your choice (1/2/3/4/5): ")

# Perform the calculation
if choice == "1":
    print("Result:", a + b)
elif choice == "2":
    print("Result:", a - b)
elif choice == "3":
    print("Result:", a * b)
elif choice == "4":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero ")
elif choice == "5":
    print("Result:", a ** b )        
else:
    print("Invalid choice ")
