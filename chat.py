import os



class Chat():
    def __init__(self, user, new):
        self.user = user
        if new==True:
            try:
                self.workingDirec = f"data/chats/{self.user}Chats"
                os.mkdir(self.workingDirec)
                print("Directory Succesfully created")
            except FileExistsError:
                print(f"File for {self.user} already exists")
        elif new==False:
            try:
                self.workingDirec = f"data/chats/{self.user}Chats"
                print(f"Using {self.workingDirec} as working directory")
            except FileNotFoundError:
                print(f"File path for {self.user} not found\nGiven Directory: {self.workingDirec}")
        
    def genCode(self, topic):
        newT = topic.split()
        return self.user[0]+ newT[1] + newT[2]
    
    def newChat(self, que, ans):
        code = Chat.genCode(self, que)
        fp = f"{self.workingDirec}/{code}"
        with open(fp, 'w') as file:
            file.write('question: '+que+ '\n')
            file.write('answer: '+ans+ '\n')
            print(f"Succesfully written in {fp}")
        file.close()
        return code
            
    def writeToChat(self, conv ,code):
        try:
            fp = f"data/chats/{self.user}Chats/{code}"
            with open(fp, 'a') as file:
                file.write('question: '+conv['question']+ '\n')
                file.write('answer: '+conv['answer']+ '\n')
                print(f"Succesfully written to {code} ")
        except FileNotFoundError:
            print(f"Unable to find file at {fp}")
    
    def getAllCodes(self):
        codes = os.listdir(self.workingDirec)
        return codes
    
    def getAllChatsForMenu(self):
        chats = self.getAllCodes()
        if len(chats) == 0:
            return "Cannot find any previous chats"
        count = 0
        fp = f"data/chats/{self.user}Chats/"
        output = []
        for chat in chats:
            with open((fp+chat), 'r') as file:
                for line in file:
                    if line.lower().startswith('question:'):
                        qtext = line.split(":", 1)[1].strip()
                        output.append({'id': count, 'question': qtext})
                        count+=1
                        break
        return output
            
# c = Chat("Peter", True)
# conv = {'question': 'this is a question', 'answer': 'This is the asnwer'}
# c.writeToChat(conv,"Cmanywoods?")

# firstCode = c.newChat(conv['question'], conv['answer']) #Writes into cisa

# conv2 = {'question': 'QQQQQQ QQQQ QQQQ', 'answer': 'AAAAAAAA AAAA AAAA'}
# secCode = c.newChat(conv2['question'], conv2['answer'])
# c.writeToChat(conv2, secCode) #Is gonna print another entry into secCode

