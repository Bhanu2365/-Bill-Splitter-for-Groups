def split_bill():
    try:
        total_bill = float(input("Enter the total bill amount: $"))
        num_people = int(input("Enter the number of people: "))

        if num_people <= 0:
            print("Number of people must be greater than 0.")
            return

        amount_per_person = total_bill / num_people
        print(f"Each person should pay: ${amount_per_person:.2f}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Run the function
split_bill()
