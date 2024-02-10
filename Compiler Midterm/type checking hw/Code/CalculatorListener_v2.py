
from antlr4 import *
from Gen.JavaLexer import JavaLexer
from Gen.JavaParserListener import JavaParserListener
from Gen.JavaParser import JavaParser

class CalculatorListener(JavaParserListener):

    def __init__(self):
        self.result = 0

    # def exitIdentifier(self, ctx: JavaParser.IdentifierContext):
    #     variable_type = ctx.parentCtx.parentCtx.children[0].getText()
    #     variable_declarator_id = ctx.variableDeclaratorId()
    #     dims_text = variable_declarator_id.dims().getText()
    #
    #     print(f"line {ctx.start.line} and name : {ctx.getText()} and type : {variable_type} , {dims_text}")

    # def exitPrimitiveType(self, ctx: JavaParser.PrimitiveTypeContext):
    #     pass

    # def enterVariableDeclarator(self, ctx: JavaParser.VariableDeclaratorContext):
    #     variable_name = ctx.variableDeclaratorId().Identifier().getText()
    #     variable_type = ctx.parentCtx.parentCtx.children[0].getText()
    #     line_number = ctx.start.line
    #     variable_declarator_id = ctx.variableDeclaratorId()
    #     if variable_declarator_id.dims():
    #         dims_text = variable_declarator_id.dims().getText()
    #         print(f'line {line_number}:{variable_type}{dims_text} - name:{variable_name}')
    #     else:
    #         print(f'line {line_number}:{variable_type} - name:{variable_name}')

    # def enterVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
    #     variable_name = ctx.variableDeclaratorId().Identifier().getText()
    #     variable_type = ctx.parentCtx.parentCtx.children[0].getText()
    #     line_number = ctx.start.line
    #     print(f'line {line_number}:{variable_type},{variable_name}')


class VariableListener(ParseTreeListener):

    def enterVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
        variable_name = ctx.variableDeclaratorId().Identifier().getText()
        variable_type = ctx.parentCtx.parentCtx.children[0].getText()
        line_number = ctx.start.line
        print(f'line {line_number}:{variable_type},{variable_name}')
