import mysql.connector
import re

def email_validation(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.[\w\.-]+$'
    return re.match(pattern, email)

def password_validation(password):
    return any(c.isdigit() for c in password) and any(c.isalpha() for c in password)


db_selection = input("Do you have an existing database?[yes/no] ")
if db_selection == 'yes':
    db_select = input("Please enter the name of your database: ")
    mydb = mysql.connector.connect(
        user="root",
        password="",
        database= str(db_select)
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE users (username VARCHAR(255), password VARCHAR(255))")
    while True:
        user_email = input("Enter your email: ")
        if not email_validation(user_email):
            print("Invalid email format. Example of valid format: example@domain.com")
            continue
        user_password = input("Enter your password (must contain letters and digits): ")
        if not password_validation(user_password):
            print("Password must contain both letters and digits.")
            continue
        mycursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (user_email, user_password))
        mydb.commit()
        print("User registered successfully!")
        break
    mydb.close()

elif db_selection == 'no':
    db_create = input("Please enter a name for your database to be created: ")
    mydb = mysql.connector.connect(user="root",
                                   password="")
    mycursor = mydb.cursor()
    mycursor.execute(f"CREATE DATABASE {db_create}")
    mydb = mysql.connector.connect(user="root",
                                   password="",
                                   database= str(db_create))
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE users (username VARCHAR(255), password VARCHAR(255))")
    while True:
        user_email = input("Enter your email: ")
        if not email_validation(user_email):
            print("Invalid email format. Example of valid format: example@domain.com")
            continue
        user_password = input("Enter your password (must contain letters and digits): ")
        if not password_validation(user_password):
            print("Password must contain both letters and digits.")
            continue
        mycursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (user_email, user_password))
        mydb.commit()
        print("User registered successfully!")
        break
    mydb.close()
