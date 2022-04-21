from userProfile import UserProfile
import constants

if __name__ == "__main__":
    #user = UserProfile()

    while True:
        userinput = input().split()

        if userinput[0] == "exit":
            break
        elif userinput[0] == "search" and len(userinput) == 3:
            pass
        elif userinput[0] == "holds":
            pass
        elif userinput[0] == "requestHold":
            pass
        elif userinput[0] == "display":
            pass
        else:
            if user.isSuperUser():
                if userinput[0] == "removeUser" and len(userinput) == 2:
                    user.removeUser(userinput[1])
                elif userinput[0] == "createUser" and len(userinput) == 2:
                    user.createUser(userinput[1])
                elif userinput[0] == "addBook" and len(userinput) == 6:
                    pass
                elif userinput[0] == "removeBook" and len(userinput) == 2:
                    pass

            else:
                print("Invalid Input")
                

 # cofirm login
 # user data
