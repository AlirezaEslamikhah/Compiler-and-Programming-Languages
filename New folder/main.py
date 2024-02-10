from antlr4 import *
from Gen.JavaParser import JavaParser
from Gen.JavaLexer import JavaLexer
from Code.CustomAlirezaListener import CustomListener
from Code.CustomMahdiListener import ReadabilityMetricListener
from Code.saba import EjioguMetricsListener
from Code.CustomAliListener import HenryMetricListener
from Code.Albrecht import Albrecht
from Code.CustomAhmadrezaListener import CustomAhmadrezaListener


def calculate_comment_ratio(file_path):
    total_lines = 0
    comment_lines = 0

    with open(file_path, 'r') as file:
        for line in file:
            total_lines += 1
            line = line.strip()
            if line.startswith('#') or line.startswith('//') or line.startswith('/*') or line.startswith(
                    '*') or line.startswith('*/'):
                comment_lines += 1

    if total_lines == 0:
        return 0
    else:
        return comment_lines / total_lines


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

    ########### Alireza's Metrics ###########
    print(f'**********Alireza\'s Metrics**********')
    # Create a custom listener object
    listener = CustomListener()

    # Walk the parse tree with the custom listener
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)

    listener.flexbility_factcor()  # The flexibility factor
    listener.complexity_factor()  # The Complexity factor

    ########### Saba's Metrics ###########
    print(f'**********Saba\'s Metrics**********')
    # Create a custom listener object
    listener = EjioguMetricsListener()

    # Walk the parse tree with the custom listener
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)

    listener.calculate_metrics()

    ########### Mahdi's Metrics ###########
    print(f'\n**********Mahdi\'s Metrics**********')
    listener = ReadabilityMetricListener(parse_tree)
    # Walk the parse tree with the custom listener
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)
    listener.testability_factor()  # The Testability Factor
    listener.integrity_factor()  # The Integrity Factor

    ########### Ali's Metrics ###########
    print(f'\n**********Ali\'s Metrics**********')
    # Create a custom listener object
    listener = HenryMetricListener()

    # Walk the parse tree with the custom listener
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)

    print(f'calculate_comment_ratio : {calculate_comment_ratio("input1_Alireza.txt")}')
    print("---------------------------------------------------------------------")
    print("---------------------------------------------------------------------\n\n")

    ########### Ahmadreza's Metrics ###########
    print(f'\n**********Ahmadreza\'s Metrics**********')
    # Create a custom listener object
    listener = CustomAhmadrezaListener()

    # Walk the parse tree with the custom listener
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)

    listener.usability_factcor()
    listener.testability_factor()

    ########### Vahid's Metrics ###########
    print(f'\n**********Vahid\'s Metrics**********')
    # file_path = ".\JavaCode.txt"
    file_path = "Albrecht.java"
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
    # listener = EjioguMetricsListener()
    listener = Albrecht()
    # Walk the parse tree with the custom listener
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)

    listener.calculateFP()


# Call the main function
if __name__ == '__main__':
    main()
