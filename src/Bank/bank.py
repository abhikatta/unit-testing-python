class Bank:
    def __init__(self) -> None:
        self.accounts = {}

    def create_account(self, accountID: str, initial_amount: int or float):
        if accountID in self.accounts:
            raise ValueError(
                'Account ID already in use!')
        if initial_amount > 0:
            self.accounts[accountID] = initial_amount
        else:
            raise ValueError(
                'Insufficient deposit. Deposit more than 2$ for creating an account')

    def add_to_savings(self, accountID: str, debit_money: int or float):
        if accountID not in self.accounts:
            raise ValueError(f'No account found with account ID:{accountID}')
        if debit_money > 0:
            self.accounts[accountID] += debit_money
        else:
            raise ValueError(
                'Insufficient deposit. Deposit more than 1$ for debiting money into the account')

    def withdraw(self, accountID: str, withdraw_money: int or float):
        if accountID not in self.accounts:
            raise ValueError(f'No account found with account ID:{accountID}')
        if withdraw_money > self.accounts[accountID]:
            raise ValueError(
                f'Insufficient deposit. Credit amount exceeding existing balance of {self.accounts[accountID]}$')
        elif withdraw_money < 0:
            raise ValueError(
                f'Incorrect Withdraw amount of {withdraw_money}$.')
        else:
            self.accounts[accountID] -= withdraw_money
            print(
                f"Withdrawn {withdraw_money}$. Remaining balance :{self.accounts[accountID]}$.")

    def get_balance(self, accountID):
        if accountID in self.accounts:
            return self.accounts[accountID]
        else:
            raise ValueError("Invalid account ID.")
