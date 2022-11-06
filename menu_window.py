from tkinter import *
from tkinter import messagebox
from login_window import client
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="mybank")
cursor = mydb.cursor()


class MenuPage:
    def __init__(self, master):
        master.geometry("480x480")
        master.config(bg="gray")

        self.title_label = Label(master, text="Please select \n your transaction", font=("Ariel", 15, 'bold'),
                                 bg="gray")
        self.title_label.place(x=140, y=50, width=200, height=50)

        self.balance_inquiry_button = Button(master, text="Balance Inquiry", font=("Ariel", 14, 'bold'),
                                             bg="#d63718", activebackground="#d63718",
                                             fg="white",
                                             command=self.balance_inquiry)
        self.balance_inquiry_button.place(x=150, y=120, width=170, height=40)

        self.deposit_Cash_button = Button(master, text="Deposit ", font=("Ariel", 14, 'bold'),
                                          bg="#d63718", activebackground="#d63718", command=self.deposit_cash,
                                          fg="white")
        self.deposit_Cash_button.place(x=150, y=180, width=170, height=40)

        self.cash_withdrawal_button = Button(master, text="Cash Withdrawal ", font=("Ariel", 14, 'bold'),
                                             bg="#d63718", activebackground="#d63718", command=self.cash_withdrawal,
                                             fg="white")
        self.cash_withdrawal_button.place(x=150, y=240, width=170, height=40)

        self.transfers_button = Button(master, text=" Transfers ", font=("Ariel", 14, 'bold'),
                                       bg="#d63718", activebackground="#d63718", command=self.transfers,
                                       fg="white")
        self.transfers_button.place(x=150, y=300, width=170, height=40)

        self.exit_button = Button(master, text="Exit", font=("Ariel", 14, 'bold'), bg="black",
                                  activebackground="#d63718", command=exit,
                                  fg="white")
        self.exit_button.place(x=150, y=360, width=100, height=30)

    # Balance Inquiry button
    # checks into the database the balance for the current client
    # return a message with client's balance
    def balance_inquiry(self):
        query = "Select balance from clients where CardNumber = '" + client.card + "';"
        cursor.execute(query)
        result = cursor.fetchone()
        client.sold = int(result[0])  # convert the tuple resulted into int
        mydb.commit()

        messagebox.showinfo(message="Your current balance is " + str(client.check_balance()) + " euros")

    # opens the window where the client can deposit cash
    def deposit_cash(self):
        window = Tk()
        from deposit_window import AmountPage
        deposit_w = AmountPage(window)

    # opens the window where the client can withdraw cash
    def cash_withdrawal(self):
        window = Tk()
        from withdraw_window import AmountPage
        deposit_w = AmountPage(window)

    # opens the window where the client can transfer cash
    def transfers(self):
        window = Tk()
        from money_transfer import Transfer
        transfer = Transfer(window)
