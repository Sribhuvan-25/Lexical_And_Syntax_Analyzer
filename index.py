import os
import sys
import re
from Statements import statement
from Stack import stack

def main():
   
    # Reads the file with the code
    filename = 'test.slang'
    text = open('test.slang', 'r', encoding='utf-8').read()
    text = text.replace("\n", " ")
    text = re.sub('\s+', " ", text)
    text = re.findall(r'Start (.*) End', text)[0] # Takes all the content between Start and End
    statement(text)
    print(stack)

main()
