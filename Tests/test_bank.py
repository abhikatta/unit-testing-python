'''
Unit tests for the module Bank.

Tests Reqiured:
    proper working of creation, add to savings, withdraw
    when duplicate account is created => raise error
    when add to savings is less than 0 => raise error
    when withdraw money > account => raise error
'''
import pytest
from src.bank.main import Bank


class TestBank:
    '''
    Class for unit testing the Bank class and its methods.
    Tests Reqiured:
    proper working of creation, add to savings, withdraw
    when duplicate account is created => raise error
    when add to savings is less than 0 => raise error
    when withdraw money > account => raise error
    '''

    @pytest.fixture
    def bank(self):
        '''
        Returns an instance of the Bank.
        '''
        self.bank = Bank()
        return self.bank

    def test_proper_work(self, bank):
        '''
        Test for when everything is supposed to work when everything well.
        '''
        bank.create_account(account_id='acc1', initial_amount=100)
        assert bank.get_balance('acc1') == 100
        bank.withdraw(account_id='acc1', amount=50)
        assert bank.get_balance('acc1') == 50
        bank.add_to_savings(account_id='acc1', amount=200)
        assert bank.get_balance('acc1') == 250

    def test_duplicacy(self, bank):
        '''
        Test for checking duplicacy when duplicate accounts are tried to 
        be created.
        '''
        bank.create_account(account_id='acc2', initial_amount=202)
        with pytest.raises(ValueError):
            assert bank.create_account(
                account_id='acc2', initial_amount=202)

    def test_duplicacy2(self, bank):
        '''
        Test 2 for checking duplicacy when duplicate accounts are tried to 
        be created.
        '''
        bank.create_account(account_id='acc3', initial_amount=202)
        with pytest.raises(ValueError):
            assert bank.create_account(
                account_id='acc3', initial_amount=202)

    def test_negative_deposit(self, bank):
        '''
        Test for the method add_to_savings, should raise error when incorrect parameters are passed.
        '''

        with pytest.raises(ValueError):
            assert bank.add_to_savings(account_id='acc1', amount=-100)

    def test_withdraw_more_than_available(self, bank):
        '''
        Test for the method add_to_savings, should raise error when incorrect parameters are passed.
        '''
        with pytest.raises(ValueError):
            assert bank.withdraw('acc1', amount=400)
