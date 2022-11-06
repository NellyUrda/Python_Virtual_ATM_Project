import tkinter
from tkinter import *
from tkinter import messagebox
from client import Person
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="mybank")
cursor = mydb.cursor()
client = Person()


class LoginPage:

    def __init__(self, master):
        self.master = master
        master.geometry("380x410")
        master.config(bg="gray")

        self.title_label = Label(master, text="Welcome to the \n ATM Machine", font=("Ariel", 14, 'bold'),
                                 bg="gray")
        self.title_label.place(x=120, y=70, width=160, height=50)

        self.card_label = Label(master, text="Card Number", font=("Ariel", 13, 'bold'), bg="gray")
        self.card_label.place(x=15, y=160, width=150, height=40)

        self.card_entry = Entry(master)
        self.card_entry.place(x=150, y=160, width=150, height=25)

        self.pin_label = Label(master, text="Pin Code", font=("Ariel", 13, 'bold'), bg="gray")
        self.pin_label.place(x=35, y=220, width=100, height=40)

        self.pin_entry = Entry(master, show="*")
        self.pin_entry.place(x=150, y=220, width=150, height=25)

        self.ok_button = Button(master, text="OK", font=("Ariel", 14, "bold"), bg="#d63718",
                                activebackground="#d63718",
                                command=self.ok,
                                fg="white")
        self.ok_button.place(x=165, y=265, width=60, height=30)

    # OK button
    # we check into the database if the client's card and pin introduced in entry box exists
    # if yes, we log in , ATM menu window opens
    def ok(self):
        try:
            client.card = self.card_entry.get()
            card = int(client.card)
            client.pin = self.pin_entry.get()

            query = "select cardNumber from clients;"
            cursor.execute(query)
            result1 = cursor.fetchall()

            query = "SELECT Pin from clients WHERE CardNumber = '" + client.card + "';"
            cursor.execute(query)
            result2 = cursor.fetchone()

            if tuple([card]) in result1:
                if int(client.pin) in result2:
                    self.master.withdraw()  # close login_window
                    window = Tk()
                    from menu_window import MenuPage
                    MenuPage(window)
                else:
                    tkinter.messagebox.showinfo(message="Wrong pin !")
            else:
                tkinter.messagebox.showinfo(message="Wrong card-number or pin!")
        except Exception:
            tkinter.messagebox.showinfo(message="Something went wrong!")
