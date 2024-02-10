# Generated from C:/Users/lenovo/Desktop/Term7/Compiler/HW3/Q1.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Q1Parser import Q1Parser
else:
    from Q1Parser import Q1Parser

# This class defines a complete generic visitor for a parse tree produced by Q1Parser.

class Q1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Q1Parser#start.
    def visitStart(self, ctx:Q1Parser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q1Parser#ifst.
    def visitIfst(self, ctx:Q1Parser.IfstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q1Parser#whilest.
    def visitWhilest(self, ctx:Q1Parser.WhilestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q1Parser#statement.
    def visitStatement(self, ctx:Q1Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q1Parser#compoundst.
    def visitCompoundst(self, ctx:Q1Parser.CompoundstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q1Parser#assignment.
    def visitAssignment(self, ctx:Q1Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Q1Parser#condition.
    def visitCondition(self, ctx:Q1Parser.ConditionContext):
        return self.visitChildren(ctx)



del Q1Parser