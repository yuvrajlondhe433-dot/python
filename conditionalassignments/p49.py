age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))

if age >= 21:
    if salary >= 25000:
        print("Eligible to apply for a loan")
    else:
        print("Salary is insufficient")
else:
    print("Age requirement not met")
