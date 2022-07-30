import datetime
from datetime import timedelta
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lms_project"
)


def BorrowBook():
    print("""............CHECKIN (BORROW) FORM.............""")
    print("")
    print("Please fill the form below!")
    acc_ID = input("Enter your ID >>> ")
    acc_name = input("Enter your name >>> ")
    book_ID = input("Enter book ID >>> ")
    book_name = input("Enter book title >>> ")
    print("")
    date_issue = datetime.date.today()
    # borrow period 3 days
    td = datetime.timedelta(days=3)
    due_date = date_issue + td
    data = (acc_ID, acc_name, book_ID, book_name, date_issue, due_date)
    # Fetch account list in mysql
    sql = "SELECT * FROM accounts"
    c = mydb.cursor()
    c.execute(sql)
    result_accounts = c.fetchall()
    # Fetch books list in mysql
    sql1 = "SELECT * FROM books"
    d = mydb.cursor()
    d.execute(sql1)
    result_books = c.fetchall()
    if (acc_ID != result_accounts[0] or acc_name != result_accounts[1]) and (book_ID != result_books[0] or book_name != result_books[1]):
        sql2 = "INSERT INTO borrows(acc_ID,acc_name,book_ID,book_name,date_issue,due_date) values(%s,%s,%s,%s,%s,%s)"
        cur = mydb.cursor()
        cur.execute(sql2, data)
        mydb.commit()
        print("The book is successfully recorded.")
        print("The book is issued to:", acc_name)
        print("Due date: ", due_date)
        bookup(book_ID, -1)
    else:
        print("Put the correct information in the form!")

# Update book stock
def bookup(co, u):
    sql = "SELECT book_stock FROM books WHERE book_ID = %s"
    data = (co,)
    c = mydb.cursor()
    c.execute(sql, data)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "UPDATE books SET book_stock = %s where book_ID = %s"
    d = (t, co)
    c.execute(sql, d)
    mydb.commit()
