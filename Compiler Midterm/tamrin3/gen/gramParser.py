# Generated from E:/git/Compiler/Parsa/gram.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,5,0,19,8,0,10,0,12,0,22,9,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,4,1,32,8,1,11,1,12,1,33,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,1,2,5,2,44,8,2,10,2,12,2,47,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,
        3,56,8,3,1,4,1,4,5,4,60,8,4,10,4,12,4,63,9,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,6,3,6,72,8,6,1,6,1,6,1,6,1,6,1,6,3,6,79,8,6,1,6,1,6,1,6,1,
        6,3,6,85,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,3,7,103,8,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,1,1,0,8,9,
        113,0,20,1,0,0,0,2,25,1,0,0,0,4,37,1,0,0,0,6,55,1,0,0,0,8,57,1,0,
        0,0,10,66,1,0,0,0,12,84,1,0,0,0,14,102,1,0,0,0,16,19,3,6,3,0,17,
        19,3,8,4,0,18,16,1,0,0,0,18,17,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,
        0,20,21,1,0,0,0,21,23,1,0,0,0,22,20,1,0,0,0,23,24,5,0,0,1,24,1,1,
        0,0,0,25,26,5,6,0,0,26,27,5,1,0,0,27,28,3,14,7,0,28,29,5,2,0,0,29,
        31,5,3,0,0,30,32,3,6,3,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,
        0,33,34,1,0,0,0,34,35,1,0,0,0,35,36,5,4,0,0,36,3,1,0,0,0,37,38,5,
        7,0,0,38,39,5,1,0,0,39,40,3,14,7,0,40,41,5,2,0,0,41,45,5,3,0,0,42,
        44,3,6,3,0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,
        0,46,48,1,0,0,0,47,45,1,0,0,0,48,49,5,4,0,0,49,5,1,0,0,0,50,56,3,
        2,1,0,51,56,3,12,6,0,52,56,3,4,2,0,53,56,3,8,4,0,54,56,3,10,5,0,
        55,50,1,0,0,0,55,51,1,0,0,0,55,52,1,0,0,0,55,53,1,0,0,0,55,54,1,
        0,0,0,56,7,1,0,0,0,57,61,5,3,0,0,58,60,3,6,3,0,59,58,1,0,0,0,60,
        63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,
        0,64,65,5,4,0,0,65,9,1,0,0,0,66,67,7,0,0,0,67,68,5,10,0,0,68,69,
        5,13,0,0,69,11,1,0,0,0,70,72,5,8,0,0,71,70,1,0,0,0,71,72,1,0,0,0,
        72,73,1,0,0,0,73,74,5,10,0,0,74,75,5,5,0,0,75,76,5,11,0,0,76,85,
        5,13,0,0,77,79,5,9,0,0,78,77,1,0,0,0,78,79,1,0,0,0,79,80,1,0,0,0,
        80,81,5,10,0,0,81,82,5,5,0,0,82,83,5,12,0,0,83,85,5,13,0,0,84,71,
        1,0,0,0,84,78,1,0,0,0,85,13,1,0,0,0,86,103,5,12,0,0,87,88,5,10,0,
        0,88,89,5,15,0,0,89,103,5,10,0,0,90,91,5,10,0,0,91,92,5,15,0,0,92,
        103,5,11,0,0,93,94,5,11,0,0,94,95,5,15,0,0,95,103,5,10,0,0,96,97,
        5,11,0,0,97,98,5,15,0,0,98,103,5,11,0,0,99,100,5,10,0,0,100,101,
        5,16,0,0,101,103,5,12,0,0,102,86,1,0,0,0,102,87,1,0,0,0,102,90,1,
        0,0,0,102,93,1,0,0,0,102,96,1,0,0,0,102,99,1,0,0,0,103,15,1,0,0,
        0,10,18,20,33,45,55,61,71,78,84,102
    ]

