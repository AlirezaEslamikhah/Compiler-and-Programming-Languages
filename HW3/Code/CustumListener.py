from antlr4 import *
from Gen.Q1Lexer import Q1Lexer
from Gen.Q1Listener import Q1Listener
from Gen.Q1Parser import Q1Parser

class find_depth (Q1Listener):
    def __init__(self):
        self.depth = 0
        self.max_depth = 0


    def enterIfst(self, ctx:Q1Parser.IfstContext):
        print("entered")
        self.depth = self.depth + 1
        if self.depth > self.max_depth:
            self.max_depth = self.depth

    def exitIfst(self, ctx: Q1Parser.IfstContext):
        self.depth = self.depth - 1

    def enterWhilest(self, ctx:Q1Parser.WhilestContext):
        self.depth = self.depth + 1
        if self.depth > self.max_depth:
            self.max_depth = self.depth

    def exitWhilest(self, ctx:Q1Parser.WhilestContext):
        self.depth = self.depth - 1

    def exitStart(self, ctx:Q1Parser.StartContext):
        print(self.max_depth)


