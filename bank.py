import os.path


def get_file_name():
    return input("Enter file name to save data: ")


def add_expense(expenses):
    amount = input("Enter expense amount: ")
    description = input("Enter expense description: ")
    expenses.append({'amount': amount, 'description': description})


def add_income(incomes):
    amount = input("Enter income amount: ")
    description = input("Enter income description: ")
    incomes.append({'amount': amount, 'description': description})


def display_data(expenses, incomes):
    print("Expenses:")
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Description: {expense['description']}")

    print("\nIncomes:")
    for income in incomes:
        print(f"Amount: {income['amount']}, Description: {income['description']}")


def calculate_total(expenses, incomes):
    total_expenses = sum(int(e['amount']) for e in expenses)
    total_incomes = sum(int(i['amount']) for i in incomes)
    return total_expenses, total_incomes


def compare_expenses_with_budget(total_expenses, budget):
    if total_expenses > budget:
        print("You exceeded your budget.")
    elif total_expenses == budget:
        print("You used up your whole budget.")
    else:
        print(f"Your expenses are {budget - total_expenses} below your budget.")


def save_data(file_path, expenses, incomes):
    with open(file_path, 'w') as f:
        f.write("Expenses:\n")
        for expense in expenses:
            f.write(f"Amount: {expense['amount']}, Description: {expense['description']}\n")

        f.write("\nIncomes:\n")
        for income in incomes:
            f.write(f"Amount: {income['amount']}, Description: {income['description']}\n")
    print("Data saved successfully.")


def load_data(file_path, expenses, incomes):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            current_list = None
            for line in lines:
                if "Expenses" in line:
                    current_list = expenses
                elif "Incomes" in line:
                    current_list = incomes
                elif any(c.isalpha() for c in line):
                    amount, description = line.split(", ")
                    current_list.append(
                        {'amount': amount.split(": ")[1], 'description': description.split(": ")[1].strip()})

        print("Data loaded successfully.")
    else:
        print("File not found.")


expenses = []
incomes = []
while True:
    print("Select an option:")
    print("1 - Add expense")
    print("2 - Add income")
    print("3 - Display expenses and incomes")
    print("4 - Calculate total expenses and incomes")
    print("5 - Compare expenses with budget")
    print("6 - Save data to file")
    print("7 - Load data from file")
    print("0 - Exit")

    option = input("Option: ")

    if option == "1":
        add_expense(expenses)

    elif option == "2":
        add_income(incomes)

    elif option == "3":
        display_data(expenses, incomes)

    elif option == "4":
        total_expenses, total_incomes = calculate_total(expenses, incomes)
        print(f"Total expenses: {total_expenses}\nTotal incomes: {total_incomes}")

    elif option == "5":
        budget = input("Enter your budget: ")
        total_expenses, total_incomes = calculate_total(expenses, incomes)
        compare_expenses_with_budget(total_expenses, int(budget))

    elif option == "6":
        file_path = get_file_name()
        save_data(file_path, expenses, incomes)

    elif option == "7":
        file_path = get_file_name()
        load_data(file_path, expenses, incomes)

    elif option == "0":
        break

    else:
        print("Invalid option. Try again.")

print("Goodbye!"
