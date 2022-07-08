import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], ".."))
from account import Account

# this validator can be recreated in tests
# the point is that I can have a different class just for testing
# maybe my validator would need an API key, here I could create one just
# for testing purposes -> not import it
from validator import Validator
import pytest


def create_account(balance=0):
    account = Account(balance)
    return account


def test_deposit():
    account = create_account()
    account.deposit(100, Validator())
    assert account.return_balance() == 100


def test_withdraw():
    account = create_account(balance=500)
    account.withdraw(100, Validator())
    assert account.return_balance() == 400


def test_negative_withdraw():
    account = create_account()
    with pytest.raises(Exception) as info:
        account.withdraw(100, Validator())


def test_negative_deposit():
    account = create_account()
    with pytest.raises(Exception) as info:
        account.deposit(-100, Validator())


if __name__ == "__main__":
    test_negative_deposit()
