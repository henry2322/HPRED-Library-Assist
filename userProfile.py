from profilesDB import profilesDataBase
from booksDB import booksDB
from holdsDB import holdsDB
import constants

class UserProfile:
    def __init__(self):
        self.profilesdatabase = profilesDataBase()
        self.userID = None
        self.userStatus = None
        self.confirmLogin()
        self.book = booksDB()
        self.searched = []
        self.hold = holdsDB()
        self.ISBN = None
        profile_ID = None
        

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

    

    # user database
    def createUser(self, userID: str):
        self.profilesdatabase.createUser(userID)


    def removeUser(self, userID: str):
        self.profilesdatabase.removeUser(userID)

    

    # Display Book Details
    def displayCheckedBooks(self):
        raise NotImplementedError
    

    def displayHoldBooks(self):
        raise NotImplementedError
    


    #Book Database
    def addBook(self, title: str, author: str, isbn: int, total: int):
        self.book.addBook(isbn, title, author, total)
    

    def removeBook(self, isbn: int):
        self.book.delBook(isbn)

    
    def searchBook(self, searchStr: str, mode: int):
        self.searched = self.book.searchBook(searchStr, mode)
        
        
    def displayBook(self, index: int):
        if(len(self.searched) == 0):
            return
        if(index - 1 >= 0 and index - 1 < len(self.searched)):
            self.book.displayBook(self.searched[index - 1])
            self.searched = []


    #Holds Database
    def getHolds(self,profile_ID: str):
        self.hold.getHolds(profile_ID)
    

    def requestHold(self, ISBN: int, profile_ID: str):
        self.hold.request_hold(ISBN,profile_ID)

        
    

    def cancelHold(self):
        raise NotImplementedError


    #Search Display
    def bookSelection(self):
        raise NotImplementedError
    
    #might combine with function from book database unless 1 function is for super user and 1 for normal user ()
    def getBookInfo(self):
        raise NotImplementedError



    #Main Menu
    def login(self):
        raise NotImplementedError

    def displaySearch(self):
        raise NotImplementedError
