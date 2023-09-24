'''
A simple module for working with 'n'th degree polynomials/expressions in form of string.
'''


def factorise(expression: str) -> list:
    '''Splits a expression into individual terms of degrees in 
    descending order from maximum degree term to constant.
    params:
        expression: The 'n'th degree expression to be split.
    returns:
        list with all the terms.
    '''
    splits = expression.split("+")
    # stack = []
    # for i in splits:
    #     stack.append(i)
    # return stack
    return splits
