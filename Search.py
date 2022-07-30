import pandas as pd

# Create list---------------------------------------------------------------------------------------------------------------
import mysql.connector
book_barcode = []
book_title = []
book_cat = []
book_avail = []

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lms_project"
)


def SearchBook():
    # Display search book menu
    print("""............SEARCH BOOK.............
    1.Search by Book ID
    2.Search by Title""")
    print("")
    srch_opt = input("Select your option[1-2] >>> ")
    print("")
    if srch_opt > '0' and srch_opt < '3':
        # Search by Book ID
        if srch_opt == "1":
            book_ID = input("Enter Book ID >>> ")
            # Fetch book list in mysql
            sql = "SELECT * FROM books"
            c = mydb.cursor()
            c.execute(sql)
            result_books = c.fetchall()
            print('Book ID', '%13s' % 'Book Title', '%48s' %
                  'Category', '%17s' % 'Stock')
            print("-"*150)
            for i in result_books:
                if book_ID == i[0]:

                    print(
                        f"{str(i[0]):<10s} {str(i[1]):<50s} {str(i[2]):<20s} {str(i[3]):<10s}")
        # Search by title
        elif srch_opt == "2":  
            book_name = input("Enter book title >>> ")
            # Fetch book list in mysql
            c = mydb.cursor()
            sql = "SELECT * FROM books"
            c.execute(sql)
            result_books = c.fetchall()
            print('Book ID', '%13s' % 'Book Title', '%48s' %
                  'Category', '%17s' % 'Stock')
            print("-"*150)
            for i in result_books:
                if book_name != None and book_name in i[1]:
                    print(
                        f"{str(i[0]):<10s} {str(i[1]):<50s} {str(i[2]):<20s} {str(i[3]):<10s}")
