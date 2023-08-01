from myAuth import MyAuth


print("""
Login
---------------------
""")

ma = MyAuth()

def  turnOff(value):
    if value == "quit" or value == "q":
        quit()


while(True):

    print('Welcome to the fake login app')

    username = input("username:  ")
    turnOff(username)
    email = input("email:  ")
    turnOff(email)
    password = input("password:  ")
    turnOff(password)

    print("")

    ma.addingInfo(username, email, password)

