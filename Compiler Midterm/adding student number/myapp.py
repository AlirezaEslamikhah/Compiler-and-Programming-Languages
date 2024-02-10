from antlr4 import *
from grammars.JavaLexer import JavaLexer
import os

input_address=input('Enter the f..... address : ')
student_number = input("your student number: ")

file_stream=FileStream(input_address)

lexer=JavaLexer(file_stream)
token=lexer.nextToken()
refactoredSTR=''


while token.type!=Token.EOF:
    if(token.type==lexer.COMMENT):
        # ("//" + token.text.strip("/*").replace("\n", "\n//"))
        # refactoredSTR+='/*'+token.text[2:]+'*/'
        refactoredSTR += token.text.replace("/*","/*"+student_number+" ")
    elif (token.type == lexer.LINE_COMMENT):
        refactoredSTR += token.text.replace("//", "//" + student_number+ " ")
    # elif token.type == JavaLexer.COMMENT and
    else:
        refactoredSTR+=token.text
    token=lexer.nextToken()


print(refactoredSTR+'\n')