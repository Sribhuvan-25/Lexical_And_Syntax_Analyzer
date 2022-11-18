import Stack
import Statement

def declaration(statement):
    rmatch = re.match(r'([^;]+);(.*)', statement, re.M|re.I)
    declarationStatement, restStatement = rmatch

    vType, variable = declarationStatement.split(" ")

    vType = vType.trim()
    variable = variable.trim()

    if Stack.stack[variable] != None:
        raise Exception("{} is already present".format(variable))

    Stack.stack[variable] = [vType, None]
    Statement(restStatement.trim())