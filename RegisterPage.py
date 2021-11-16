import tkinter
from functools import partial
from tkinter import *
from tkinter import messagebox

import main
from User import User


class RegisterPage(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.geometry('300x150')
        self.title('Interfata de register')
        usernameLabelR = Label(self, bg='#64e1e8', text="User Name").grid(row=0, column=0)
        user = StringVar()
        usernameEntryR = Entry(self, textvariable=user).grid(row=0, column=1)
        passwordLabel = Label(self, text="Password").grid(row=1, column=0)
        passs = StringVar()
        passwordEntryR = Entry(self, textvariable=passs, show='•').grid(row=1, column=1)
        register = partial(self.register, user, passs)
        loginButton = Button(self, bg='#64e1e8', text="Register", command=register).grid(row=4, column=0)
        button2Click = partial(self.button2Click)
        button2 = Button(self, bg='#64e1e8', text="Exit", command=button2Click).grid(row=5, column=0)

    def register(self, username, password):
        print(username.get(), password.get())
        if len(username.get()) < 3:
            messagebox.showerror("ERROR", "Numele de utilizator este prea scurt (<3 caractere)!")
            return
        if len(password.get()) < 5:
            messagebox.showerror("ERROR", "Parola este prea scurta (<5 caractere)!")
            return
        u = User(username.get(), password.get())
        main.list.append(u)
        messagebox.showinfo("INFO", f"Userul {u.username} a fost adaugat cu succes")

    def button2Click(self):
        self.destroy()
        return
