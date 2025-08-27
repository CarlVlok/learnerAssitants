import os



class fileChat():
    def __init__(self, user, topic):
        self.fp = os.path.join(os.getcwd()+"/data/chats")
        self.user = user
        self.topic = topic
        
    def genCode(self, user, chat, topic):
        newT = topic.split()
        return user[0]+ str(chat)+ newT[1] + newT[2]
    
    def newChat(self):
        fp = f"{self.fp}/{fileChat.genCode(self, self.user, self.chat, self.topic)}"
        with open(fp, 'w') as file:
            file.write("Hello world")
            

c = fileChat("Carl", 1, "I dont know man")
c.newChat()