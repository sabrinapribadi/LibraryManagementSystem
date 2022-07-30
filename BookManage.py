from gettext import find
from numpy import dtype
import pandas as pd
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lms_project"
)


def BookManagement():
    # Display book management menu
    print("""........BOOK MANAGEMENT..........
    1.Add Book
    2.Delete Book
    3.Book List""")
    print("")
    option = input("Select your option[1-3] >>> ")
    print("")
    if option > '0' and option < '4':
        # Add book
        if option == '1':
            print(".............")
            print("Please fill the form below!")
            print("")
            book_ID = input("Enter book ID >>> ")
            book_name = input("Enter book title >>> ")
            book_name = book_name.title()
            book_cat = input("Enter book category >>> ")
            book_stock = input("Enter book stock >>> ")
            data = (book_ID, book_name, book_cat, book_stock)
            # Fetch book list in mysql
            sql = "SELECT * FROM books"
            c = mydb.cursor()
            c.execute(sql)
            result_books = c.fetchall()
            if len(result_books) == 0 or book_ID != result_books[0] or book_name != result_books[1]:
                sql1 = "INSERT INTO books (book_ID,book_name,book_cat,book_stock) values(%s,%s,%s,%s);"
                cur = mydb.cursor()
                cur.execute(sql1, data)
                mydb.commit()
                print("Completed! The book is successfully listed.")
            else:
                print("The book has already listed!")
        # Delete book
        elif option == '2':
            print("To delete the book,please enter the book ID!")
            print("")
            book_ID = input("Enter book ID >>> ")
            # Fetch book list in mysql
            sql = "SELECT * FROM books"
            c = mydb.cursor()
            c.execute(sql)
            result_books = c.fetchall()
            for i in result_books:
                if str(book_ID) == str(i[0]):
                    sql1 = "DELETE FROM books WHERE book_ID = %s;"
                    data = (book_ID,)
                    cur = mydb.cursor()
                    cur.execute(sql1, data)
                    mydb.commit()
                    print("The book has been deleted.")
        # Display book list
        elif option == '3':
            c = mydb.cursor()
            sql = "SELECT * FROM books;"
            c.execute(sql)
            result_books = c.fetchall()
            print('Book ID', '%13s' % 'Book Title', '%48s' %
                  'Category', '%17s' % 'Stock')
            print("-"*150)
            for i in result_books:
                print(
                    f"{str(i[0]):<10s} {str(i[1]):<50s} {str(i[2]):<20s} {str(i[3]):<10s}")
    else:
        print("Invalid input!!")
