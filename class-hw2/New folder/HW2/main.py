import antlr4
from Gen.TypeCheckerLexer import TypeCheckerLexer
from Gen.TypeCheckerParser import TypeCheckerParser
from Gen.TypeCheckerListener import TypeCheckerListener
from Code.MyTypeCheckerListener import MyTypeCheckerListener

from io import StringIO

def main():
    # listener = TypeCheckerListener()
    listener = MyTypeCheckerListener()

    expression = input("Enter an expression: ")
    # expression = "2 + 3"
    input_stream = antlr4.InputStream(expression)
    lexer = TypeCheckerLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = TypeCheckerParser(stream)
    tree = parser.expr()

    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, tree)

    type = listener.get_type()
    # type = listener.type
    if type is not None:
        print(type)
    else:
        print("Type error")

if __name__ == "__main__":
    main()
