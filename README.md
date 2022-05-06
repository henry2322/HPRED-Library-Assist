# HPRED-Library-Assist
# Project Info
This project is about creating a software in which a group of 5 people will help develop. In which the software focuses on Librarian Assistant, this will help librarians manage certain task via through an application or web browser. Such things like book searches, ordering books, placing orders online, checking out books through the software, and possible implement a check feature that allows the librarian to know how long a book has check out. Which enables the librarian to notify the person to turn in the book if the due date is reached. Overall, the application is implemented to assist Librarians with their task.

# Team Info
For the team we have 5 people, Henry, Phillip, Rafael, Ethan, and Dathan. All of which we all have experienced in with coding C/C++ or Python. We wish to implement the software on either language but, we are leaning towards Python as our main language we will use for this project.

#Instructions on Program 
For User Profiles
For the User profile features you must enter a ID that is in the csv file. 0 indicates deletedUser(which can't access anything and must retype ID) 1 indicates  normalUser (which only have access to functions that dont modify the database) 1 superUser or admin (which access every command displayed). Enter valid ID:
superUser = all commands
normalUser = limited commands
deletedUser = no commands and asked again
To create/remove
--Note when entering functions must type :(function namee) (argument) (argument2) etc...

For Book functions 
Search feature first thing was a string and the second and integer for the mode. 0 is by title, 1 for author, and 2 for ISBN  seaarch African 1
display features demonstrates book based on ISBN: Sample could be:(0)  or (9780762419227) display 9780762419227
addBook which accepts (int isbn) (str title) (str author) (int total) = addBook 128371289 TheLogofortune Billy 3
removeBook  which deleted book from database based on unique ISBN code  = delBook 812981605 or del 0(which would return ISBN does not exist)

For Hold Function
holds function prints all based on profileID  = holds superUser
requestHold gets hold on a book based on ISBN and profile = requestHold 9780762419227 superUser

