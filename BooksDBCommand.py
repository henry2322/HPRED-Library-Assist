import sqlite3
import csv

libDB = sqlite3.connect('library.db')

def initDB():
    crsr = libDB.cursor()
    crsr.execute("""CREATE Table User (Title varchar(255), Author varchar(255), Isbn int, Available int, Total int)""")
    a_file = open("book.csv")
    rows = csv.reader(a_file)
    crsr.executemany("INSERT INTO User VALUES (?, ?, ?, ?, ?)", rows)

def searchBook(searching, searchMode):
    crsr = libDB.cursor()
    if searchMode == 0:
        crsr.execute("SELECT * FROM User WHERE Title=" + searching + ";")
    elif searchMode == 1:
        crsr.execute("SELECT * FROM User WHERE Author=" + searching + ";")
    elif searchMode == 2:
        crsr.execute("SELECT * FROM User WHERE Isbn=" + searching + ";")

    ans = crsr.fetchall()

    for i in ans:
        print(i)
    crsr.close()

def displayBook(ISBN):
    crsr = libDB.cursor()
    crsr.execute("SELECT * FROM User WHERE Isbn=" + ISBN + ";")
    ans = crsr.fetchone()
    if ans and ans[4] > 0:
        print(ans)
        crsr.close()
        return True
    else:
        crsr.close()
        return False

def addBook(isbn,title,author,available,total):
    crsr = libDB.cursor()
    if displayBook(isbn):
        crsr.execute("SELECT DISTINCT Total FROM User")
        v = crsr.fetchone()
        crsr.execute("UPDATE User SET Total=" + str(v[3] + total) + "WHERE Isbn=" + isbn + ";")
    else:
        crsr.execute("INSERT INTO User VALUES (Title,Author,Isbn,Availabe,Total) (" + title + "," + author + "," + str(isbn) +
                     "," + str(available) + str(total) + ");")
    crsr.commit()
    crsr.close()

def delBook(isbn):
    crsr = libDB.cursor()
    if displayBook(isbn):
        crsr.execute("DELETE FROM User WHERE Isbn=" + isbn + ";")
