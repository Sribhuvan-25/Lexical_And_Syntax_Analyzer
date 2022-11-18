from misc import Tokens
import Statement
from misc import InsideBrackets
from misc import BooleanEquation


def condition(statement):
    statement = statement.replace("cond", "")

    [booleanStatement, restStatement] = InsideBrackets.insideBrackets(statement, Tokens.OPEN, Tokens.CLOSE)
    [insideStatement, restStatement] = InsideBrackets.insideBrackets(restStatement.trim(), Tokens.CODEBLOCKSTART, Tokens.CODEBLOCKEND)

    if BooleanEquation(booleanStatement):
        Statement.statement(insideStatement)

    Statement.statement(restStatement)