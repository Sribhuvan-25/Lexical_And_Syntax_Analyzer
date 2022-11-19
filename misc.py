import re
from typing import Union
from Stack import stack

def booleanEquation(equation):
    
    operators = [TList.GT, TList.LT, TList.GTE, TList.LTE, TList.EQ, TList.NE]

    for i in range(0, len(operators)):
        hasToken = "{}".format(operators[i]) in equation

        if not hasToken:
            continue

        expression1, expression2 = equation.split("{}".format(operators[i]))


        value1 = expression(expression1)
        value2 = expression(expression2)

        token = operators[i]

        if token == operators[0]:
            return value1 < value2
        
        if token == operators[1]:
            return value1 <= value2
        
        if token == operators[2]:
            return value1 > value2
        
        if token == operators[3]:
            return value1 >= value2
        
        if token == operators[4]:
            return value1 == value2
        
        if token == operators[5]:
            return value1 != value2
    
    raise Exception("Invalid boolean expression")

datatypes = {"XS", "S", "L", "XL"}

class BinaryNode:
    
    # left:BinaryNode
    # right: BinaryNode
    val: Union[str,int]

    def __init__(self, val = "") -> None:
        self.right = None
        self.left = None
        self.val = val


def tree(expression, node: BinaryNode):
    if expression.isnumeric():
        node.val = int(expression)
        return
    
    expression = expression.strip()

    index_plus = expression.index(f' {TList.ADD} ')
    index_minus = expression.index(f' {TList.SUB} ')
    index_mul = expression.index(f' {TList.MUL} ')
    index_div = expression.index(f' {TList.DIV} ')


    if index_plus != -1 or index_minus != -1 or index_mul != -1 or index_div != -1:
        node.left = BinaryNode("")
        node.right = BinaryNode("")
    else:
        if stack[expression] == None or stack[expression][1] == None:
            raise Exception("Variable does not exist")
        
        if stack[expression] != None:
            node.val = stack[expression][1]
        
        return 
    
    if index_plus != -1:
        node.val = TList.ADD
        tree(expression.substring(0,index_plus), node.left)
        tree(expression.substring(index_plus+2), node.right)
        return 
    
    if index_minus != -1:
        node.val = TList.SUB
        tree(expression.substring(0,index_minus), node.left)
        tree(expression.substring(index_minus + 2), node.right)
        return 
    
    if index_mul != -1:
        node.val = TList.MUL
        tree(expression.substring(0,index_mul), node.left)
        tree(expression.substring(index_mul+2), node.right)
        return 
    
    if index_div != -1:
        node.val = TList.DIV
        tree(expression.substring(0,index_div), node.left)
        tree(expression.substring(index_div + 2), node.right)
        return 


def solveTree(node: BinaryNode):
    if not node:
        return 0
    
    if type(node.val) is int:
        return node.val
    
    if node.val == TList.ADD:
        return solveTree(node.left) + solveTree(node.right)
    elif node.val == TList.SUB:
        return solveTree(node.left) - solveTree(node.right)
    elif node.val == TList.MUL:
        return solveTree(node.left) * solveTree(node.right)
    else:
        return solveTree(node.left) / solveTree(node.right)


def expression(expression):
    expression = expression.strip()

    isValidExp = re.findall("(-?\d|[a-zA-Z])*( [+|-|*|\/] (-?\d+|[a-zA-Z]+))*", expression)

    if not isValidExp or len(isValidExp[0]) != len(expression):
        raise Exception("Invaid Expression")
    
    root = BinaryNode()

    tree(expression, root)
    return solveTree(root)

def insideBrackets(statement, startBracket, endBracket):
    
    bracketCounter = 1
    currentIndex = 1

    while bracketCounter > 0 :
        if statement[currentIndex] == startBracket:
            bracketCounter += 1
        elif statement[currentIndex] == endBracket:
            bracketCounter -= 1

        currentIndex += 1
    
    return [statement.substring(1,currentIndex-1), statement.substring(currentIndex)]

TList = {
    'ASSIGN': "=",
    'END': "End",
    'START': "Start",
    'COND': "cond",
    'RERUN': "rerun",
    'ADD': "+",
    'SUB': "-",
    'MUL': "*",
    'DIV': "/",
    'MOD': "%",
    'FLRDIV': "$",
    'GT': ">",
    'LT': "<",
    'GTE': ">=",
    'LTE': "<=",
    'EQ': "==",
    'NE': "!=",
    'OPEN': "(",
    'CLOSE': ")",
    'CODEBLOCKSTART': "{",
    'CODEBLOCKEND': "}",
}