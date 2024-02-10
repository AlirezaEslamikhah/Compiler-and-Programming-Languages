from antlr4 import *
from Gen.TypeCheckerListener import TypeCheckerListener

# from TypeCheckerParser import TypeCheckerParser


class MyTypeCheckerListener(TypeCheckerListener):

    def __init__(self):
        self.result = 0

    def get_type(self):
        return self.result

    def exitExpr1(self, ctx):
        left_type = ctx.e2.type
        right_type = ctx.t1.type
        if left_type != right_type:
            print("Type error: Incompatible types in addition operation")
        ctx.type = left_type

        self.result = ctx.type

    def exitExpr2(self, ctx):
        left_type = ctx.expr().type
        right_type = ctx.term().type
        if left_type != right_type:
            print("Type error: Incompatible types in subtraction operation")
        ctx.type = left_type

        self.result = ctx.type

    def exitExpr3(self, ctx):
        ctx.type = ctx.term().type

        self.result = ctx.type

    def exitTerm1(self, ctx):
        left_type = ctx.term().type
        right_type = ctx.fact().type
        if left_type != right_type:
            print("Type error: Incompatible types in multiplication operation")
        ctx.type = left_type

    def exitTerm2(self, ctx):
        left_type = ctx.term().type
        right_type = ctx.fact().type
        if left_type != right_type:
            print("Type error: Incompatible types in division operation")
        ctx.type = left_type

    def exitTerm3(self, ctx):
        ctx.type = ctx.fact().type

    def exitFactString(self, ctx):
        ctx.type = "string"

    def exitFactInteger(self, ctx):
        ctx.type = "integer"

    def exitFactFloat(self, ctx):
        ctx.type = "float"

    def exitFactExpr(self, ctx):
        ctx.type = ctx.expr().type
