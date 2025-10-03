import os



class Chat():
    """
    Initializing Chat, using the users session name and whether its a new session
    This class handles anything to do with textfiles, and specific session information
    """
    def __init__(self, session, new):
        self.session = session
        if new==True:
            try:
                self.workingDirec = f"data/chats/{self.session}Chats"
                os.mkdir(self.workingDirec)
                print("-----Directory Succesfully created-----")
            except FileExistsError:
                print(f"-----ERROR:File for {self.session} already exists-----")
        elif new==False:
            try:
                self.workingDirec = f"data/chats/{self.session}Chats"
                print(f"-----Using {self.workingDirec} as working directory-----")
            except FileNotFoundError:
                print(f"-----ERROR:File path for {self.session} not found\nGiven Directory: {self.workingDirec}-----")
        
    def genCode(self, topic):
        newT = topic.split()
        return self.session[0]+ newT[1] + newT[2]
    
    def writeToNewChat(self, que, ans):
        code = Chat.genCode(self, que)
        fp = f"{self.workingDirec}/{code}.txt"
        with open(fp, 'w') as file:
            file.write('question: '+que+ '\n')
            file.write('answer: '+ans+ '\n')
            print(f"-----Succesfully written in {fp}-----")
        file.close()
        return code
            
    def writeToChat(self, conv ,code):
        try:
            fp = f"data/chats/{self.session}/{code}"
            with open(fp, 'a') as file:
                file.write('question: '+conv[0]+ '\n')
                file.write('answer: '+conv[1]+ '\n')
                print(f"-----Succesfully written to {code}-----")
        except FileNotFoundError:
            print(f"-----ERROR:Unable to find file at {fp}-----")
    
    def getAllCodes(self):
        codes = os.listdir(self.workingDirec)
        if codes != None:
            return codes
        return False
    
    def getAllChatsForMenu(self):
        chats = self.getAllCodes()
        if chats!=False:
            if len(chats) == 0:
                return False
            count = 0
            fp = f"data/chats/{self.session}Chats/"
            output = []
            for chat in chats:
                with open((fp+chat), 'r') as file:
                    for line in file:
                        if line.lower().startswith('question:'):
                            qtext = line.split(":", 1)[1].strip()
                            output.append({'id': count, 'question': qtext, 'file':chat})
                            count+=1
                            break
            return output
                
    def getAllText(self, code):
        fp = f"data/chats/{self.session}Chats"
        folder = os.listdir(fp)
        for f in folder:
            if f == code:
                file = f
        with open(f"{fp}/{file}",'r') as file:
            for line in file:
                print(line)
            out = file.read()
        return out

                
# c = Chat("fittest", False)
# print(c.getAllText('fisthe.txt'))