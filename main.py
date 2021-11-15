from tkinter import *
from functools import partial


def validateLogin(user, password):
    if(user.get()=="flesar" and password.get()):
        print("succes")
    else:
        print("wrong user/pass")
    print("username entered :", user.get())
    print("password entered :", password.get())
    return


tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Login Form')

usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()

