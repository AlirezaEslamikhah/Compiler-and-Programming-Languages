# Generated from E:/git/Compiler/Parsa/gram.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramParser import gramParser
else:
    from gramParser import gramParser

# This class defines a complete generic visitor for a parse tree produced by gramParser.

class gramVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramParser#start.
    def visitStart(self, ctx:gramParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramParser#ifst.
    def visitIfst(self, ctx:gramParser.IfstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramParser#whilest.
    def visitWhilest(self, ctx:gramParser.WhilestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramParser#statement.
    def visitStatement(self, ctx:gramParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramParser#compoundst.
    def visitCompoundst(self, ctx:gramParser.CompoundstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramParser#define.
    def visitDefine(self, ctx:gramParser.DefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramParser#assignment.
    def visitAssignment(self, ctx:gramParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramParser#cond.
    def visitCond(self, ctx:gramParser.CondContext):
        return self.visitChildren(ctx)



del gramParser