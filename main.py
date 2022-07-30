import time
import datetime

# import python files
import Search
import Borrow
import Return
import AccMember
import BookManage
import Records

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lms_project"
)

# Main loop for user input


def main():
    print("""............LIBRARY MANAGEMENT SYSTEM.............   
    1.Search Book    
    2.Check Out (Borrow) Book
    3.Check In (Return) Book
    4.Account & Membership Maintenance
    5.Book Management
    6.Records
    7.Exit
    """)
    choice = input("Enter task no >>> ")
    print("")

    # Tasks Option
    if(choice == '1'):
        Search.SearchBook()
        print("")
        main()
    elif(choice == '2'):
        Borrow.BorrowBook()
        print("")
        main()
    elif(choice == '3'):
        Return.ReturnBook()
        print("")
        main()
    elif(choice == '4'):
        AccMember.AccountList()
        print("")
        main()
    elif(choice == '5'):
        BookManage.BookManagement()
        print("")
        main()
    elif(choice == '6'):
        Records.RecordList()
        print("")
        main()
    elif(choice == '7'):
        print("Thank you for visiting us. As a wiseman said, 'Nothing is more pleasant than exploring a library'. Have a good day! ")
    else:
        print("UNKNOWN CHOICE!!!")
        print("Please input the correct number!")
        print("")
        main()


# Run the programm
main()
