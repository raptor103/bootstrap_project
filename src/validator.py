class Validator:
    def _check_amount(self, amt: int):
        if amt <= 0:
            raise ValueError("Amount must be greater than zero.")

    def validate_deposit(self, amt: int):
        self._check_amount(amt)

    def validate_withdraw(self, balance: int, amt: int):
        self._check_amount(amt)
        if balance - amt <= 0:
            raise ValueError("Balance can´t be less than zero.")
