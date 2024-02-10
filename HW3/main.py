from antlr4 import *
from Gen.Q1Lexer import Q1Lexer
from Gen.Q1Parser import Q1Parser
import argparse
from Code.CustumListener import find_depth



def main(args):
    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')

    # Step 2: Create an instance of AssignmentStLexer
    lexer = Q1Lexer(stream)

            # "Q2"
            # lastname = "Eslamikhah"
            # studentid = "99521064"
            # token = lexer.nextToken()
            # refactoredStr = ''
            # while token.type != Token.EOF :
            #     if(token.type == lexer.COMMENT):
            #         refactoredStr += '#' + lastname + ' ' +token.text[1:] +' ' +studentid + '#'
            #         print(token.text+ '\n')
            #
            #     else :
            #         refactoredStr += token.text
            #     token = lexer.nextToken()
            #
            # print(refactoredStr+'\n')




    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)

    # Step 4: Create an instance of the AssignmentStParser
    parser = Q1Parser(token_stream)

    # Step 5: Create parse tree
    parse_tree = parser.start()
    listener = find_depth()
    walker = ParseTreeWalker()
    walker.walk(listener,parse_tree)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'input.txt')
    args = argparser.parse_args()
    main(args)


