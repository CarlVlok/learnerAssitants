import os
base_dir = os.getcwd()


class authentication:
    def __init__(self):
        """
        Initializes and populates the userDB list, storing all login info of users
        userDB is used in code
        """
        self.userDB = []
        self.userPath = os.path.join(base_dir, "data/authentication/users.txt")
        

        file = open(self.userPath, "r")
        for line in file:
            word = line.strip("\n").split(";")
            self.userDB.append(tuple(word))
        file.close()

        
        """
        Initializes and populates the userModulesDB list, storing all login info of users
        userModulesDB is used in code
        """
        self.userModulesDB = {}
        self.modulesPath = os.path.join(base_dir, "data/authentication/userModules.txt")
        
        file = open(self.modulesPath, "r")
        for line in file:
            word = line.strip("\n").split(";")
            self.userModulesDB[word[0]] = tuple(word[1:])
        file.close()
    
    #Searches userDB to validate username and password
    def login(self, un, pw):
        for user in self.userDB:
            if user[2] == un and user[3] == pw:
                return True
        return False
    
    #Searches for the user, and returns their modules
    def getModules(self, un):
        for moduleU in self.userModulesDB.keys():
            if un == moduleU:
                return self.userModulesDB[moduleU]
        
a = authentication()
print(a.login("testU", "testP"))
print(a.getModules("testU"))