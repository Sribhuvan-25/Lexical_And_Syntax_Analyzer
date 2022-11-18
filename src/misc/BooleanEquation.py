import Expression
import Tokens

def BooleanEquation(equation):

    operators = [Tokens.GT, Tokens.LT, Tokens.GTE, Tokens.LTE, Tokens.EQ, Tokens.NE]

    for i in range(0, len(operators)):
        hasToken = "{}".format(operators[i]) in equation

        if not hasToken:
            continue

        expression1, expression2 = equation.split("{}".format(operators[i]))


        value1 = Expression(expression1)
        value2 = Expression(expression2)

        token = operators[i]

        if token == LT:
            return value1 < value2
        
        if token == LTE:
            return value1 <= value2
        
        if token == GT:
            return value1 > value2
        
        if token == GTE:
            return value1 >= value2
        
        if token == EQ:
            return value1 == value2
        
        if token == NE:
            return value1 != value2
    
    raise Exception("Invalid boolean expression")

