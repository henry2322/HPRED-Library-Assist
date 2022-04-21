import constants

class profilesDataBase():

    def __init__(self) -> None:
        pass

    
    def writeDictToCSV(self, profileDict):
        writeFile = open(constants.USERPROFILECSV_PATH, 'w', encoding="UTF-8")
        for profile in profileDict:
            print(str(profile) + "," + str(profileDict[profile]),file = writeFile)
        writeFile.close()


    def getProfileDict(self):
        profilesFile = open(constants.USERPROFILECSV_PATH, encoding = "UTF-8")
        profiles = profilesFile.readlines()
        profilesFile.close()
        profiles = [profile[:-1].split(",") for profile in profiles]
        profileDict = {}
        for profile in profiles:
            profileDict[profile[0]] = profile[1]
        return profileDict


    def removeUser(self, userID: str):
        profileDict = self.getProfileDict()
        if userID in profileDict:
            profileDict[userID] = constants.DELETED_USER
            self.writeDictToCSV(profileDict)
        else:
            print("User does not exist.")

    
    def createUser(self, userID: str):
        profileDict = self.getProfileDict()
        if userID not in profileDict:
            profileDict[userID] = constants.NORMAL_USER
            self.writeDictToCSV(profileDict)
        else:
            print("That userID is already taken.")