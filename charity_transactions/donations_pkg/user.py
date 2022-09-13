""" database = {}
username = ""
password = ""
"""

def login(database, username, password):

    if username in database and password in database[username]:
        print ("Welcome back", username)
        return (username)
    elif username in database and password not in database[username]:
        print ("incorrect login, please register or try again \n")
        return ("")
    else:
        print ("incorrect login, please register first or try again\n")
        return ("")
    
def register(database, username):
    if username in database:
        print ("Username already registered, please enter a different username")
        return ("")
    if username not in database:
        print (username, "has been registered and you are now logged in")
        return (username)
