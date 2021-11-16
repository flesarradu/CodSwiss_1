import mysql.connector
from LoginPage import *
list = []

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bazaswiss"
)
mycursor = mydb.cursor()

print(mydb)
def main():
    app = LoginPage()
    app.mainloop()



if __name__ == "__main__":
    main()



