balance = 5000

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Available balance: Rs.", balance)

    case 2:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Deposited successfully")
            print("New balance: Rs.", balance)
        else:
            print("Invalid deposit amount")

    case 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount <= balance:
            balance -= amount
            print("Withdrawal successful")
            print("Remaining balance: Rs.", balance)
        else:
            print("Insufficient balance")

    case 4:
        print("Thank you for using the ATM")

    case _:
        print("Invalid choice")
