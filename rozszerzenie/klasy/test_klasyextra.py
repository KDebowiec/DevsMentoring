import pytest
from klasyextra import *


def test_account_balance_afer_creation():
    bank_account = BankAccount(1000)
    assert bank_account.balance == 1000


# def test_deposit_of_bank_account_after_creation():
#     bank_account = BankAccount()
#     bank_account.deposit()
#     assert bank_account.balance == 1234

def test_withdraw_of_bank_account_after_creation():
    bank_account = BankAccount(1000)
    bank_account.withdraw(500)
    assert bank_account.balance == 500


def test_charging_interest_after_creation():
    bookmark_account = BookmarkAccount(interest=0.5, account_balance=100)
    bookmark_account.charge_interest_amount()
    assert bookmark_account.account_balance == 150
