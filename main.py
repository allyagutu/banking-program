def print_border():
    print("*********************")

def show_balance(balance):
    print_border()
    print(f"Your balance is ${balance:.2f}")
    print_border()

def deposit():
    print_border()
    try:
        amount = float(input("Enter an amount to be deposited: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        print_border()
        return 0
    print_border()

    if amount <= 0:
        print_border()
        print("That's not a valid amount")
        print_border()
        return 0
    else:
        return amount

def withdraw(balance):
    print_border()
    try:
        amount = float(input("Enter amount to be withdrawn: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        print_border()
        return 0
    print_border()

    if amount > balance:
        print_border()
        print("Insufficient funds")
        print_border()
        return 0
    elif amount <= 0:
        print_border()
        print("Amount must be greater than 0")
        print_border()
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print_border()
        print("     banking program     ")
        print_border()
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print_border()

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print_border()
            print("That is not a valid choice")
            print_border()

    print_border()
    print("Thank you! Have a nice day")
    print_border()

if __name__ == "__main__":
    main()
