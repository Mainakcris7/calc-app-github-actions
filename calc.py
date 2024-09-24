# Addition
def add(*args):
    '''
    Returns the sum of n numbers
    '''
    return sum(args)


# Multiplication
def multiply(*args):
    '''
    Returns the multiplication of n numbers
    '''
    result = 1
    for i in args:
        result *= i
    return result


# Division
def divide(a, b):
    '''
    Returns the division result of 2 numbers
    '''
    return a/b


# Subtraction
def subtract(a, b):
    '''
    Returns the subtraction result of 2 numbers
    '''
    return a - b


# Evaluate expression
def evaluate(expression: str):
    '''
    Evaluates an expression
    '''
    return eval(expression)
