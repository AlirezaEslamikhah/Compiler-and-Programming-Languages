from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParser import JavaParser
from Code.CodeSmellListener import CodeSmellListener
from io import StringIO

def main():
    # Example input: "3 + 4"
    # input_expression = input("Enter an arithmetic expression: ")
    # input_expression = input("Enter an arithmetic expression: ")
    file_path =".\input1.java"
    with open(file_path , 'r') as file:
        input_expression = file.read()
        # lines = file.readlines()

    # Create a lexer that feeds off the input expression
    lexer = JavaLexer(InputStream(input_expression))

    # Create a stream of tokens using the lexer
    token_stream = CommonTokenStream(lexer)

    # Create a parser that feeds off the token stream
    parser = JavaParser(token_stream)

    # Obtain the parse tree by invoking the parser's entry point
    # parse_tree = parser.start()#expression()
    parse_tree = parser.compilationUnit()#expression()

    # Create a custom listener object
    listener = CodeSmellListener

    # Walk the parse tree with the custom listener
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)

    # Get the result from the Listener
    # result = listener.result
    #
    # # Output the result
    # print("Result:", result)

# Call the main function
if __name__ == '__main__':
    main()
