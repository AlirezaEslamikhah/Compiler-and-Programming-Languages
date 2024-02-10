# Generated from E:/git/Compiler/Parsa/gram.g4 by ANTLR 4.13.1
from antlr4 import *


if "." in __name__:

    from .gramParser import gramParser
else:
    from gramParser import gramParser


# This class defines a complete listener for a parse tree produced by gramParser.
class gramListener(ParseTreeListener):
    def __init__(self):
        self.max=0
        self.stack=[]
    # Enter a parse tree produced by gramParser#start.
    def enterStart(self, ctx:gramParser.StartContext):
        pass

    # Exit a parse tree produced by gramParser#start.
    def exitStart(self, ctx:gramParser.StartContext):
        print(self.max)


    # Enter a parse tree produced by gramParser#ifst.
    def enterIfst(self, ctx:gramParser.IfstContext):
        self.stack.append("if")
        if(len(self.stack) > self.max):
            self.max = len(self.stack)

    # Exit a parse tree produced by gramParser#ifst.
    def exitIfst(self, ctx:gramParser.IfstContext):
        self.stack.pop()


    # Enter a parse tree produced by gramParser#whilest.
    def enterWhilest(self, ctx:gramParser.WhilestContext):
        self.stack.append("while")
        if(len(self.stack) > self.max):
            self.max = len(self.stack)

    # Exit a parse tree produced by gramParser#whilest.
    def exitWhilest(self, ctx:gramParser.WhilestContext):
        self.stack.pop()


    # Enter a parse tree produced by gramParser#statement.
    def enterStatement(self, ctx:gramParser.StatementContext):
        pass

    # Exit a parse tree produced by gramParser#statement.
    def exitStatement(self, ctx:gramParser.StatementContext):
        pass


    # Enter a parse tree produced by gramParser#compoundst.
    def enterCompoundst(self, ctx:gramParser.CompoundstContext):
        pass

    # Exit a parse tree produced by gramParser#compoundst.
    def exitCompoundst(self, ctx:gramParser.CompoundstContext):
        pass


    # Enter a parse tree produced by gramParser#define.
    def enterDefine(self, ctx:gramParser.DefineContext):
        pass

    # Exit a parse tree produced by gramParser#define.
    def exitDefine(self, ctx:gramParser.DefineContext):
        pass


    # Enter a parse tree produced by gramParser#assignment.
    def enterAssignment(self, ctx:gramParser.AssignmentContext):
        pass

    # Exit a parse tree produced by gramParser#assignment.
    def exitAssignment(self, ctx:gramParser.AssignmentContext):
        pass


    # Enter a parse tree produced by gramParser#cond.
    def enterCond(self, ctx:gramParser.CondContext):
        pass

    # Exit a parse tree produced by gramParser#cond.
    def exitCond(self, ctx:gramParser.CondContext):
        pass



del gramParser
