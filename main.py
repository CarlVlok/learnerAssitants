import gemConnect as gc
import chat
import dataLoad as dl
import os

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
            option= int(input("[1] NewChat\n[2]ExistingChat\n[3] Exit\nSelect an option: "))
            if option==1:
                prompt = ""
                while prompt!="Exit":
                    prompt = input("Enter your prompt:\n")
                    response = bot.query(prompt, module)
                    print(f"{response[0]['question']}, {response[0]['answer']}")
                    c.writeToNewChat(response[0]['question'], response[0]['answer'])
            elif option==2:
                prev = c.getAllChatsForMenu()
                print("Previous chats\n")
                for i in prev:
                    print(f"[{i['id'] +1}] {i['question']}")
                print(f"[{len(prev) + 1}] Exit")
                prevOption = input("Select your option: ")
                
                
            elif option==3:
                break
            else:
                return "Unexpected error occured, please try again"    
            
        except ValueError:
            print("Enter a number!")




m, n, ne = login()
mainMenu(m, n, ne)

        
    
