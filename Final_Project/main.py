from antlr4 import *
from Gen.JavaParser import JavaParser
from Gen.JavaLexer import JavaLexer
from Code.CustomAlirezaListener import CustomListener


def main():
    # file_path = ".\JavaCode.txt"
    file_path = "input1_Alireza.txt"
    with open(file_path, 'r') as file:
        input_expression = file.read()

    # Create a lexer that feeds off the input expression
    lexer = JavaLexer(InputStream(input_expression))

    # Create a stream of tokens using the lexer
    token_stream = CommonTokenStream(lexer)

    # Create a parser that feeds off the token stream
    parser = JavaParser(token_stream)

    # Obtain the parse tree by invoking the parser's entry point
    parse_tree = parser.compilationUnit()

    # Create a custom listener object
    listener = CustomListener()

    # Walk the parse tree with the custom listener
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)


    listener.flexbility_factcor() ###The flexibility factor
    listener.complexity_factor()  ### The Complexity factor


# Call the main function
if __name__ == '__main__':
    main()
