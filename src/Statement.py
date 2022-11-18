import Stack
from misc import DataTypes
from misc import Tokens
from Statements import Declaration
from Statements import Assign
from Statements import Condition
from Statements import Loop
import re

def statement(statement):
    statement = statement.trim()

    if not statement:
        return
    
    regex_intialWord = re.match(r'^[a-zA-Z]* ', statement, re.M|re.I)

    if not regex_intialWord:
        raise Exception("Invalid Syntax")
    
    initalWord = regex_intialWord[0].trim()

    if initalWord in  DataTypes.datatypes :
        Declaration.declaration(statement)
    elif initalWord == Tokens.RERUN:
        Loop.loop(statement)
    elif initalWord == Tokens.COND:
        Condition.condition(statement)
    elif Stack.stack[initalWord] == None:
        Assign.assign(statement)
    else:
        raise Exception(f'{initalWord} is not defined')
    
    


