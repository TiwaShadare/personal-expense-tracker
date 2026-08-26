expenses = []


def add_expense():
    name = input("Enter expense name: ")
    
    try:
        amount = float(input("Enter amount: $"))
    except ValueError:
        print("Please enter a valid amount.")
        return

    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("\nExpense added successfully!")


def view_expenses():
    if not expenses:
        print("\nNo expenses have been added yet.")
        return

    print("\nYour Expenses")
    print("-" * 45)

    for expense in expenses:
        print(
            f"{expense['name']:<20}"
            f"${expense['amount']:>8.2f}   "
            f"{expense['category']}"
        )

    print("-" * 45)


def view_total():
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal spending: ${total:.2f}")


def main():
    while True:
        print("\n==============================")
        print("      PERSONAL EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            view_total()

        elif choice == "4":
            print("\nThank you for using the Expense Tracker!")
            break

        else:
            print("\nInvalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
