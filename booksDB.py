

class booksDB:
    def __init__(self):pass
    def searchBook(self,searching, searchMode):
        with open('books.csv', 'r') as file:
            lines = file.readlines()
            list = []
            i = 1

            if searchMode < 0 or searchMode > 2:
                return -1
            if searchMode == 2:
                searchMode = -3

            for n in lines:
                val = n.split(',')
                if val[0][0] == '"':
                    t = 1
                    while val[t][-1] != '"':
                        val[0] = val[0] + val[t]
                        t += 1
                    val[0] = val[0] + val[t]
                    val[1] = val[t + 1]
                if str(searching).lower() in val[searchMode].lower():
                    print(str(i) + ". " + val[0] + "    " + val[1] + "    " + val[-3])
                    list.append(int(val[-3]))
                    i += 1
            if len(list) == 0:
                print("No books were found")
            return list

    def displayBook(self,ISBN):
        with open('books.csv', 'r') as file:
            lines = file.readlines()
            for n in lines:
                val = n.split(',')
                try:
                    t = int(val[-3])
                except:
                    t = -1

                if ISBN == t:
                    print(n.split("\n"))
                    n = n.strip("\n")
                    return n
            print("Book does not exist")




    def addBook(self,isbn, title, author, total):
        with open('books.csv', 'r') as file:
            lines = file.readlines()
        with open('books.csv', 'w') as file2:
            i = 0
            for n in lines:
                val = n.split(',')
                if val[0][0] == '"':
                    t = 1
                    while val[t][-1] != '"':
                        val[0] = val[0] + val[t]
                        t += 1
                    val[0] = val[0] + val[t]
                    val[1] = val[t + 1]
                try:
                    t = int(val[-3])
                except:
                    t = -1
                if isbn == t:
                    ntotal = int(val[-2]) + total
                    navail = int(val[-1]) + total
                    nline = val[0] + "," + val[1] + "," + val[-3] + "," + str(ntotal) + "," + str(navail) + "\n"
                    i = 1
                    file2.write(nline)
                    print("Added " + str(total) + " books: " + nline.strip("\n"))
                else:
                    file2.write(n)
            if(i == 0):
                nline = title + "," + author + "," + str(isbn) + "," + str(total) + "," + str(total) + "\n"
                file2.write(nline)
                print("Added new book:" + nline.strip("\n"))
            return i

    def delBook(self,isbn):
        with open('books.csv', 'r') as file:
            lines = file.readlines()
        with open('books.csv', 'w') as file2:
            i = 0
            x = -1
            for n in lines:
                val = n.split(',')
                try:
                    t = int(val[-3])
                except:
                    t = -1
                if isbn != t:
                    file2.write(n)
                else:
                    print("Deleted " + n.strip("\n") + " from library")
                    x = i
                i += 1
            if x == -1:
                print("Book ISBN: " + str(isbn) + " does not exist")
            return x

if __name__ == '__main__':
    x = booksDB()
    #a = x.searchBook("The Power of Habit", 0)
    #a = x.searchBook("Land Apart: A South African Reader", 0)
    #a = x.searchBook("the", 0)
    #a = x.searchBook("African", 1)
    #a = x.searchBook(19, 2)
    #b = x.displayBook(a[1])
    b = x.displayBook(0)
    #x.addBook(812981605, "The Power of Habit", "Charles Duhigg", 3)
    #x.addBook(140100040, "Land Apart: A South African Reader", "Various", 2)
    #x.delBook(812981605)
    #x.delBook(0)
    #f = "finished"
