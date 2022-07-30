import pandas as pd
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lms_project"
)


def RecordList():
 # Display records menu
    print("""............RECORDS.............
    1.Check Out (Borrow) Records
    2.Check In (Return) Records""")
    print("")
    option = input("Select your option[1-2] >>> ")
    print("")
    if option > '0' and option < '3':
        # Display Check Out (Borrow) Records
        if option == "1":
            # Fetch borrows list
            sql = "SELECT * FROM borrows"
            c = mydb.cursor()
            c.execute(sql)
            result_borrows = c.fetchall()
            result_borrows = pd.DataFrame(result_borrows, columns=[
                'acc_ID', 'acc_name', 'book_ID', 'book_name', 'date_issue', 'due_date'])
            result_borrows = result_borrows.drop_duplicates()
            # Fetch book stock from books list
            sql = "SELECT book_ID,book_cat,book_stock FROM books"
            d = mydb.cursor()
            d.execute(sql)
            result_bookstock = c.fetchall()
            result_bookstock = pd.DataFrame(result_bookstock, columns=[
                'book_ID', 'book_cat', 'book_stock'])
            # Looksup book stock from borrows list
            borrows_record = pd.merge(
                left=result_borrows, right=result_bookstock, how='left', left_on='book_ID', right_on='book_ID')
            print('Book ID', '%13s' % 'Book Title', '%48s' %
                  'Category', '%17s' % 'Stock')
            print("-"*150)
            for index, row in borrows_record.iterrows():
                book_ID = row["book_ID"]
                book_name = row["book_name"]
                book_cat = row["book_cat"]
                book_stock = row["book_stock"]
                print(
                    f"{str(book_ID):<10s} {str(book_name):<50s} {str(book_cat):<20s} {str(book_stock):<10s}")
        # DisplayCheck In (Return) Records
        elif option == "2":
            # Fetch returns list
            sql = "SELECT * FROM returns"
            c = mydb.cursor()
            c.execute(sql)
            returns_record = c.fetchall()
            return_frame = pd.DataFrame(returns_record, columns=[
                'acc_ID', 'book_ID', 'date_return', 'acc_name',
                'book_name', 'date_issue', 'due_date'])
            return_frame = return_frame.drop_duplicates()
            # Fetch book stock from books list
            sql = "SELECT book_ID,book_cat,book_stock FROM books"
            d = mydb.cursor()
            d.execute(sql)
            result_bookstock_2 = c.fetchall()
            result_bookstock_2 = pd.DataFrame(result_bookstock_2, columns=[
                'book_ID', 'book_cat', 'book_stock'])
            # Looksup book stock from borrows list
            borrows_record = pd.merge(left=return_frame, right=result_bookstock_2, how='left',
                                      left_on='book_ID', right_on='book_ID')
            print('Book ID', '%13s' % 'Book Title', '%48s' %
                  'Category', '%17s' % 'Stock')
            print("-"*150)
            for index, row in borrows_record.iterrows():
                book_ID = row["book_ID"]
                book_name = row["book_name"]
                book_cat = row["book_cat"]
                book_stock = row["book_stock"]
                print(
                    f"{str(book_ID):<10s} {str(book_name):<50s} {str(book_cat):<20s} {str(book_stock):<10s}")
