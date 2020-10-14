"""

Default user = veysibisen
Default password = 12345

"""

users = {
    "veysibisen": {
        "name": "Veysi Furkan",
        "surname": "Bisen",
        "phone":  "05313442040",
        "email": "veysi@gmail.com",
        "password": "12345",
        "primary": 0,
        "loan": 0
    }
}

def display_starting_menu():
    print("\n********** Starting Menu **********")
    print("\n1.Login\n2.Register\n3.Exit")

    while True:
        try:
            choice = int(input("\nPlease write the Menu Item Number that you want to go: "))
            if choice == 1:
                login()
                break
            elif choice == 2:
                register()
                break
            elif choice == 3:
                exit()
            else:
                print("The Menu Item you requested is not exist!!")
                continue
        except ValueError:
            print("You must enter only the number of the menu item!")
            continue
        break


def display_main_menu(user):
    print("\n\n********** Main Menu **********")
    print(f"\nHello {user}, have a good day.")

    print("\n1.Account Information\n2.Deposit Money\n3.Withdraw Money\n4.Aplly For Loan\n5.Log-out")

    while True:
        try:
            choice = int(input("\nPlease write the Menu Item Number that you want to go: "))
            if choice == 1:
                account_information(user)
                break
            elif choice == 2:
                deposit_money(user)
                break
            elif choice == 3:
                withdraw_money(user)
                break
            elif choice == 4:
                apply_for_loan(user)
                break
            elif choice == 5:
                logout()
                break
            else:
                print("The Menu Item you requested is not exist!!")
                continue
        except ValueError:
            print("You must enter only the number of the menu item!")
            continue


def login():
    print("\n\n********** Login **********\n")
    print("Provide your credentials below.\n")

    while True:
        username = input("Please write your username: ")
        password = input("Please write your password: ")

        if username in users.keys():
            if users[username]["password"] != password:
                print("\nThe password you provided is WRONG!!")
                continue
            else:
                display_main_menu(username)

        else:
            print("\nThe username you provided is WRONG!!")
            continue

        break


def register():
    print("\n\n********** Register **********")
    print("\nPlease fill the personal information form.\n")
    new_user = {}
    username = ""

    name = input("Name: ")
    surname = input("Surname: ")
    phone = input("Phone Number: ")
    email = input("Email: ")

    while True:
        username += input("\nUsername: ")
        if username not in users.keys():
            password = input("Password: ")
            password_again = input("Password (again): ")
            if password == password_again:
                new_user["name"] = name
                new_user["surname"] = surname
                new_user["phone"] = phone
                new_user["email"] = email
                new_user["password"] = password
                new_user["primary"] = 0
                new_user["loan"] = 0
                users.setdefault(username, new_user)
            else:
                print("The passwords do not mach! Please check again!")
                continue
        else:
            username = ""
            print("The username you choose has been taken! Please provide another one!")
            continue

        break

    print("\nSaving your information...")
    print("Returning to Starting Menu...")
    display_starting_menu()


def account_information(user):
    print("\n\n********** Account Information **********")
    name_surname = users[user]["name"] + " " + users[user]["surname"]
    print(43 * "_" + f"\n|Name/Surname: {name_surname}" + (40-len(name_surname)-13) * " " + "|")
    print("|" + 41 * " " + "|")
    print("|" + "Contact Information: " + (41 - 21) * " " + "|")
    print("|\t" + "Phone Number: " + users[user]["phone"] + (41 - 14 - len(users[user]["phone"]) - 7) * " " + "|")
    print("|\t" + "Email: " + users[user]["email"] + (41 - 7 - len(users[user]["email"]) - 7) * " " + "|")
    print("|" + 41 * " " + "|")
    print("|" + "Balance Information: " + (41 - 21) * " " + "|")
    print("|\t" + "Primary Account Balance: " + str(users[user]["primary"]) + "$" + (40 - 25 - len(str(users[user]["primary"])) - 7) * " " + "|")
    print("|\t" + "Loan Account Balance: " + str(users[user]["loan"]) + "$" + (40 - 22 - len(str(users[user]["loan"])) - 7) * " " + "|")
    print("|" + 41 * "_" + "|")

    print("Returning back to Main Menu...")
    display_main_menu(user)


def deposit_money(user):
    print("\n\n********** Deposit Money **********")
    print("\nYour current balance in Primary Account is", str(users[user]["primary"]) + "$")
    while True:
        try:
            deposit_amount = int(input("\nPlease write the amount you would like to deposit: "))
            users[user]["primary"] += deposit_amount
            print("\nDepositing your money...")
            print("Your updated balance is", str(users[user]["primary"]) + "$")
            while True:
                again = input("\nWould you like to deposit again? (Y or N): ")
                if again == "y" or again == "Y" or again == "yes" or again == "Yes" or again == "YES":
                    break
                elif again == "n" or again == "N" or again == "no" or again == "No" or again == "NO":
                    print("\nReturning to Main Menu..")
                    display_main_menu(user)
                    break
                else:
                    print("Please write valid answer to question!!")
                    continue
            continue
        except ValueError:
            print("You must enter only positive number in order to complete your process!")
            continue


