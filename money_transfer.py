from tkinter import *
import tkinter.messagebox
import mysql.connector
from login_window import client

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="mybank")
cursor = mydb.cursor()


class Transfer:
    def __init__(self, master):
        self.master = master
        master.config(bg="gray")
        master.geometry("300x280")
        master.title("TRANSFER")
        self.master.resizable(0, 0)

        self.label1 = Label(master, text="Bank Account", font=("Ariel", 10, 'bold'), background="gray")
        self.label1.place(x=10, y=40, width=100, height=30)

        self.entry1 = Entry(master)
        self.entry1.place(x=10, y=70, width=260, height=25)

        self.label2 = Label(master, text="Quantity", font=("Ariel", 10, 'bold'), background="gray")
        self.label2.place(x=5, y=100, width=100, height=30)

        self.entry2 = Entry(master)
        self.entry2.place(x=10, y=130, width=260, height=25)

        self.ok_button = Button(master, text="OK", font=("Ariel", 10, 'bold'), bg="#d63718", activebackground="#d63718",
                                fg="white", command=self.ok)
        self.ok_button.place(x=20, y=170, width=60, height=30)

        self.exit_button = Button(master, text="EXIT", font=("Ariel", 10, 'bold'), bg="black", activebackground="black",
                                  fg="white", command=self.master.withdraw)
        self.exit_button.place(x=90, y=170, width=60, height=30)

    # OK button
    # Transfer the quantity into the client's given BankAccount
    # update into the database the new balances for both clients, the one who made the
    # transfer and the one who receives the transfer
    def ok(self):
        bank_account = self.entry1.get()
        quantity = self.entry2.get()

        query = "Select BankAccount from clients"
        cursor.execute(query)
        result = cursor.fetchall()

        if tuple([bank_account]) in result:
            if quantity == "":
                tkinter.messagebox.showinfo(message="Enter the quantity you wish to transfer")
            else:
                query = "UPDATE  clients SET Balance = Balance + '" + quantity + "' WHERE BankAccount" \
                                                                                 " ='" + bank_account + "' ";
                cursor.execute(query)
                mydb.commit()
                tkinter.messagebox.showinfo(message="Bank transfer successfully completed!")

                query = "Select balance from clients where CardNumber = '" + client.card + "';"
                cursor.execute(query)
                result = cursor.fetchone()
                client.sold = int(result[0])  # convert into int the tuple resulted
                client.sold = client.sold - int(quantity)

                query = "UPDATE clients SET Balance = '" + str(
                    client.sold) + "' where CardNumber = '" + client.card + "' "
                cursor.execute(query)
                mydb.commit()
        else:
            tkinter.messagebox.showinfo(message="The Bank Account doesn't exists!")

