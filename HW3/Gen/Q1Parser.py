# Generated from C:/Users/lenovo/Desktop/Term7/Compiler/HW3/Q1.g4 by ANTLR 4.13.1
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
        4,1,17,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,4,1,30,8,1,11,1,12,1,31,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,5,
        2,42,8,2,10,2,12,2,45,9,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,53,8,3,1,4,
        1,4,5,4,57,8,4,10,4,12,4,60,9,4,1,4,1,4,1,5,3,5,65,8,5,1,5,1,5,1,
        5,1,5,1,5,3,5,72,8,5,1,5,1,5,1,5,1,5,3,5,78,8,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,3,6,90,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,0,
        98,0,18,1,0,0,0,2,23,1,0,0,0,4,35,1,0,0,0,6,52,1,0,0,0,8,54,1,0,
        0,0,10,77,1,0,0,0,12,89,1,0,0,0,14,17,3,6,3,0,15,17,3,8,4,0,16,14,
        1,0,0,0,16,15,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,
        19,21,1,0,0,0,20,18,1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,24,5,7,
        0,0,24,25,5,1,0,0,25,26,3,12,6,0,26,27,5,2,0,0,27,29,5,3,0,0,28,
        30,3,6,3,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,
        0,32,33,1,0,0,0,33,34,5,4,0,0,34,3,1,0,0,0,35,36,5,8,0,0,36,37,5,
        1,0,0,37,38,3,12,6,0,38,39,5,2,0,0,39,43,5,3,0,0,40,42,3,6,3,0,41,
        40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,
        0,45,43,1,0,0,0,46,47,5,4,0,0,47,5,1,0,0,0,48,53,3,2,1,0,49,53,3,
        10,5,0,50,53,3,4,2,0,51,53,3,8,4,0,52,48,1,0,0,0,52,49,1,0,0,0,52,
        50,1,0,0,0,52,51,1,0,0,0,53,7,1,0,0,0,54,58,5,3,0,0,55,57,3,6,3,
        0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,
        1,0,0,0,60,58,1,0,0,0,61,62,5,4,0,0,62,9,1,0,0,0,63,65,5,9,0,0,64,
        63,1,0,0,0,64,65,1,0,0,0,65,66,1,0,0,0,66,67,5,11,0,0,67,68,5,5,
        0,0,68,69,5,12,0,0,69,78,5,6,0,0,70,72,5,10,0,0,71,70,1,0,0,0,71,
        72,1,0,0,0,72,73,1,0,0,0,73,74,5,11,0,0,74,75,5,5,0,0,75,76,5,13,
        0,0,76,78,5,6,0,0,77,64,1,0,0,0,77,71,1,0,0,0,78,11,1,0,0,0,79,90,
        5,13,0,0,80,81,5,11,0,0,81,82,5,15,0,0,82,90,5,11,0,0,83,84,5,11,
        0,0,84,85,5,15,0,0,85,90,5,12,0,0,86,87,5,11,0,0,87,88,5,16,0,0,
        88,90,5,13,0,0,89,79,1,0,0,0,89,80,1,0,0,0,89,83,1,0,0,0,89,86,1,
        0,0,0,90,13,1,0,0,0,10,16,18,31,43,52,58,64,71,77,89
    ]

