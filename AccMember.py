import itertools
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lms_project"
)


def AccountList():
    # Display account & membership maintenance menu
    print("""............ACCOUNT & MEMBERSHIP MAINTENANCE.............
    1.Add Account
    2.Delete Account
    3.Account List""")
    print("")
    option = input("Select your option[1-3] >>> ")
    if option > '0' and option < '4':
        # Add account
        if option == "1":
            print("Please fill the form below!")
            print("")
            acc_name = input("Enter your name >>> ")
            acc_prof = input("Enter your profession >>> ")
            # Fetch account list in mysql
            sql = "SELECT * FROM accounts"
            c = mydb.cursor()
            c.execute(sql)
            result_account = c.fetchall()
            if len(result_account) == 0:
                acc_ID = 1
                sql1 = "INSERT INTO accounts(acc_ID,acc_name,acc_prof) values(%s,%s,%s)"
                cur = mydb.cursor()
                data = (acc_ID, acc_name, acc_prof)
                cur.execute(sql1, data)
                mydb.commit()
                print("Completed! The account is successfully created.")
            elif len(result_account) > 0:
                # Fetch account list in mysql
                sql_row = "SELECT acc_ID FROM accounts ORDER BY acc_ID DESC LIMIT 1;"
                curs = mydb.cursor()
                curs.execute(sql_row)
                result_lastrow = c.fetchall()
                acc_ID = int(result_lastrow[0][0]) + 1
                sql1 = "INSERT INTO accounts(acc_ID,acc_name,acc_prof) values(%s,%s,%s)"
                cur = mydb.cursor()
                data = (acc_ID, acc_name, acc_prof)
                cur.execute(sql1, data)
                mydb.commit()
                print("Completed! The account is successfully created.")
            else:
                print("Error")
        # Delete account
        elif option == "2":
            print("To delete the account,please enter the account name!")
            print("")
            acc_name = input("Enter account name>>> ")
            # Fetch account list in mysql
            sql = "SELECT * FROM accounts"
            c = mydb.cursor()
            c.execute(sql)
            result_account = c.fetchall()
            for i in result_account:
                if acc_name == i[1]:
                    sql1 = "DELETE FROM accounts WHERE acc_name = %s"
                    data = (acc_name,)
                    cur = mydb.cursor()
                    cur.execute(sql1, data)
                    mydb.commit()
                    print("The account has been deleted.")
        # Display account list
        elif option == "3":
            sql = "SELECT * FROM accounts"
            c = mydb.cursor()
            c.execute(sql)
            result_account = c.fetchall()
            print('Account ID', '%14s' % 'Name', '%36s' % 'Profession',)
            print("-"*150)
            for i in result_account:
                print(
                    f"{str(i[0]):<20s} {str(i[1]):<30s} {str(i[2]):<20s}")
    else:
        print("Invalid input!!")
