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
    bank.withdraw(accountID='acc1', withdraw_money=50)
    assert bank.get_balance('acc1') == 50
    bank.add_to_savings(accountID='acc1', debit_money=200)
    assert bank.get_balance('acc1') == 250


def test_duplicacy(bank):
    bank.create_account(accountID='acc2', initial_amount=202)
    with pytest.raises(ValueError):
        assert bank.create_account(accountID='acc2', initial_amount=202)


def test_duplicacy2(bank):
    bank.create_account(accountID='acc3', initial_amount=202)
    with pytest.raises(ValueError):
        assert bank.create_account(accountID='acc5', initial_amount=202)


def test_negative_deposit(bank):
    with pytest.raises(ValueError):
        assert bank.add_to_savings(accountID='acc1', debit_money=-100)


def test_withdraw_more_than_available(bank):
    with pytest.raises(ValueError):
        assert bank.withdraw('acc1', withdraw_money=400)
