
'''
Test module for Expression Factoriser
'''
import pytest
from utils.polynomial_expression_factoriser import ExpressionFactoriser


class TestExpressionFactoriser:
    '''
    Class for unit testing the Polynomial Expression Factoriser class.
    '''
    @pytest.fixture
    def facto(self) -> ExpressionFactoriser:
        """Create and return an object of class ExpressionFactoriser.
        Returns:
            object: An object of class ExpressionFactoriser.
        """
        self.facto = ExpressionFactoriser()
        return self.facto

    def test_factorise(self, facto):
        '''Test 1 for splitting terms in polynomial expression.'''
        assert facto.factorise(expression="x^2+2x+1") == ['x^2', '2x', '1']

    def test_factorise2(self, facto):
        '''Test 2 for splitting terms in polynomial expression.'''
        assert facto.factorise(
            expression='x^3+2x^2+9x+12') == ['x^3', '2x^2', '9x', '12']
