# # test_bank.py
# import pytest
# from src.Bank.bank import Bank

# # Create a fixture for the bank
# @pytest.fixture
# def bank():

#     return Bank()

# # Test account creation
# def test_create_account(bank):
#     bank.create_account("acc1", 100)
#     assert bank.get_balance("acc1") == 100

# # Test deposit and withdrawal
# def test_deposit_and_withdraw(bank):
#     bank.create_account("acc2", 200)

#     # Deposit
#     bank.deposit("acc2", 50)
#     assert bank.get_balance("acc2") == 250

#     # Withdraw
#     bank.withdraw("acc2", 100)
#     assert bank.get_balance("acc2") == 150

# # Test invalid actions
# def test_invalid_actions(bank):
#     # Attempt to create an existing account
#     bank.create_account("acc3", 300)
#     with pytest.raises(ValueError):
#         bank.create_account("acc3", 500)

#     # Attempt to deposit a negative amount
#     with pytest.raises(ValueError):
#         bank.deposit("acc3", -50)

#     # Attempt to withdraw from a non-existent account
#     with pytest.raises(ValueError):
#         bank.withdraw("acc4", 100)

#     # Attempt to withdraw more than the balance
#     with pytest.raises(ValueError):
#         bank.withdraw("acc3", 400)


import pytest
from src.Bank.bank import Bank


@pytest.fixture
def bank():
    return Bank()

# Tests Reqiured:
# proper working of creation, add to savings, withdraw
# when duplicate account is created => raise error
# when add to savings is less than 0 => raise error
# when withdraw money > account => raise error


def test_proper_work(bank):
    bank.create_account(accountID='acc1', initial_amount=100)
    assert bank.get_balance('acc1') == 100


def test_duplicacy(bank):
    # bank.create_account(accountID='acc2', initial_amount=202)
    # with pytest.raises(ValueError):
    #     assert bank.create_account(accountID='acc2', initial_amount=202)
    bank.create_account("acc3", 300)
    with pytest.raises(ValueError):
        bank.create_account("acc3", 500)


def test_negative_deposit(bank):
    with pytest.raises(ValueError):
        assert bank.add_to_savings(accountID='acc1', debit_money=-100)


def test_withdraw_more_than_available(bank):
    with pytest.raises(ValueError):
        assert bank.withdraw('acc1', withdraw_money=400)
