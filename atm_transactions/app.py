#Task 5
from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

#Task 2
print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
pin = input("Enter PIN ")
balance = 0.0
print(name,"has been registered with a starting balance of", balance)

#Task 3
while (True):
    name_to_validate = input("Enter Name: ")
    pin_to_validate = input("Enter PIN: ")
    if (name_to_validate == name and pin_to_validate == pin):
        print ("Login Successful!")
        break
    else:
        print ("Invalid Credentials!")

while (True):
    atm_menu(name)
    option = input ("Choose an option: ")
    if option == "1":
        account.show_balance(balance)

    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
        

    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)

    elif option == "4":
        account.logout
        break

    else:
        print("You have entered an invalid selection, please choose from options 1-4")


