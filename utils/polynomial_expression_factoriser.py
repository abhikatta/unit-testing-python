'''
A simple module for working with 'n'th degree polynomials/expressions in form of string.
'''


class ExpressionFactoriser:
    def __init__(self) -> None:
        pass
    '''
    The Class for working with 'n'th degree polynomials/expressions in form of string.
    '''

    @staticmethod  # because the self is not required here as its a single function, just like the same problem in C#
    def factorise(expression: str) -> list:
        '''Splits a expression into individual terms of degrees in 
        descending order from maximum degree term to constant.
        params:
            expression: The 'n'th degree expression to be split.
        returns:
            list with all the terms.
        '''
        stack = []
        splits = expression.split("+")
        for i in splits:
            stack.append(i)
        return stack
