from misc import *

def statement(st):
    st = st.strip()

    if not st:
        return
    
    regex_intialWord = re.findall("^[a-zA-Z]*", st)

    if not regex_intialWord:
        raise Exception("Invalid Syntax")
    
    initalWord = regex_intialWord[0].strip()

    if initalWord in  datatypes :
        declaration(st)

    elif initalWord == TList['RERUN']:
        loop(st)

    elif initalWord == TList['COND']:
        condition(st)

    elif stack[initalWord] == None:
        assign(st)

    else:
        raise Exception(f'{initalWord} is not defined')


def assign(st):
    
    rmatch = re.findall("([^;]+);(.*)", st)
    assignStatement, restStatement = rmatch

    variable, expr = assignStatement.split(TList.ASSIGN)

    variable = variable.strip()
    expr = expr.strip()

    stack[variable][1] = expression(expr)
    statement(restStatement.strip())

def condition(st):
    st = st.replace("cond", "")

    [booleanStatement, restStatement] = insideBrackets(st, TList.OPEN, TList.CLOSE)
    [insideStatement, restStatement] = insideBrackets(restStatement.strip(), TList.CODEBLOCKSTART, TList.CODEBLOCKEND)

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

    if stack[variable] != None:
        raise Exception("{} is already present".format(variable))

    stack[variable] = [vType, None]
    statement(restStatement.strip())

def loop(st):
    st = st.replace("rerun", "").strip()

    [booleanEquation, restStatement] = insideBrackets(statement, TList.OPEN, TList.CLOSE)
    [ifStatement, restStatement] = insideBrackets(restStatement.strip(), TList.CODEBLOCKSTART, TList.CODEBLOCKEND)

    while True:
        if booleanEquation(booleanEquation):
            statement(ifStatement)
        else:
            break
    
    statement(restStatement)