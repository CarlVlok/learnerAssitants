from authentication import authentication

def login():
    auth = authentication()

    while True:
        print("--Login--")
        un = input("Username: ")
        pw = input("Password: ")
        if auth.login(un, pw) == True:
            print('SUCCESSFUL LOGIN')
            modules = auth.getModules(un)
            return modules
        else:
            print("FAILURE!!!!!!!!!")
        

def studyGuidesMenu():
    pass

def chatBot():
    pass

def previousChat():
    pass

modules = login()
while True:
    print("---Main Menu---")
    option = int(input(f"[1] Study guides\n[2] Chatbot\n[3] Previous chats\n[0] Exit\nSelect an option: "))
    if option == 1:
        studyGuidesMenu()
    elif option == 2:
        chatBot()
    elif option == 3:
        previousChat()
    elif option == 0:
        print("Bye Bye")
        break