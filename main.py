import gemConnect as gc
import chat
import dataLoad as dl


# bot = gc.agent()
# response = bot.query(input, module)
# c = chat.Chat(user, True)
# code = c.newChat(response[0]['question'], response[0]['answer'])


def login():
    name=input("Enter your name: ")
    module=input("Enter your module: ")
    new = input("Are you new [y/n]:").lower()
    if new=='y' or new=='yes':
        return module, name, True
    elif new=='n' or new=='no':
        return module, name, False


def mainMenu(module, user, new):
    bot = gc.agent()
    c = chat.Chat(user, new)
    option=''
    while option!="3":
        print("MAIN MENU\n")
        try:
            option= int(input("1: NewChat\n2:ExistingChat\n3: Exit\nSelect an option"))
            if option==1:
                prompt = input("Enter your prompt:\n")
                response = bot.query(prompt, module)
                code = c.newChat(response[0]['question'], response[0]['answer'])
        except ValueError:
            print("Enter a number!")


res = login()
mainMenu(res)

        
    