def withdraw_money(user):
    print("\n\n********** Withdraw Money **********")
    print("1. Your current balance in Primary Account is", str(users[user]["primary"]) + "$")
    print("2. Your current balance in Loan Account is", str(users[user]["loan"]) + "$")

    while True:
        try:
            choice = int(input("\nPlease choose from which account you would like to withdraw money from: "))
            # Withdraw from Primary account
            if choice == 1:
                while True:
                    withdraw_amount = int(input("Please write the amount you would like to withdraw: "))
                    if type(withdraw_amount) != int or withdraw_amount < 0:
                        print("Please write only positive numbers!!")
                        continue
                    elif users[user]["primary"] < withdraw_amount:
                        print("\nSorry... Your account balance is not enough!")
                        while True:
                            answer = input("Would you like to barrow loan? (Y or N): ")
                            if answer == "y" or answer == "Y" or answer == "yes" or answer == "Yes" or answer == "YES":
                                print("\nRedirecting to Loan Menu...")
                                apply_for_loan(user)
                                break
                            elif answer == "n" or answer == "N" or answer == "no" or answer == "No" or answer == "NO":
                                print("\nReturning to Main Menu..")
                                display_main_menu(user)
                                break
                            else:
                                print("Please write valid answer to question!!")
                                continue
                    else:
                        users[user]["primary"] -= withdraw_amount
                        print("\nWithdrawing your money from 'Primary Account'...")
                        print("Your updated balance in Primary Account is", str(users[user]["primary"]) + "$")
                        while True:
                            again = input("\nWould you like to withdraw again? (Y or N): ")
                            if again == "y" or again == "Y" or again == "yes" or again == "Yes" or again == "YES":
                                break
                            elif again == "n" or again == "N" or again == "no" or again == "No" or again == "NO":
                                print("\nReturning to Main Menu..")
                                display_main_menu(user)
                                break
                            else:
                                print("Please write valid answer to question!!")
                                continue
                        continue
                    break
                break
            # Withdraw from Loan account
            elif choice == 2:
                while True:
                    withdraw_amount = int(input("Please write the amount you would like to withdraw: "))
                    if type(withdraw_amount) != int or withdraw_amount < 0:
                        print("Please write only positive numbers!!")
                        continue
                    elif users[user]["primary"] < withdraw_amount:
                        print("\nSorry... Your account balance is not enough!")
                        while True:
                            answer = input("Would you like to barrow loan? (Y or N): ")
                            if answer == "y" or answer == "Y" or answer == "yes" or answer == "Yes" or answer == "YES":
                                print("\nRedirecting to Loan Menu...")
                                apply_for_loan(user)
                                break
                            elif answer == "n" or answer == "N" or answer == "no" or answer == "No" or answer == "NO":
                                print("\nReturning to Main Menu..")
                                display_main_menu(user)
                                break
                            else:
                                print("Please write valid answer to question!!")
                                continue
                    else:
                        users[user]["loan"] -= withdraw_amount
                        print("\nWithdrawing your money from 'Loan Account'...")
                        print("Your updated balance in Loan Account is", str(users[user]["loan"]) + '$')
                        while True:
                            again = input("\nWould you like to withdraw again? (Y or N): ")
                            if again == "y" or again == "Y" or again == "yes" or again == "Yes" or again == "YES":
                                break
                            elif again == "n" or again == "N" or again == "no" or again == "No" or again == "NO":
                                print("\nReturning to Main Menu..")
                                display_main_menu(user)
                                break
                            else:
                                print("Please write valid answer to question!!")
                                continue
                        continue
                    break
                break
            else:
                print("The Menu Item you requested is not exist!!")
                continue
        except ValueError:
            print("You must enter only the number of the menu item!")
            continue


def apply_for_loan(user):
    print("\n\n********** Apply For Loan **********")

    print("\n**Note that the interest rate is 15%!")

    while True:
        try:
            month = int(input("\nPlease give the time-period you would like to pay back (in Months): "))
            while True:
                amount = int(input("Please provide the amount you would like to barrow (max 10.000$): "))
                if amount > 10000:
                    print("Maximum amount for loan is 10.000$! Please proceed accordingly!")
                    continue
                if amount < 0:
                    print("You can't apply for negative loan you dumb-ass!")
                    continue
                else:
                    print("\n***** Report *****\n")
                    interest = month / 12
                    total_payment = truncate(amount + ((amount * (15 * interest)) / 100), 2)
                    installment = truncate(total_payment / month, 2)

                    # Printing the report
                    print(42 * "_")
                    print("|" + 40 * " " + "|")
                    tpa = f"| Total Payback Amount: {total_payment}$"
                    print(tpa + (41 - len(tpa)) * " " + "|")
                    print("|" + 40 * " " + "|")
                    for month_num in range(1, month+1):
                        m = f" Mounth #{month_num} "
                        total_payment -= installment
                        tp = f"| Total Payment Left: {truncate(total_payment, 1)}$"
                        tmi = f"| This Month's Installment: {installment}$"
                        print("|" + int((40 - len(m))/2) * "*" + m + int((41 - len(m))/2) * "*" + "|")
                        print(tp + (41 - len(tp)) * " " + "|")
                        print(tmi + (41 - len(tmi)) * " " + "|")
                        print("|" + 40 * " " + "|")
                    print("|" + 40 * "_" + "|")

                    while True:
                        okay = input("\nPlease write 'ok' to confirm and 'cancel' to stop your loan request: ")
                        if okay == "okay" or okay == "Okay" or okay == "ok" or okay == "OK":
                            users[user]["loan"] += amount
                            print("\nYour loan is transferring to Loan Account...")
                            print("Redirecting to Account Information Menu...")
                            account_information(user)
                            break
                        elif okay == "cancel" or okay == "Cancel":
                            print("\nCancelling your loan application...")
                            print("Redirecting to Main Menu...")
                            display_main_menu(user)
                            break
                        else:
                            print("Please write valid answer to question!!")
                            continue

        except ValueError:
            print("You must enter only numbers to apply for a loan!")
            continue


def logout():
    display_starting_menu()


# Function for formatting the numbers for installment calculation.
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


display_starting_menu()
