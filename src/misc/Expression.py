import Tokens
import Stack
from typing import Union
import re

class BinaryNode:
    left:BinaryNode
    right: BinaryNode
    val: Union[str,int]

    def __init__(self, val = "") -> None:
        self.val = val


def tree(expression, node: BinaryNode):
    if isnumeric(expression):
        node.val = int(expression)
        return;
    
    expression = expression.trim()

    index_plus = expression.index(f' {Tokens.ADD} ')
    index_minus = expression.index(f' {Tokens.SUB} ')
    index_mul = expression.index(f' {Tokens.MUL} ')
    index_div = expression.index(f' {Tokens.DIV} ')


    if index_plus != -1 or index_minus != -1 or index_mul != -1 or index_div != -1:
        node.left = BinaryNode("")
        node.right = BinaryNode("")
    else:
        if Stack.stack[expression] == None or Stack.stack[expression][1] == None:
            raise Exception("Variable does not exist")
        
        if Stack.stack[expression] != None:
            node.val = Stack.stack[expression][1]
        
        return 
    
    if index_plus != -1:
        node.val = Tokens.ADD
        tree(statement.substring(0,index_plus), node.left)
        tree(statement.substring(index_plus+2), node.right)
        return 
    
    if index_minus != -1:
        node.val = Tokens.SUB
        tree(statement.substring(0,index_minus), node.left)
        tree(statement.substring(index_minus + 2), node.right)
        return 
    
    if index_mul != -1:
        node.val = Tokens.MUL
        tree(statement.substring(0,index_mul), node.left)
        tree(statement.substring(index_mul+2), node.right)
        return 
    
    if index_div != -1:
        node.val = Tokens.DIV
        tree(statement.substring(0,index_div), node.left)
        tree(statement.substring(index_div + 2), node.right)
        return 
    

def solveTree(node: BinaryNode):
    if not node:
        return 0
    
    if type(node.val) is int:
        return node.val
    
    if node.val == Token.ADD:
        return solveTree(node.left) + solveTree(node.right)
    elif node.val == Token.SUB:
        return solveTree(node.left) - solveTree(node.right)
    elif node.val == Token.MUL:
        return solveTree(node.left) * solveTree(node.right)
    else:
        return solveTree(node.left) / solveTree(node.right)


def Expression(expression):
    expression = expression.trim()

    isValidExp = re.match(r'(-?\d|[a-zA-Z])*( [+|-|*|\/] (-?\d+|[a-zA-Z]+))*', statement, re.M|re.I)

    if not isValidExp or len(isValidExp[0]) != len(expression):
        raise Exception("Invaid Expression")
    
    root = BinaryNode()

    tree(expression, root)
    return solveTree(root)

