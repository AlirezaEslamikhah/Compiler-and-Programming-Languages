from antlr4 import *
from Gen.TypeCheckerListener import TypeCheckerListener

class MyTypeCheckerListener(TypeCheckerListener):

    def __init__(self):
        self.type = ""

    def get_type(self):
        return self.type

    def exitExpr1(self, ctx): # e2=expr '+' t1=term  #expr1
        left_type = ctx.getChild(0).type
        right_type = ctx.getChild(2).type

        if left_type == "Integer" and right_type == "Integer":
            ctx.type = "Integer"
        elif left_type == "Float" and right_type == "Float":
            ctx.type = "Float"
        elif left_type == "Integer" and right_type == "Float":
            ctx.type = "Float"
        elif left_type == "Float" and right_type == "Integer":
            ctx.type = "Float"
        elif left_type == "String" and right_type == "Integer":
            ctx.type = "String"
        elif left_type == "String" and right_type == "Float":
            ctx.type = "String"
        elif left_type == "String" and right_type == "String":
            ctx.type = "String"
        elif left_type == "Integer" and right_type == "String":
            raise Exception("error")
        elif left_type == "Float" and right_type == "String":
            raise Exception("error")
        else:
            raise Exception("None of them")

        self.type = ctx.type

    def exitExpr2(self, ctx): # expr '-' term  #expr2
        left_type = ctx.getChild(0).type
        right_type = ctx.getChild(2).type

        if left_type == "Integer" and right_type == "Integer":
            ctx.type = "Integer"
        elif left_type == "Float" and right_type == "Float":
            ctx.type = "Float"
        elif left_type == "Integer" and right_type == "Float":
            ctx.type = "Float"
        elif left_type == "Float" and right_type == "Integer":
            ctx.type = "Float"
        elif left_type == "String" or right_type == "String":
            raise Exception("error")

        self.type = ctx.type

    def exitExpr3(self, ctx): # term #expr3
        ctx.type = ctx.getChild(0).type

        self.type = ctx.type

    def exitTerm1(self, ctx): # term '*' fact  #term1
        left_type = ctx.getChild(0).type
        right_type = ctx.getChild(2).type

        if left_type == "Integer" and right_type == "Integer":
            ctx.type = "Integer"
        elif left_type == "Float" and right_type == "Float":
            ctx.type = "Float"
        elif left_type == "Integer" and right_type == "Float":
            ctx.type = "Float"
        elif left_type == "Float" and right_type == "Integer":
            ctx.type = "Float"
        elif left_type == "String" or right_type == "String":
            raise Exception("Type error: String cannot be multiplied")
        else:
            raise Exception("None of them")

    def exitTerm2(self, ctx): # term '/' fact #term2
        left_type = ctx.getChild(0).type
        right_type = ctx.getChild(2).type

        if left_type == "Integer" and right_type == "Integer":
            ctx.type = "Float"
        elif left_type == "Float" and right_type == "Float":
            ctx.type = "Float"
        elif left_type == "Integer" and right_type == "Float":
            ctx.type = "Float"
        elif left_type == "Float" and right_type == "Integer":
            ctx.type = "Float"
        elif left_type == "String" or right_type == "String":
            raise Exception("Type error: String cannot be divided")
        else:
            raise Exception("None of them")

    def exitTerm3(self, ctx): # fact #term3
        # ctx.type = ctx.fact().type
        ctx.type = ctx.getChild(0).type

    def exitFactString(self, ctx):
        ctx.type = "String"

    def exitFactInteger(self, ctx):
        ctx.type = "Integer"

    def exitFactFloat(self, ctx):
        ctx.type = "Float"

    def exitFactExpr(self, ctx):
        # ctx.type = ctx.expr().type
        ctx.type = ctx.getChild(1).type
