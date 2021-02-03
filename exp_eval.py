from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass
    
# Tuple used when checking if item on stack is an operator
operators = ("+", "-", "*", "/", "**")

def postfix_eval(input_str):
    '''Evaluates a postfix expression
    
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    !!!'''
    
    tokens = input_str.split()
    
    # Check to make sure input string is properly formatted
    numOperators = 0
    numOperands = 0
    for i in tokens:
        if i in operators:          # Compare token against operators tuple
            numOperators += 1
        else:
            try:
                float(i)            # Check that any tokens that aren't operators are numbers
            except ValueError:
                raise PostfixFormatException("Invalid token")
            numOperands += 1        # Only runs if exception isn't raised (token is a number)
    
    # There should always be one more operand than operator
    if numOperands < numOperators + 1:
        raise PostfixFormatException("Insufficient operands")
    if numOperands > numOperators + 1:
        raise PostfixFormatException("Too many operands")
    
    # Evaluate the postfix expression
    tokenStack = Stack(30)
    for i in tokens:
        if i in operators:                                  # Compare token against operators tuple
            secondValue = float(tokenStack.pop())           # Second value in expression
            firstValue = float(tokenStack.pop())            # First value in expression
            answer = DoMath(firstValue, secondValue, i)     # Helper function to evaluate expression
            tokenStack.push(answer)                         # Put number on stack
        else:
            tokenStack.push(i)                              # Put number on stack
    return float(tokenStack.pop())


def DoMath(first, second, operator):
    '''Helper function that does different operations based on the operator string
    input: 2 floats (first, second) and 1 string (operator)
    output: float'''
    
    if operator == "+":
        return first + second
    elif operator == "-":
        return first - second
    elif operator == "*":
        return first * second
    elif operator == "/":
        if second == 0:         # Dividing by zero raises an error
            raise ValueError
        return first / second
    else:
        return first ** second

def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    
    tokenStack = Stack(30)
    tokens = input_str.split()
    tempList = ["first", "second", "operator"]
    i = -1
    while i >= len(tokens) * -1:
        if tokens[i] in operators:
            tempList[0] = tokenStack.pop()
            tempList[1] = tokenStack.pop()
            tempList[2] = tokens[i]
            tokenStack.push(" ".join(tempList))
        else:
            tokenStack.push(tokens[i])
        i -= 1
    return tokenStack.pop()
