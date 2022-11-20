from misc import *

def statement(st):
    st = st.strip()

    if not st:
        return
    
    regex_intialWord = re.findall("^[a-zA-Z]* ", st)

    if not regex_intialWord:
        raise Exception("Invalid Syntax")
    
    initalWord = regex_intialWord[0].strip()

    if initalWord in  datatypes :
        declaration(st)

    elif initalWord == TList['RERUN']:
        loop(st)

    elif initalWord == TList['COND']:
        condition(st)

    elif initalWord in stack:
        assign(st)

    else:
        raise Exception(f'{initalWord} is not defined')


def assign(st):
   
    rmatch = re.findall("([^;]+);(.*)", st.strip())

    assignStatement = rmatch[0][0]
    restStatement = rmatch[0][1]

    variable, expr = assignStatement.split("=")

    variable = variable.strip()
    expr = expr.strip()

    stack[variable][1] = expression(expr)
    statement(restStatement.strip())

def condition(st):
    st = st.replace("cond ", "", 1)

    [booleanStatement, restStatement] = insideBrackets(st, TList["OPEN"], TList["CLOSE"])
    [insideStatement, restStatement] = insideBrackets(restStatement.strip(), TList["CODEBLOCKSTART"], TList["CODEBLOCKEND"])

    if booleanEquation(booleanStatement):
        statement(insideStatement)

    statement(restStatement)

def declaration(st):
    rmatch = re.split("([^;]+);(.*)", st.strip())
    
    stStatement = rmatch[1]
    restStatement = rmatch[2]
    

    vType, variable = stStatement.split(" ")

    vType = vType.strip()
    variable = variable.strip()

    if variable in stack:
        raise Exception("{} is already present".format(variable))

    stack[variable] = [vType, None]
    statement(restStatement.strip())

def loop(st):
    
    st = st.replace("rerun ", "", 1).strip()
    [boolStatement, restStatement] = insideBrackets(st, TList["OPEN"], TList["CLOSE"])
    [ifStatement, restStatement] = insideBrackets(restStatement.strip(), TList["CODEBLOCKSTART"], TList["CODEBLOCKEND"])

    while True:
        if booleanEquation(boolStatement):
            statement(ifStatement)
        else:
            break
    
    statement(restStatement)