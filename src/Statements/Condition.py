from misc import Tokens
import Statement
from misc import InsideBrackets
from misc import BooleanEquation


def condition(statement):
    statement = statement.replace("cond", "")

    [booleanEquation, restStatement] = InsideBrackets(statement, Tokens.OPEN, Tokens.CLOSE)
    [insideStatement, restStatement] = InsideBrackets(restStatement.trim(), Tokens.CODEBLOCKSTART, Tokens.CODEBLOCKEND)

    if BooleanEquation(booleanStatement):
        Statement(insideStatement)

    Statement(restStatement)