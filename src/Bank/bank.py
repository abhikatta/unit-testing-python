'''Some docstring about this Bank class'''


class Bank:
    '''Bank with operations for creating account, withdrawing amount,
        adding amount to savings, getting remaining balance. '''

    def __init__(self) -> None:
        self.accounts = {}

    def create_account(self, account_id: str, initial_amount: int or float) -> None:
        '''
        Creates a new bank account with account_id and initial_amount
        account_id: ID for the bank account.
        initial_amount: Funds to be deposited into the account when the account is created.
        returns None

        '''
        if account_id in self.accounts:
            raise ValueError('Account ID already in use!')
        if initial_amount < 0:
            raise ValueError(
                'Insufficient deposit.\
                Deposit more than 2$ for creating an account')
        self.accounts[account_id] = initial_amount

    def add_to_savings(self, account_id: str, amount: int or float):
        '''
        Adds amount to the account of account with id account_id.
        '''
        if account_id not in self.accounts:
            raise ValueError(f'No account found with account ID:{account_id}')
        if amount > 0:
            self.accounts[account_id] += amount
        else:
            raise ValueError(
                'Insufficient deposit.\
                Deposit more than 1$ for debiting money into the account')

    def withdraw(self, account_id: str, amount: int or float):
        '''Withdraw money from the bank of account passed as account_id.'''
        if account_id not in self.accounts:
            raise ValueError(f'No account found with account ID:{account_id}')
        if amount > self.accounts[account_id]:
            raise ValueError(
                f'Insufficient deposit.\
                Credit amount exceeding existing balance of {self.accounts[account_id]}$')
        if amount < 0:
            raise ValueError(
                f'Incorrect Withdraw amount of {amount}$.')
        self.accounts[account_id] -= amount
        print(
            f"Withdrawn {amount}$. \
            Remaining balance :{self.accounts[account_id]}$.")

    def get_balance(self, account_id):
        '''Print out the remaining balance in the bank account with account_id'''
        if account_id in self.accounts:
            return self.accounts[account_id]
        raise ValueError("Invalid account ID.")
