# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write(".\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\2\7\2\23\n\2\f\2\16\2\26\13\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\5\3\36\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\2\2\b\3\3\5\2\7\2\t\2\13")
        buf.write("\4\r\5\3\2\6\4\2$$^^\n\2$$\61\61^^ddhhppttvv\5\2\62;C")
        buf.write("Hch\5\2\13\f\17\17\"\"\2-\2\3\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\3\17\3\2\2\2\5\32\3\2\2\2\7\37\3\2\2\2\t%\3\2")
        buf.write("\2\2\13\'\3\2\2\2\r+\3\2\2\2\17\24\7$\2\2\20\23\5\5\3")
        buf.write("\2\21\23\n\2\2\2\22\20\3\2\2\2\22\21\3\2\2\2\23\26\3\2")
        buf.write("\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25\27\3\2\2\2\26\24\3")
        buf.write("\2\2\2\27\30\7$\2\2\30\31\b\2\2\2\31\4\3\2\2\2\32\35\7")
        buf.write("^\2\2\33\36\t\3\2\2\34\36\5\7\4\2\35\33\3\2\2\2\35\34")
        buf.write("\3\2\2\2\36\6\3\2\2\2\37 \7w\2\2 !\5\t\5\2!\"\5\t\5\2")
        buf.write("\"#\5\t\5\2#$\5\t\5\2$\b\3\2\2\2%&\t\4\2\2&\n\3\2\2\2")
        buf.write("\'(\t\5\2\2()\3\2\2\2)*\b\6\3\2*\f\3\2\2\2+,\13\2\2\2")
        buf.write(",-\b\7\4\2-\16\3\2\2\2\6\2\22\24\35\5\3\2\2\b\2\2\3\7")
        buf.write("\3")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRING = 1
    WS = 2
    ERROR_CHAR = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "STRING", "WS", "ERROR_CHAR" ]

    ruleNames = [ "STRING", "ESC", "UNICODE", "HEX", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.STRING_action 
            actions[5] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     


