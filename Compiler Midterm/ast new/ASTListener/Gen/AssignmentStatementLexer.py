# Generated from E:/MyWorks/Class Projects/Compiler/Compiler_1402/Resources/13. AST-builder\AssignmentStatement.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,30,246,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,13,1,13,
        1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,4,19,140,
        8,19,11,19,12,19,141,1,20,4,20,145,8,20,11,20,12,20,146,1,20,1,20,
        5,20,151,8,20,10,20,12,20,154,9,20,1,20,1,20,4,20,158,8,20,11,20,
        12,20,159,3,20,162,8,20,1,21,1,21,1,21,5,21,167,8,21,10,21,12,21,
        170,9,21,1,21,1,21,1,22,1,22,1,22,5,22,177,8,22,10,22,12,22,180,
        9,22,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,5,24,191,8,24,
        10,24,12,24,194,9,24,1,24,1,24,1,25,1,25,1,25,1,25,5,25,202,8,25,
        10,25,12,25,205,9,25,1,25,1,25,1,26,1,26,1,26,1,26,5,26,213,8,26,
        10,26,12,26,216,9,26,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,29,
        1,29,3,29,228,8,29,1,30,4,30,231,8,30,11,30,12,30,232,1,30,1,30,
        1,31,1,31,1,31,3,31,240,8,31,1,32,1,32,1,32,3,32,245,8,32,1,168,
        0,33,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,
        13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,
        24,49,25,51,26,53,27,55,0,57,0,59,0,61,28,63,29,65,30,1,0,3,1,0,
        48,57,2,0,65,90,97,122,3,0,9,9,13,13,32,32,258,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,
        0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,
        0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,
        0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,
        0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,
        0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,1,67,1,0,0,0,3,75,1,0,
        0,0,5,79,1,0,0,0,7,81,1,0,0,0,9,87,1,0,0,0,11,91,1,0,0,0,13,98,1,
        0,0,0,15,104,1,0,0,0,17,108,1,0,0,0,19,111,1,0,0,0,21,116,1,0,0,
        0,23,121,1,0,0,0,25,123,1,0,0,0,27,126,1,0,0,0,29,128,1,0,0,0,31,
        130,1,0,0,0,33,132,1,0,0,0,35,134,1,0,0,0,37,136,1,0,0,0,39,139,
        1,0,0,0,41,161,1,0,0,0,43,163,1,0,0,0,45,173,1,0,0,0,47,181,1,0,
        0,0,49,186,1,0,0,0,51,197,1,0,0,0,53,208,1,0,0,0,55,219,1,0,0,0,
        57,221,1,0,0,0,59,227,1,0,0,0,61,230,1,0,0,0,63,239,1,0,0,0,65,244,
        1,0,0,0,67,68,5,112,0,0,68,69,5,114,0,0,69,70,5,111,0,0,70,71,5,
        103,0,0,71,72,5,114,0,0,72,73,5,97,0,0,73,74,5,109,0,0,74,2,1,0,
        0,0,75,76,5,118,0,0,76,77,5,97,0,0,77,78,5,114,0,0,78,4,1,0,0,0,
        79,80,5,58,0,0,80,6,1,0,0,0,81,82,5,102,0,0,82,83,5,108,0,0,83,84,
        5,111,0,0,84,85,5,97,0,0,85,86,5,116,0,0,86,8,1,0,0,0,87,88,5,105,
        0,0,88,89,5,110,0,0,89,90,5,116,0,0,90,10,1,0,0,0,91,92,5,115,0,
        0,92,93,5,116,0,0,93,94,5,114,0,0,94,95,5,105,0,0,95,96,5,110,0,
        0,96,97,5,103,0,0,97,12,1,0,0,0,98,99,5,98,0,0,99,100,5,101,0,0,
        100,101,5,103,0,0,101,102,5,105,0,0,102,103,5,110,0,0,103,14,1,0,
        0,0,104,105,5,101,0,0,105,106,5,110,0,0,106,107,5,100,0,0,107,16,
        1,0,0,0,108,109,5,105,0,0,109,110,5,102,0,0,110,18,1,0,0,0,111,112,
        5,116,0,0,112,113,5,104,0,0,113,114,5,101,0,0,114,115,5,110,0,0,
        115,20,1,0,0,0,116,117,5,101,0,0,117,118,5,108,0,0,118,119,5,115,
        0,0,119,120,5,101,0,0,120,22,1,0,0,0,121,122,5,62,0,0,122,24,1,0,
        0,0,123,124,5,58,0,0,124,125,5,61,0,0,125,26,1,0,0,0,126,127,5,43,
        0,0,127,28,1,0,0,0,128,129,5,45,0,0,129,30,1,0,0,0,130,131,5,42,
        0,0,131,32,1,0,0,0,132,133,5,47,0,0,133,34,1,0,0,0,134,135,5,40,
        0,0,135,36,1,0,0,0,136,137,5,41,0,0,137,38,1,0,0,0,138,140,3,55,
        27,0,139,138,1,0,0,0,140,141,1,0,0,0,141,139,1,0,0,0,141,142,1,0,
        0,0,142,40,1,0,0,0,143,145,3,55,27,0,144,143,1,0,0,0,145,146,1,0,
        0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,152,5,46,
        0,0,149,151,3,55,27,0,150,149,1,0,0,0,151,154,1,0,0,0,152,150,1,
        0,0,0,152,153,1,0,0,0,153,162,1,0,0,0,154,152,1,0,0,0,155,157,5,
        46,0,0,156,158,3,55,27,0,157,156,1,0,0,0,158,159,1,0,0,0,159,157,
        1,0,0,0,159,160,1,0,0,0,160,162,1,0,0,0,161,144,1,0,0,0,161,155,
        1,0,0,0,162,42,1,0,0,0,163,168,5,34,0,0,164,167,3,59,29,0,165,167,
        9,0,0,0,166,164,1,0,0,0,166,165,1,0,0,0,167,170,1,0,0,0,168,169,
        1,0,0,0,168,166,1,0,0,0,169,171,1,0,0,0,170,168,1,0,0,0,171,172,
        5,34,0,0,172,44,1,0,0,0,173,178,3,57,28,0,174,177,3,57,28,0,175,
        177,3,55,27,0,176,174,1,0,0,0,176,175,1,0,0,0,177,180,1,0,0,0,178,
        176,1,0,0,0,178,179,1,0,0,0,179,46,1,0,0,0,180,178,1,0,0,0,181,182,
        3,45,22,0,182,183,5,91,0,0,183,184,3,39,19,0,184,185,5,93,0,0,185,
        48,1,0,0,0,186,187,5,91,0,0,187,192,3,39,19,0,188,189,5,44,0,0,189,
        191,3,39,19,0,190,188,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,
        193,1,0,0,0,193,195,1,0,0,0,194,192,1,0,0,0,195,196,5,93,0,0,196,
        50,1,0,0,0,197,198,5,91,0,0,198,203,3,41,20,0,199,200,5,44,0,0,200,
        202,3,41,20,0,201,199,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,
        204,1,0,0,0,204,206,1,0,0,0,205,203,1,0,0,0,206,207,5,93,0,0,207,
        52,1,0,0,0,208,209,5,91,0,0,209,214,3,43,21,0,210,211,5,44,0,0,211,
        213,3,43,21,0,212,210,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,
        215,1,0,0,0,215,217,1,0,0,0,216,214,1,0,0,0,217,218,5,93,0,0,218,
        54,1,0,0,0,219,220,7,0,0,0,220,56,1,0,0,0,221,222,7,1,0,0,222,58,
        1,0,0,0,223,224,5,92,0,0,224,228,5,34,0,0,225,226,5,92,0,0,226,228,
        5,92,0,0,227,223,1,0,0,0,227,225,1,0,0,0,228,60,1,0,0,0,229,231,
        7,2,0,0,230,229,1,0,0,0,231,232,1,0,0,0,232,230,1,0,0,0,232,233,
        1,0,0,0,233,234,1,0,0,0,234,235,6,30,0,0,235,62,1,0,0,0,236,240,
        5,10,0,0,237,238,5,13,0,0,238,240,5,10,0,0,239,236,1,0,0,0,239,237,
        1,0,0,0,240,64,1,0,0,0,241,242,5,60,0,0,242,245,5,61,0,0,243,245,
        5,60,0,0,244,241,1,0,0,0,244,243,1,0,0,0,245,66,1,0,0,0,17,0,141,
        146,152,159,161,166,168,176,178,192,203,214,227,232,239,244,1,6,
        0,0
    ]

class AssignmentStatementLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    INT = 20
    FLOAT = 21
    String = 22
    ID = 23
    ARRAY_TYPE = 24
    INT_ARRAY = 25
    FLOAT_ARRAY = 26
    STRING_ARRAY = 27
    WS = 28
    NEWLINE = 29
    RELOP = 30

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'program'", "'var'", "':'", "'float'", "'int'", "'string'", 
            "'begin'", "'end'", "'if'", "'then'", "'else'", "'>'", "':='", 
            "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "String", "ID", "ARRAY_TYPE", "INT_ARRAY", "FLOAT_ARRAY", 
            "STRING_ARRAY", "WS", "NEWLINE", "RELOP" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "INT", "FLOAT", 
                  "String", "ID", "ARRAY_TYPE", "INT_ARRAY", "FLOAT_ARRAY", 
                  "STRING_ARRAY", "DIGIT", "LETTER", "ESC", "WS", "NEWLINE", 
                  "RELOP" ]

    grammarFileName = "AssignmentStatement.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

