def show_homepage():
    print("        === DonateMe Homepage ===         ")
    print("------------------------------------------")
    print("| 1.    Login       | 2.   Register      |")
    print("------------------------------------------")
    print("| 3.    Donate      | 4.  Show Donations |")
    print("------------------------------------------")
    print("|              5.   Exit                 |")
    print("------------------------------------------")

def donate(username):
    donation_amt = input("Enter amount to donate:")
    donation_string = username+ " donated $" +donation_amt
    print ("Thank you for your donation of $"+donation_amt)
    return (donation_string)

def show_donations(donations):
    print ("\n--- All Donations ---")
    if donations == []:
        print ("There are currently no donations")
    else:
        for donation in donations:
            print(donation)