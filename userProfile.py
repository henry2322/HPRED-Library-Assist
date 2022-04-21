from profilesDB import profilesDataBase
import constants

class UserProfile:
    def __init__(self):
        self.profilesdatabase = profilesDataBase()
        self.userID = None
        self.userStatus = None
        self.confirmLogin()

    def confirmLogin(self):
        profileDict = self.profilesdatabase.getProfileDict()
        validUser = False
        self.userStatus = None
        while validUser == False:
            print("Enter valid userID: ",end="")
            userinput = input()
            if userinput in profileDict and profileDict[userinput] != constants.DELETED_USER:
                validUser = True
                self.userStatus = profileDict[userinput]
                self.userID = userinput
    

    def isSuperUser(self):
        return self.userStatus == str(constants.SUPER_USER)

    
    def createUser(self, userID: str):
        self.profilesdatabase.createUser(userID)


    def removeUser(self, userID: str):
        self.profilesdatabase.removeUser(userID)