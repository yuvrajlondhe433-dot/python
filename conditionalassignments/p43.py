status = input("Enter result status (pass, fail, absent): ").lower()

match status:
    case "pass":
        print("Congratulations! You passed.")
    case "fail":
        print("You failed. Please try again.")
    case "absent":
        print("You were absent for the exam.")
    case _:
        print("Invalid result status")
