import string
import unittest
import assertpy
import sys

from assertpy import assert_that
from assertpy import add_extension
from assertpy import contains


class BankAccount:
    def __init__(self, balance: float, owner: str, acc_no: str):
        self.balance = balance
        self.owner = owner
        self.initial_balance = 0
        self.acc_no = acc_no

    def set_acc_no(self, acc_no):
        self.acc_no = acc_no

    def get_acc_no(self) -> str:
        return self.acc_no

    def credit(self, deposit):
        self.balance = self.balance + deposit
        return self.balance

    def withdraw(self, withdrawal):
        try:
            self.balance = self.balance - withdrawal
            while self.balance < 0:
                break
        except Exception as e:
            print(e, "debit ahead")
        return self.balance

    def get_balance(self):
        return self.balance

    def get_owner(self):
        return self.owner

    def set_owner(self, o):
        self.owner = o


class AccountTest(unittest.TestCase):
    def setUp(self):
        self.test_account = BankAccount(0.0, "Tyler Durden", "12345678912345678911123456")

    def test_balance_is_150(self):
        self.test_account = BankAccount(150, "Tyler Durden", "12345678912345678911123456")
        if self.test_account.get_balance() != 150:
            return self.error(f'{self.test_account.get_balance()} is NOT 150!')
        return self

    add_extension(test_balance_is_150)

    def test_balance_150(self):
        assert_that(150).test_balance_is_150()

    def test_account_no_contains_digits(self):
        self.test_account = BankAccount(150, "Tyler Durden", "12345678912345678911123456")
        if self.test_account.get_acc_no() != "12345678912345678911123456":
            return self.error(f'{self.test_account.get_acc_no()} is inproper')
        return self

    add_extension(test_account_no_contains_digits)

    def test_acc_no_for_proper_digits(self):
        assert_that("12345678912345678911123456").test_account_no_contains_digits()

    def tearDown(self):
        self.test_account = None
