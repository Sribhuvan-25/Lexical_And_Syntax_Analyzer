import Stack
import Statement
import os
import re

def main():
    # filename = "test.slang"
    filepath = os.path.realpath(filename)
    exceCode = open(filepath,"r").trim().replace("\n", " ").replace(re.match(r'\s+', re))
    result = ""
    statement = ""
    Statement.statement(statement)
    print(Stack.stack)
    