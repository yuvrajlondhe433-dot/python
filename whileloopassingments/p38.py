while True:
    print("\n--- MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Program ended.")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Addition =", a + b)

    elif choice == 2:
        print("Subtraction =", a - b)

    elif choice == 3:
        print("Multiplication =", a * b)

    elif choice == 4:
        if b != 0:
            print("Division =", a / b)
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid choice")
