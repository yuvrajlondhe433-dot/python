username = input("Enter username: ")

if username == "admin":
    password = input("Enter password: ")

    if password == "admin123":
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")
