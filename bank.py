accounts = {}


def create_account():
    account_no = input("Enter account number: ")
    balance = int(input("Enter initial balance: "))
    accounts[account_no] = balance
    print("Account created successfully.")


def deposit():
    account_no = input("Enter account number: ")
    if account_no in accounts:
        amount = int(input("Enter amount to deposit: "))
        accounts[account_no] += amount
        print("Deposit successful.")
    else:
        print("Account not found.")


def withdraw():
    account_no = input("Enter account number: ")
    if account_no in accounts:
        amount = int(input("Enter amount to withdraw: "))
        if accounts[account_no] >= amount:
            accounts[account_no] -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")


def check_balance():
    account_no = input("Enter account number: ")
    if account_no in accounts:
        print("Account balance:", accounts[account_no])
    else:
        print("Account not found.")


while True:
    print("Options:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("0. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        create_account()

    elif choice == 2:
        deposit()

    elif choice == 3:
        withdraw()

    elif choice == 4:
        check_balance()

    elif choice == 0:
        break

    else:
        print("Invalid choice. Try again")
