from misc import Tokens
import Statement
from misc import InsideBrackets
from misc import BooleanEquation

def loop(statement):
    statement = statement.replace("rerun", "").trim()

    [booleanEquation, restStatement] = InsideBrackets.insideBrackets(statement, Tokens.OPEN, Tokens.CLOSE)
    [ifStatement, restStatement] = InsideBrackets.insideBrackets(restStatement.trim(), Tokens.CODEBLOCKSTART, Tokens.CODEBLOCKEND)

    while True:
        if BooleanEquation.booleanEquation(booleanEquation):
            Statement.statement(ifStatement)
        else:
            break
    
    Statement.statement(restStatement)
