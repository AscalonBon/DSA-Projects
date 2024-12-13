class CDAccount:
    def __init__(self, balance, interest_rate, term):
        self.balance = balance
        self.interest_rate = interest_rate
        self.term = term

def double_interest(old_account):
    return CDAccount(
        old_account.balance,
        old_account.interest_rate * 2,
        old_account.term
    )

def account_balance(account):
    rate_fraction = account.interest_rate / 100.0
    interest = account.balance * (rate_fraction * (account.term / 12.0))
    account.balance += interest

def validate_input(prompt, value_type=float, condition=None, error_message="Invalid input."):
    while True:
        try:
            value = value_type(input(prompt))
            if condition and not condition(value):
                raise ValueError(error_message)
            return value
        except ValueError:
            print(error_message)

if __name__ == "__main__":
    balance = validate_input(
        "Enter account balance: Php ", float,
        condition=lambda x: x > 0,
        error_message="Balance must be a positive number."
    )
    interest_rate = validate_input(
        "Enter account interest rate: ", float,
        condition=lambda x: x >= 0,
        error_message="Interest rate cannot be negative."
    )
    term = validate_input(
        "Enter the number of months until maturity: ", int,
        condition=lambda x: x > 0,
        error_message="Term must be a positive integer greater than 0."
    )

    account = CDAccount(balance, interest_rate, term)
    account_balance(account)

    print("\nOld Account")
    print(f"When your CD matures in \n{account.term} months,\nit will have a balance of Php {account.balance:.2f}")

    new_account = double_interest(account)
    account_balance(new_account)

    print("\nNew Account")
    print(f"When your CD matures in \n{new_account.term} months,\nit will have a balance of Php {new_account.balance:.2f}")