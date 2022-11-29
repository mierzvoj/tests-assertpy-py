import string
import unittest
import assertpy
import sys

from assertpy import assert_that


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


    def test_account_balance_equals_zero(self):
        self.assertEqual(self.test_account.get_balance(), 0.0, msg="equal")

    def test_account_balance_positive(self):
        self.test_account.credit(100)
        self.assertEqual(self.test_account.get_balance(), 100, msg="equal")

    def test_account(self):
        self.assertRaises(Exception, self.test_account.withdraw(150))

    def test_account_owner(self):
        self.test_account.set_owner("Mr White")
        self.assertEqual(self.test_account.get_owner(), "Mr White", msg="correct")

    def test_account_owner_swap(self):
        self.test_account.set_owner("Mr Pink")
        self.assertEqual(self.test_account.get_owner(), "Mr Pink", msg="correct")

    def test_account_no_for_twenty_six_digits(self):
        length = len(self.test_account.get_acc_no())
        print(length)
        self.assertEqual(length, 26)

    def test_acc_no_format(self):
        assert_that(self.test_account.get_acc_no()).is_length(26).starts_with('12').ends_with('56')

    def test_acc_is_digit(self):
        assert_that(self.test_account.get_acc_no()).is_digit()

    def tearDown(self):
        self.test_account = None
