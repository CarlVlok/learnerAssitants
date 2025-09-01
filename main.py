import gemConnect as gc
import chat
import dataLoad as dl

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
    while True:
        print("MAIN MENU\n")
        try:
            option= int(input("[1] NewChat\n[2]ExistingChat\n[3] Exit\nSelect an option: "))
        except ValueError:
            print(f"{ValueError}: Enter a number!")
        if option==1:
            prompt = ""
            ans = []
            prompt = input("Enter your prompt:\n")
            if prompt!="Exit":
                response = bot.query(prompt, module,ans)
                print(f"\nResponse: {response[0]['answer']}")
                code = c.writeToNewChat(response[0]['question'], response[0]['answer'])
                ans.append((response[0]['question'], response[0]['answer']))
                while True:
                    prompt = input("Enter your prompt:\n")
                    if prompt!="Exit":
                        response = bot.query(prompt, module,ans)
                        print(f"\nResponse: {response[0]['answer']}")
                        conv = [response[0]['question'], response[0]['answer']]
                        c.writeToChat(conv, code)
                        ans.append({"question":response[0]['question'], "answer":response[0]['answer']})
                    else:
                        break
                    
        elif option==2:
            prev = c.getAllChatsForMenu()
            print("Previous chats\n")
            for i in prev:
                print(f"[{i['id'] +1}] {i['question']}")
            print(f"[{len(prev) + 1}] Exit")
            prevOption = int(input("Select a chat: "))
            p = prev[prevOption-1]['file']
            prevContext = [c.getAllText(p)]
            while True:
                prompt = input("Enter your prompt:\n")
                if prompt!="Exit":
                    response = bot.query(prompt, module, prevContext)
                    print(f"\nResponse: {response[0]['answer']}")
                    conv = [response[0]['question'], response[0]['answer']]
                    c.writeToChat(conv, p)
                    prevContext.append({"question":response[0]['question'], "answer":response[0]['answer']})
                else:
                    break
        elif option==3:
            print('Exitting...')
            break
        else:
            return "Unexpected error occured, please try again"    
            
        




m, n, ne = login()
mainMenu(m, n, ne)

        
    
