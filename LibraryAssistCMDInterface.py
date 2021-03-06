from userProfile import UserProfile
import constants

if __name__ == "__main__":
    user = UserProfile()

    while True:
        print("\nList of Commands you can use.\nsearch\ndisplay\nholds\nrequestHold\n")
        if user.isSuperUser():
                print("List of additional commands you can use.\nremoveUser\ncreateUser\naddBook\nremoveBook\n")
        userinput = input().split()

        if userinput[0] == "exit":
            break
        elif userinput[0] == "search" and len(userinput) == 3:
            user.searchBook(userinput[1], int(userinput[2]))
        elif userinput[0] == "holds" and len(userinput) == 2:
            user.getHolds(userinput[1])
        elif userinput[0] == "requestHold" and len(userinput) == 3:
            user.requestHold(int(userinput[1]),userinput[2])
        elif userinput[0] == "display" and len(userinput) == 2:
            user.displayBook(int(userinput[1]))
        else:
            if user.isSuperUser():
                if userinput[0] == "removeUser" and len(userinput) == 2:
                    user.removeUser(userinput[1])
                elif userinput[0] == "createUser" and len(userinput) == 2:
                    user.createUser(userinput[1])
                elif userinput[0] == "addBook" and len(userinput) == 5:
                    user.addBook(userinput[1], userinput[2], userinput[3], userinput[4])    
                elif userinput[0] == "removeBook" and len(userinput) == 2:
                    user.removeBook(int(userinput[1]))

            else:
                print("Invalid Input")
                

 # cofirm login
 # user data