class gramParser ( Parser ):

    grammarFileName = "gram.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'='", "'if'", 
                     "'while'", "'int'", "'boolean'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "';'", "<INVALID>", "<INVALID>", "'=='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IF", "WHILE", "INT", "BOOL", 
                      "ID", "INTTYPE", "BOOLTYPE", "SC", "WS", "RELOP", 
                      "EQ", "COMMENT" ]

    RULE_start = 0
    RULE_ifst = 1
    RULE_whilest = 2
    RULE_statement = 3
    RULE_compoundst = 4
    RULE_define = 5
    RULE_assignment = 6
    RULE_cond = 7

    ruleNames =  [ "start", "ifst", "whilest", "statement", "compoundst", 
                   "define", "assignment", "cond" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    IF=6
    WHILE=7
    INT=8
    BOOL=9
    ID=10
    INTTYPE=11
    BOOLTYPE=12
    SC=13
    WS=14
    RELOP=15
    EQ=16
    COMMENT=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gramParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramParser.StatementContext,i)


        def compoundst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramParser.CompoundstContext)
            else:
                return self.getTypedRuleContext(gramParser.CompoundstContext,i)


        def getRuleIndex(self):
            return gramParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = gramParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1992) != 0):
                self.state = 18
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 16
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 17
                    self.compoundst()
                    pass


                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 23
            self.match(gramParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def IF(self):
            return self.getToken(gramParser.IF, 0)

        def cond(self):
            return self.getTypedRuleContext(gramParser.CondContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramParser.StatementContext,i)


        def getRuleIndex(self):
            return gramParser.RULE_ifst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfst" ):
                listener.enterIfst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfst" ):
                listener.exitIfst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfst" ):
                return visitor.visitIfst(self)
            else:
                return visitor.visitChildren(self)




    def ifst(self):

        localctx = gramParser.IfstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ifst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(gramParser.IF)
            self.state = 26
            self.match(gramParser.T__0)
            self.state = 27
            self.cond()
            self.state = 28
            self.match(gramParser.T__1)
            self.state = 29
            self.match(gramParser.T__2)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.statement()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1992) != 0)):
                    break

            self.state = 35
            self.match(gramParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def WHILE(self):
            return self.getToken(gramParser.WHILE, 0)

        def cond(self):
            return self.getTypedRuleContext(gramParser.CondContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramParser.StatementContext,i)


        def getRuleIndex(self):
            return gramParser.RULE_whilest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhilest" ):
                listener.enterWhilest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhilest" ):
                listener.exitWhilest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilest" ):
                return visitor.visitWhilest(self)
            else:
                return visitor.visitChildren(self)




    def whilest(self):

        localctx = gramParser.WhilestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_whilest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(gramParser.WHILE)
            self.state = 38
            self.match(gramParser.T__0)
            self.state = 39
            self.cond()
            self.state = 40
            self.match(gramParser.T__1)
            self.state = 41
            self.match(gramParser.T__2)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1992) != 0):
                self.state = 42
                self.statement()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(gramParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def ifst(self):
            return self.getTypedRuleContext(gramParser.IfstContext,0)


        def assignment(self):
            return self.getTypedRuleContext(gramParser.AssignmentContext,0)


        def whilest(self):
            return self.getTypedRuleContext(gramParser.WhilestContext,0)


        def compoundst(self):
            return self.getTypedRuleContext(gramParser.CompoundstContext,0)


        def define(self):
            return self.getTypedRuleContext(gramParser.DefineContext,0)


        def getRuleIndex(self):
            return gramParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = gramParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.ifst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.whilest()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.compoundst()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.define()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramParser.StatementContext,i)


        def getRuleIndex(self):
            return gramParser.RULE_compoundst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundst" ):
                listener.enterCompoundst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundst" ):
                listener.exitCompoundst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundst" ):
                return visitor.visitCompoundst(self)
            else:
                return visitor.visitChildren(self)




    def compoundst(self):

        localctx = gramParser.CompoundstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_compoundst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(gramParser.T__2)

            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1992) != 0):
                self.state = 58
                self.statement()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(gramParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def ID(self):
            return self.getToken(gramParser.ID, 0)

        def SC(self):
            return self.getToken(gramParser.SC, 0)

        def INT(self):
            return self.getToken(gramParser.INT, 0)

        def BOOL(self):
            return self.getToken(gramParser.BOOL, 0)

        def getRuleIndex(self):
            return gramParser.RULE_define

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine" ):
                listener.enterDefine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine" ):
                listener.exitDefine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine" ):
                return visitor.visitDefine(self)
            else:
                return visitor.visitChildren(self)




    def define(self):

        localctx = gramParser.DefineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_define)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 67
            self.match(gramParser.ID)
            self.state = 68
            self.match(gramParser.SC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def ID(self):
            return self.getToken(gramParser.ID, 0)

        def INTTYPE(self):
            return self.getToken(gramParser.INTTYPE, 0)

        def SC(self):
            return self.getToken(gramParser.SC, 0)

        def INT(self):
            return self.getToken(gramParser.INT, 0)

        def BOOLTYPE(self):
            return self.getToken(gramParser.BOOLTYPE, 0)

        def BOOL(self):
            return self.getToken(gramParser.BOOL, 0)

        def getRuleIndex(self):
            return gramParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = gramParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 70
                    self.match(gramParser.INT)


                self.state = 73
                self.match(gramParser.ID)
                self.state = 74
                self.match(gramParser.T__4)
                self.state = 75
                self.match(gramParser.INTTYPE)
                self.state = 76
                self.match(gramParser.SC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 77
                    self.match(gramParser.BOOL)


                self.state = 80
                self.match(gramParser.ID)
                self.state = 81
                self.match(gramParser.T__4)
                self.state = 82
                self.match(gramParser.BOOLTYPE)
                self.state = 83
                self.match(gramParser.SC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def BOOLTYPE(self):
            return self.getToken(gramParser.BOOLTYPE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def RELOP(self):
            return self.getToken(gramParser.RELOP, 0)

        def INTTYPE(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.INTTYPE)
            else:
                return self.getToken(gramParser.INTTYPE, i)

        def EQ(self):
            return self.getToken(gramParser.EQ, 0)

        def getRuleIndex(self):
            return gramParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = gramParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cond)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(gramParser.BOOLTYPE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(gramParser.ID)
                self.state = 88
                self.match(gramParser.RELOP)
                self.state = 89
                self.match(gramParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.match(gramParser.ID)
                self.state = 91
                self.match(gramParser.RELOP)
                self.state = 92
                self.match(gramParser.INTTYPE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 93
                self.match(gramParser.INTTYPE)
                self.state = 94
                self.match(gramParser.RELOP)
                self.state = 95
                self.match(gramParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 96
                self.match(gramParser.INTTYPE)
                self.state = 97
                self.match(gramParser.RELOP)
                self.state = 98
                self.match(gramParser.INTTYPE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 99
                self.match(gramParser.ID)
                self.state = 100
                self.match(gramParser.EQ)
                self.state = 101
                self.match(gramParser.BOOLTYPE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





