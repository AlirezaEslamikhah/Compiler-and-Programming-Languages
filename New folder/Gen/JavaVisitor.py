# Generated from D:/UniClasses/7th Semester/Compiler Design/HWs/HW4/Java.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .JavaParser import JavaParser
else:
    from JavaParser import JavaParser

# This class defines a complete generic visitor for a parse tree produced by JavaParser.

class JavaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JavaParser#start.
    def visitStart(self, ctx:JavaParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:JavaParser.FieldDeclarationContext):
        return self.visitChildren(ctx)



del JavaParser