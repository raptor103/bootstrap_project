import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], ".."))
from account import Account
import pytest


def create_account(balance=0):
    account = Account(balance)
    return account


def test_deposit():
    account = create_account()
    account.deposit(100)
    assert account.return_balance() == 100


def test_withdraw():
    account = create_account(balance=500)
    account.withdraw(100)
    assert account.return_balance() == 400


if __name__ == "__main__":
    test_deposit()
