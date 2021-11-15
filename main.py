from tkinter import *
from functools import partial
from tkinter import messagebox

class User:

    def __init__(self):
        self.username = "none"
        self.password = "none"

    def __init__(self, u,p):
        self.username = u
        self.password = p

    def checkPassword(self, passw):
        if(self.password == passw):
            return True
        return False


def validateLogin(user, password):
    u = User("flesar", "passwd")
    u1 = User("cristi", "pwdCristi")
    u2 = User("constantin", "pass")
    list = [u1,u2,u]
    b = False
    for var in list:
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

def button2Click():
    messagebox.showerror("Title","Ai apsat butonul 2")

tkWindow = Tk()
tkWindow.geometry('300x150')
tkWindow.title('Interfata de logare')


usernameLabel = Label(tkWindow, bg='#64e1e8', text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='•').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

loginButton = Button(tkWindow, bg='#64e1e8', text="Login", command=validateLogin).grid(row=4, column=0)

button2Click = partial(button2Click)
button2 = Button(tkWindow, bg='#64e1e8', text="Apasa-ma", command=button2Click).grid(row=5, column=0)

tkWindow.mainloop()

