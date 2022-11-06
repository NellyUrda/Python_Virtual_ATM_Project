from tkinter import *
from tkinter import messagebox
from login_window import client
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="mybank")
cursor = mydb.cursor()


class AmountPage:
    def __init__(self, master):
        self.master = master
        master.geometry("300x280")
        master.config(bg="gray")
        master.title(" CASH WITHDRAWAL")

        self.title_label = Label(master, text="Select amount", font=("Ariel", 15, 'bold'), bg="gray")
        self.title_label.place(x=60, y=10, width=150, height=50)

        self.button1 = Button(master, text="100€", font=("Ariel", 10, 'bold'), bg="#d63718", activebackground="#d63718",
                              fg="white", command=self.button1)
        self.button1.place(x=50, y=70, width=60, height=30)

        self.button2 = Button(master, text="50€", font=("Ariel", 10, 'bold'), bg="#d63718", activebackground="#d63718",
                              fg="white", command=self.button2)
        self.button2.place(x=140, y=70, width=60, height=30)

        self.button3 = Button(master, text="80€", font=("Ariel", 10, 'bold'), bg="#d63718", activebackground="#d63718",
                              fg="white", command=self.button3)
        self.button3.place(x=50, y=120, width=60, height=30)

        self.button4 = Button(master, text="20€", font=("Ariel", 10, 'bold'), bg="#d63718", activebackground="#d63718",
                              fg="white", command=self.button4)
        self.button4.place(x=140, y=120, width=60, height=30)

        self.quantity_label = Label(master, text="Quantity", font=("Ariel", 12, 'bold'), bg="gray")
        self.quantity_label.place(x=30, y=160, width=100, height=50)

        self.quantity_entry = Entry(master)
        self.quantity_entry.place(x=120, y=170, width=60, height=25)

        self.ok_button = Button(master, text="OK", font=("Ariel", 10, 'bold'), bg="#d63718", activebackground="#d63718",
                                fg="white", command=self.ok)
        self.ok_button.place(x=50, y=210, width=60, height=30)

        self.back_button = Button(master, text="Back", font=("Ariel", 10, 'bold'), bg="black",
                                  activebackground="black",
                                  fg="white", command=self.back)
        self.back_button.place(x=120, y=215, width=60, height=25)

    # OK button
    # the client enters the quantity he wishes to withdraw
    # the database updates with the new client's balance
    def ok(self):
        try:
            query = "Select balance from clients where CardNumber = '" + client.card + "';"
            cursor.execute(query)
            result = cursor.fetchone()
            client.sold = int(result[0])  # convert the tuple resulted in int

            amount = int(self.quantity_entry.get())
            current_balance = str(client.withdraw_cash(amount))
            self.quantity_entry.delete(0, END)
            messagebox.showinfo(message="Quantity withdraw successfully! ")

            query = "UPDATE clients SET Balance = '" + current_balance + "' WHERE CardNumber = " \
                                                                         "'" + client.card + "';"
            cursor.execute(query)
            mydb.commit()  # saves the changes in the db
        except Exception:
            messagebox.showinfo(message="Enter the quantity you wish to withdraw.")


    def back(self):
        self.master.withdraw()

    def button1(self):
        amount = 100
        self.quantity_entry.insert(0, amount)
        client.withdraw_cash(amount)

    def button2(self):
        amount = 50
        self.quantity_entry.insert(0, amount)
        client.withdraw_cash(amount)

    def button3(self):
        amount = 80
        self.quantity_entry.insert(0, amount)
        client.withdraw_cash(amount)

    def button4(self):
        amount = 20
        self.quantity_entry.insert(0, amount)
        client.withdraw_cash(amount)