class Q1Parser ( Parser ):

    grammarFileName = "Q1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'='", "';'", 
                     "'if'", "'while'", "'int'", "'boolean'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'=='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IF", "WHILE", 
                      "INT", "BOOL", "ID", "INTTYPE", "BOOLTYPE", "WS", 
                      "RELOP", "EQ", "COMMENT" ]

    RULE_start = 0
    RULE_ifst = 1
    RULE_whilest = 2
    RULE_statement = 3
    RULE_compoundst = 4
    RULE_assignment = 5
    RULE_condition = 6

    ruleNames =  [ "start", "ifst", "whilest", "statement", "compoundst", 
                   "assignment", "condition" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    IF=7
    WHILE=8
    INT=9
    BOOL=10
    ID=11
    INTTYPE=12
    BOOLTYPE=13
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
            return self.getToken(Q1Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Q1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Q1Parser.StatementContext,i)


        def compoundst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Q1Parser.CompoundstContext)
            else:
                return self.getTypedRuleContext(Q1Parser.CompoundstContext,i)


        def getRuleIndex(self):
            return Q1Parser.RULE_start

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

        localctx = Q1Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3976) != 0):
                self.state = 16
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 14
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 15
                    self.compoundst()
                    pass


                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
            self.match(Q1Parser.EOF)
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
            return self.getToken(Q1Parser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(Q1Parser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Q1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Q1Parser.StatementContext,i)


        def getRuleIndex(self):
            return Q1Parser.RULE_ifst

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

        localctx = Q1Parser.IfstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ifst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(Q1Parser.IF)
            self.state = 24
            self.match(Q1Parser.T__0)
            self.state = 25
            self.condition()
            self.state = 26
            self.match(Q1Parser.T__1)
            self.state = 27
            self.match(Q1Parser.T__2)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.statement()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3976) != 0)):
                    break

            self.state = 33
            self.match(Q1Parser.T__3)
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
            return self.getToken(Q1Parser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(Q1Parser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Q1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Q1Parser.StatementContext,i)


        def getRuleIndex(self):
            return Q1Parser.RULE_whilest

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

        localctx = Q1Parser.WhilestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_whilest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(Q1Parser.WHILE)
            self.state = 36
            self.match(Q1Parser.T__0)
            self.state = 37
            self.condition()
            self.state = 38
            self.match(Q1Parser.T__1)
            self.state = 39
            self.match(Q1Parser.T__2)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3976) != 0):
                self.state = 40
                self.statement()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(Q1Parser.T__3)
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
            return self.getTypedRuleContext(Q1Parser.IfstContext,0)


        def assignment(self):
            return self.getTypedRuleContext(Q1Parser.AssignmentContext,0)


        def whilest(self):
            return self.getTypedRuleContext(Q1Parser.WhilestContext,0)


        def compoundst(self):
            return self.getTypedRuleContext(Q1Parser.CompoundstContext,0)


        def getRuleIndex(self):
            return Q1Parser.RULE_statement

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

        localctx = Q1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.ifst()
                pass
            elif token in [9, 10, 11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.assignment()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.whilest()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.compoundst()
                pass
            else:
                raise NoViableAltException(self)

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
                return self.getTypedRuleContexts(Q1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Q1Parser.StatementContext,i)


        def getRuleIndex(self):
            return Q1Parser.RULE_compoundst

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

        localctx = Q1Parser.CompoundstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_compoundst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(Q1Parser.T__2)

            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3976) != 0):
                self.state = 55
                self.statement()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(Q1Parser.T__3)
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
            return self.getToken(Q1Parser.ID, 0)

        def INTTYPE(self):
            return self.getToken(Q1Parser.INTTYPE, 0)

        def INT(self):
            return self.getToken(Q1Parser.INT, 0)

        def BOOLTYPE(self):
            return self.getToken(Q1Parser.BOOLTYPE, 0)

        def BOOL(self):
            return self.getToken(Q1Parser.BOOL, 0)

        def getRuleIndex(self):
            return Q1Parser.RULE_assignment

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

        localctx = Q1Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 63
                    self.match(Q1Parser.INT)


                self.state = 66
                self.match(Q1Parser.ID)
                self.state = 67
                self.match(Q1Parser.T__4)
                self.state = 68
                self.match(Q1Parser.INTTYPE)
                self.state = 69
                self.match(Q1Parser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 70
                    self.match(Q1Parser.BOOL)


                self.state = 73
                self.match(Q1Parser.ID)
                self.state = 74
                self.match(Q1Parser.T__4)
                self.state = 75
                self.match(Q1Parser.BOOLTYPE)
                self.state = 76
                self.match(Q1Parser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()

        def BOOLTYPE(self):
            return self.getToken(Q1Parser.BOOLTYPE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Q1Parser.ID)
            else:
                return self.getToken(Q1Parser.ID, i)

        def RELOP(self):
            return self.getToken(Q1Parser.RELOP, 0)

        def INTTYPE(self):
            return self.getToken(Q1Parser.INTTYPE, 0)

        def EQ(self):
            return self.getToken(Q1Parser.EQ, 0)

        def getRuleIndex(self):
            return Q1Parser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = Q1Parser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(Q1Parser.BOOLTYPE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(Q1Parser.ID)
                self.state = 81
                self.match(Q1Parser.RELOP)
                self.state = 82
                self.match(Q1Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.match(Q1Parser.ID)
                self.state = 84
                self.match(Q1Parser.RELOP)
                self.state = 85
                self.match(Q1Parser.INTTYPE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.match(Q1Parser.ID)
                self.state = 87
                self.match(Q1Parser.EQ)
                self.state = 88
                self.match(Q1Parser.BOOLTYPE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





