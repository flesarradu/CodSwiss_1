from functools import partial
from tkinter import *
from RegisterPage import RegisterPage
import main

class LoginPage(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x150')
        self.title('Interfata de logare')

        usernameLabel = Label(self, bg='#64e1e8', text="User Name").grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(self, textvariable=username).grid(row=0, column=1)

        passwordLabel = Label(self, text="Password").grid(row=1, column=0)
        password = StringVar()
        passwordEntry = Entry(self, textvariable=password, show='•').grid(row=1, column=1)

        validateLogin = partial(self.validateLogin, username, password)

        loginButton = Button(self, bg='#64e1e8', text="Login", command=validateLogin).grid(row=4, column=0)

        button2 = Button(self, bg='#64e1e8', text="Register", command=self.button2Click).grid(row=5, column=0)


    def validateLogin(self, user, password):

        main.mycursor.execute(f"SELECT PASSWORD FROM USERS WHERE USERNAME='{user.get()}'")
        result = main.mycursor.fetchall()

        if len(result) == 0:
            print("Wrong username")
            return
        if password.get() == result[0][0]:
            print("succes")
        else:
            print("Wrong pass")


        print("username entered :", user.get())
        print("password entered :", password.get())
        return

    def button2Click(self):
        self.withdraw()
        register = RegisterPage(self)
        register.grab_set()
        self.iconify()
        return
