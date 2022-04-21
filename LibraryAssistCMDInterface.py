from userProfile import UserProfile
import constants


if __name__ == "__main__":
    user = UserProfile()

    while True:
        userinput = input().split()
        
        if userinput[0] == "exit":
            break
        elif False:
            pass
        else:
            if user.isSuperUser():
                if userinput[0] == "removeUser" and len(userinput) == 2:
                    user.removeUser(userinput[1])
                elif userinput[0] == "createUser" and len(userinput) == 2:
                    user.createUser(userinput[1])
            else:
                print("Invalid Input")

 # cofirm login
 # user data
