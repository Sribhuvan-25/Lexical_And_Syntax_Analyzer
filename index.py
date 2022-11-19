import os
import sys
import re
from Statements import statement
from Stack import stack

def main():
    # file_dir = os.path.dirname(__file__)
    # str = sys.path.append(file_dir)
    # working_directory = os.getcwd()
    # exceCode = str(open(working_directory,"r")).strip().replace("\n", " ")
    # exceCode = re.sub("\s+", " ", exceCode)


    text = open('test.slang', 'r', encoding='utf-8').read()
    text = text.replace("\n", " ")
    text = re.sub('\s+', " ", text)
    text = re.findall(r'Start (.*) End', text)[0]
    

    # text = open("test.slang", "r") 
    # text = text.readlines()
    # result = re.findall("Start (.*) End", text)
    # st = result[0]
    statement(text)
    print(stack)

main()
