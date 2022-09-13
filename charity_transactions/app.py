from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin":"password123"}
donations = []
authorized_user = ""

while True:
    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate.")

    else:
        print("Logged in as:", authorized_user)
    
    option = input("Select an option from the menu above: ")
    if option == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        authorized_user = login(database, username, password)

    elif option == "2":
        username = input("Register your username: ")
        password = input("Register your password: ")
        authorized_user = register(database, username)

        if authorized_user != "":
            database[authorized_user] = password

        else:
            print("You entered an invalid response, please register again:")

    elif option == "3":
        if authorized_user == "":
            print ("You must be logged in to donate.")

        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)

    elif option == "4":
        show_donations(donations)

    elif option == "5":
        print("You are now logged out")
        break

    else:
        print("You entered an invalid response, please select again:")
