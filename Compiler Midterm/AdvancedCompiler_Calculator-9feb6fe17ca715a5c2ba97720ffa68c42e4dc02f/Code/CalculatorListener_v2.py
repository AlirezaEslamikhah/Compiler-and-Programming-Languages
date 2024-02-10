
from antlr4 import *
from Gen.ArithmeticLexer import ArithmeticLexer
from Gen.ArithmeticListener import ArithmeticListener
from Gen.ArithmeticParser import ArithmeticParser

class CalculatorListener(ArithmeticListener):

    def __init__(self):
        self.result = 0

# Expression:
    def exitExpr(self, ctx:ArithmeticParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.exitTerm(ctx.getChild(0))
        else:
            result = self.exitTerm(ctx.getChild(0))
            len = ctx.getChildCount()-1
            for i in range(1,len,2):
                op = ctx.getChild(i).getText()
                if (op == '+'):
                    value = self.exitTerm(ctx.getChild(i+1))
                    result = result + value
                elif (op == '-'):
                    value = self.exitTerm(ctx.getChild(i+1))
                    result = result - value
            self.result = result
            return self.result

# Term:
    def exitTerm(self, ctx:ArithmeticParser.TermContext):
        if ctx.getChildCount() == 1:
            return self.exitFactor(ctx.getChild(0))
        else:
            result = self.exitFactor(ctx.getChild(0))
            len = ctx.getChildCount() - 1
            for i in range(1, len, 2):
                op = ctx.getChild(i).getText()
                if (op == '*'):
                    value = self.exitFactor(ctx.getChild(i + 1))
                    result = result * value
                elif (op == '/'):
                    value = self.exitFactor(ctx.getChild(i + 1))
                    result = result / value
            self.result = result
            return self.result

    def exitFactor(self, ctx:ArithmeticParser.FactorContext):
        if ctx.getChildCount() == 1:
            return float(ctx.NUMBER().getText())
        else:
            return self.exitExpr(ctx.getChild(1))
