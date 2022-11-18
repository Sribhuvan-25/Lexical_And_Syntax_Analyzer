import Expression
import Tokens

def booleanEquation(equation):

    operators = [Tokens.GT, Tokens.LT, Tokens.GTE, Tokens.LTE, Tokens.EQ, Tokens.NE]

    for i in range(0, len(operators)):
        hasToken = "{}".format(operators[i]) in equation

        if not hasToken:
            continue

        expression1, expression2 = equation.split("{}".format(operators[i]))


        value1 = Expression.expression(expression1)
        value2 = Expression.expression(expression2)

        token = operators[i]

        if token == operators[0]:
            return value1 < value2
        
        if token == operators[1]:
            return value1 <= value2
        
        if token == operators[2]:
            return value1 > value2
        
        if token == operators[3]:
            return value1 >= value2
        
        if token == operators[4]:
            return value1 == value2
        
        if token == operators[5]:
            return value1 != value2
    
    raise Exception("Invalid boolean expression")

