from tkinter import *


class Person:
    card = None
    pin = None
    name = None
    bank_account = None
    sold = None

    def check_balance(self):
        return self.sold

    def deposit_cash(self, cash):
        self.sold = self.sold + cash
        return self.sold

    def withdraw_cash(self, cash):
        self.sold = self.sold - cash
        return self.sold
