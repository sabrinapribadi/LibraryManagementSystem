import datetime
from datetime import timedelta
import pandas as pd
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lms_project"
)


def ReturnBook():
    print("""............CHECKOUT (RETURN) FORM.............""")
    print("")
    print("Please fill the form below!")
    acc_ID = input("Enter your ID >>> ")
    book_ID = input("Enter book ID >>> ")
    print("")
    dates = datetime.date.today()
    date_return = datetime.date.today().strftime('%Y-%m-%d')
    ret_data = {
        "acc_ID": [acc_ID],
        "book_ID": [book_ID],
        "date_return": [date_return],
    }
    return_frame = pd.DataFrame(ret_data)
    # Fetch borrow list in mysql
    sql = "SELECT * FROM borrows"
    c = mydb.cursor()
    c.execute(sql)
    result_borrows = c.fetchall()
    borrows_frame = pd.DataFrame(result_borrows, columns=[
                                 'acc_ID', 'acc_name', 'book_ID', 'book_name', 'date_issue', 'due_date'])
    # Lookup acc_name & book_name from borrows list
    return_list = pd.merge(left=return_frame, right=borrows_frame, how='left', left_on=[
                           'acc_ID', 'book_ID'], right_on=['acc_ID', 'book_ID'])
    return_list = return_list.drop_duplicates()
    acc_ID_merge = return_list.iloc[0, 0]
    book_ID_merge = return_list.iloc[0, 1]
    date_return_merge = return_list.iloc[0, 2]
    acc_name_merge = return_list.iloc[0, 3]
    book_name_merge = return_list.iloc[0, 4]
    date_issue_merge = return_list.iloc[0, 5]
    due_date_merge = return_list.iloc[0, 6]
    data = (acc_ID_merge, book_ID_merge, date_return_merge,
            acc_name_merge, book_name_merge, date_issue_merge, due_date_merge)
    if acc_ID_merge is not None:
        if dates <= due_date_merge:
            print("Thank you for returning the book")
        else:
            print("You are over the due date")
        sql1 = """INSERT INTO returns(acc_ID,book_ID,date_return,acc_name,
                book_name,date_issue,due_date) values(%s,%s,%s,%s,%s,%s,%s)"""
        cur = mydb.cursor()
        cur.execute(sql1, data)
        mydb.commit()
        bookup(book_ID, 1)

# Update book stock
def bookup(co, u):
    sql = "SELECT book_stock FROM books WHERE book_ID = %s"
    data2 = (co,)
    c = mydb.cursor()
    c.execute(sql, data2)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "UPDATE books SET book_stock = %s where book_ID = %s"
    d = (t, co)
    c.execute(sql, d)
    mydb.commit()
