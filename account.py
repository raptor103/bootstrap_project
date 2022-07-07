class Account:
    def __init__(self, balance=0) -> None:
        self.balance = balance

    def deposit(self, amt: int) -> int:
        self.balance = self.balance + amt
        return self.balance

    def withdraw(self, amt: int) -> int:
        self.balance = self.balance - amt
        return self.balance

    def show_balance(self):
        print("The balance is", self.balance)

    def return_balance(self):
        return self.balance


if __name__ == "__main__":
    account = Account()
    account.deposit(100)
    print(account.return_balance())




