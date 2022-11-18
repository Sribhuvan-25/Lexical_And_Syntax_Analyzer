import re
import Stack
from misc import Tokens
from misc import Expression
import Statement


def assign(statement):
    rmatch = re.match(r'([^;]+);(.*)', statement, re.M|re.I)
    assignStatement, restStatement = rmatch

    variable, expression = assignStatement.split(Tokens.ASSIGN)

    variable = variable.trim()
    expression = expression.trim()

    Stack.stack[variable][1] = Expression(expression)
    Statement(restStatement.trim())
    
