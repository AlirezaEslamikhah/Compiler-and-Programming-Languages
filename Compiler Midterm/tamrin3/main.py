



from  antlr4 import  *
from gen.gramLexer import gramLexer
from  gen.gramParser import gramParser
from gen.gramListener import gramListener
import os

fileAddress = input("Enter File Address: ")


lexer =gramLexer(FileStream(fileAddress))
token = lexer.nextToken()
mod = ''
while(token.type != Token.EOF):
    if(token.type == lexer.COMMENT):
       mod += "#BayatKhani " + token.text[1:] + " 99521136"
    else:
        mod += token.text

    token = lexer.nextToken()
print(mod)

lexer =gramLexer(FileStream(fileAddress))
paresr = gramParser(CommonTokenStream(lexer))
tree = paresr.start()
listener = gramListener()
walker = ParseTreeWalker()


try:
    walker.walk(listener, tree)
    # type_ = listener.type

except Exception as e:
        print(e)





