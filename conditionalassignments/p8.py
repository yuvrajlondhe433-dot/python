age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))

if age >= 18 and age <= 65 and weight >= 50:
    print("Basic criteria met")
else:
    print("Basic criteria not met")
