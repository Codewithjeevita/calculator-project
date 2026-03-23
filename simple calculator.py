print("====== SIMPLE CALCULATOR ======")

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Thank you for using the calculator! 👋")
        break

    if choice in ["1", "2", "3", "4"]:
        a = float(input("Enter your 1st number: "))
        b = float(input("Enter your 2nd number: "))

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
                print("Error: Cannot divide by zero!")

    else:
        print("Invalid choice! Please select between 1 to 5.")