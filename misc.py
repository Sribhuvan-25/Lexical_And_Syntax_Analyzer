import re
from typing import Union
from Stack import stack

def booleanEquation(equation):
    
    
    operators = [TList["LT"], TList["GT"], TList["GTE"], TList["LTE"], TList["EQ"], TList["NE"]]

    for i in range(0, len(operators)):
        
        hasToken = f' {operators[i]} ' in equation

        if not hasToken:
            continue

        expression1, expression2 = equation.split(operators[i])

        value1 = expression(expression1)
        value2 = expression(expression2)

        token = operators[i]

        if token == operators[0]:
            return value1 < value2
        
        if token == operators[1]:
            return value1 > value2
        
        if token == operators[2]:
            return value1 >= value2
        
        if token == operators[3]:
            return value1 <= value2
        
        if token == operators[4]:
            return value1 == value2
        
        if token == operators[5]:
            return value1 != value2

    raise Exception("Invalid boolean expression")

datatypes = {"XS", "S", "L", "XL"}

class BinaryNode:

    val: Union[str,int]

    def __init__(self, val = "") -> None:
        self.right = None
        self.left = None
        self.val = val
    


def tree(expression, node: BinaryNode):
    
    expression = expression.strip()
    if len(expression) == 0:
        return 
    if expression.isnumeric():
        node.val = int(expression)
        return
    
    index_plus = expression.find(f' {TList["ADD"]} ')
    index_minus = expression.find(f' {TList["SUB"]} ')
    index_mul = expression.find(f' {TList["MUL"]} ')
    index_div = expression.find(f' {TList["DIV"]} ')


    if index_plus != -1 or index_minus != -1 or index_mul != -1 or index_div != -1:
        node.left = BinaryNode("")
        node.right = BinaryNode("")
    else:
        if  expression not in stack or stack[expression][1] == None:
            raise Exception(f"{expression} does not exist")
        
        if stack[expression] != None:
            node.val = stack[expression][1]
        
        return 
    
    if index_plus != -1:
        node.val = TList["ADD"]
        tree(expression[0:index_plus], node.left)
        tree(expression[index_plus+2:], node.right)
        return 
    
    if index_minus != -1:
        node.val = TList["SUB"]
        tree(expression[0:index_minus], node.left)
        tree(expression[index_minus+2:], node.right)
        return 
    
    if index_mul != -1:
        node.val = TList["MUL"]
        tree(expression[0:index_mul], node.left)
        tree(expression[index_mul+2:], node.right)
        return 
    
    if index_div != -1:
        node.val = TList["DIV"]
        tree(expression[0:index_div], node.left)
        tree(expression[index_div+2:], node.right)
        return 
    


def solveTree(node: BinaryNode):
    if not node:
        return 0
    
    if type(node.val) is int:
        return node.val
    
    if node.val == TList["ADD"]:
        return solveTree(node.left) + solveTree(node.right)
    elif node.val == TList["SUB"]:
        return solveTree(node.left) - solveTree(node.right)
    elif node.val == TList["MUL"]:
        return solveTree(node.left) * solveTree(node.right)
    elif node.val == TList["DIV"]:
        denom = solveTree(node.right)
        if denom == 0:
            raise Exception("Division by Zero")
        return solveTree(node.left) / solveTree(node.right)


def expression(exp:str):
    exp = exp.strip()
    
    root = BinaryNode()

    tree(exp, root)
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
    
    return [statement[1:currentIndex-1], statement[currentIndex:]]

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