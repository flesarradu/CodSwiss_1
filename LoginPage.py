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

        b = False
        for var in main.list:
            if user.get() == var.username:
                b = True
                if var.checkPassword(password.get()):
                    print("succes")
                else:
                    print("wrong pass")

        if not b:
            print("wrong user")

        print("username entered :", user.get())
        print("password entered :", password.get())
        return

    def button2Click(self):
        self.withdraw()
        register = RegisterPage(self)
        register.grab_set()
        self.iconify()
        return
