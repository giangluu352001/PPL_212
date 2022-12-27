# Generated from c:\Users\Test\Downloads\PPL_212\assignment3\src\main\d96\parser\D96.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0206\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\6\2")
        buf.write("\\\n\2\r\2\16\2]\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3k\n\3\3\4\3\4\3\4\6\4p\n\4\r\4\16\4q\5\4t\n")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u0082\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\7\6\u008f\n\6\f\6\16\6\u0092\13\6\3\6\3\6\5\6\u0096\n")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a1\n\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\5\n\u00ae\n")
        buf.write("\n\3\n\3\n\3\13\3\13\7\13\u00b4\n\13\f\13\16\13\u00b7")
        buf.write("\13\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00c1")
        buf.write("\n\13\3\13\3\13\3\f\3\f\3\f\5\f\u00c8\n\f\3\r\3\r\7\r")
        buf.write("\u00cc\n\r\f\r\16\r\u00cf\13\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00d8\n\16\3\17\3\17\3\17\3\17\3\17\5")
        buf.write("\17\u00df\n\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00e7")
        buf.write("\n\20\f\20\16\20\u00ea\13\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\7\21\u00f2\n\21\f\21\16\21\u00f5\13\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\7\22\u00fd\n\22\f\22\16\22\u0100")
        buf.write("\13\22\3\23\3\23\3\23\5\23\u0105\n\23\3\24\3\24\3\24\5")
        buf.write("\24\u010a\n\24\3\25\3\25\3\25\3\25\3\25\6\25\u0111\n\25")
        buf.write("\r\25\16\25\u0112\7\25\u0115\n\25\f\25\16\25\u0118\13")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0121\n\26")
        buf.write("\7\26\u0123\n\26\f\26\16\26\u0126\13\26\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u012c\n\27\3\27\5\27\u012f\n\27\3\30\3\30\3")
        buf.write("\30\3\30\5\30\u0135\n\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u013f\n\31\3\32\3\32\5\32\u0143\n\32\3")
        buf.write("\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u014f\n\34\3\34\3\34\7\34\u0153\n\34\f\34\16\34\u0156")
        buf.write("\13\34\3\34\3\34\3\35\3\35\3\35\3\35\5\35\u015e\n\35\3")
        buf.write("\36\3\36\3\36\5\36\u0163\n\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \5 \u0170\n \3 \3 \3 \3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\7!\u017d\n!\f!\16!\u0180\13!\3\"\3\"")
        buf.write("\3\"\7\"\u0185\n\"\f\"\16\"\u0188\13\"\3#\3#\3#\3#\3#")
        buf.write("\7#\u018f\n#\f#\16#\u0192\13#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\7#\u019d\n#\f#\16#\u01a0\13#\5#\u01a2\n#\3#\3#\3#")
        buf.write("\3#\5#\u01a8\n#\3$\3$\3%\3%\3%\3%\3%\7%\u01b1\n%\f%\16")
        buf.write("%\u01b4\13%\3%\3%\3%\3%\3%\3%\3%\3%\3%\7%\u01bf\n%\f%")
        buf.write("\16%\u01c2\13%\5%\u01c4\n%\3%\3%\3%\3%\5%\u01ca\n%\3&")
        buf.write("\3&\3&\7&\u01cf\n&\f&\16&\u01d2\13&\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u01da\n\'\3(\3(\3(\3(\3(\3(\3(\5(\u01e3\n(")
        buf.write("\3(\3(\3(\3(\3(\3)\3)\3)\5)\u01ed\n)\3)\3)\3*\3*\3*\3")
        buf.write("+\3+\3+\7+\u01f7\n+\f+\16+\u01fa\13+\3,\3,\3,\3,\3,\3")
        buf.write(",\5,\u0202\n,\3-\3-\3-\2\7\36 \"(*.\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVX\2\n\3\2./\3\2\',\3\2%&\3\2\37 \3\2!#\3\2<=\3\2")
        buf.write("\25\26\4\2\f\f\17\17\2\u0223\2[\3\2\2\2\4j\3\2\2\2\6s")
        buf.write("\3\2\2\2\b\u0081\3\2\2\2\n\u0083\3\2\2\2\f\u0097\3\2\2")
        buf.write("\2\16\u00a5\3\2\2\2\20\u00a8\3\2\2\2\22\u00ab\3\2\2\2")
        buf.write("\24\u00c0\3\2\2\2\26\u00c4\3\2\2\2\30\u00c9\3\2\2\2\32")
        buf.write("\u00d7\3\2\2\2\34\u00de\3\2\2\2\36\u00e0\3\2\2\2 \u00eb")
        buf.write("\3\2\2\2\"\u00f6\3\2\2\2$\u0104\3\2\2\2&\u0109\3\2\2\2")
        buf.write("(\u010b\3\2\2\2*\u0119\3\2\2\2,\u012e\3\2\2\2.\u0134\3")
        buf.write("\2\2\2\60\u013e\3\2\2\2\62\u0140\3\2\2\2\64\u0146\3\2")
        buf.write("\2\2\66\u014a\3\2\2\28\u015d\3\2\2\2:\u015f\3\2\2\2<\u0167")
        buf.write("\3\2\2\2>\u016c\3\2\2\2@\u0174\3\2\2\2B\u0181\3\2\2\2")
        buf.write("D\u0189\3\2\2\2F\u01a9\3\2\2\2H\u01ab\3\2\2\2J\u01cb\3")
        buf.write("\2\2\2L\u01d9\3\2\2\2N\u01db\3\2\2\2P\u01e9\3\2\2\2R\u01f0")
        buf.write("\3\2\2\2T\u01f3\3\2\2\2V\u0201\3\2\2\2X\u0203\3\2\2\2")
        buf.write("Z\\\5\66\34\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2")
        buf.write("^_\3\2\2\2_`\7\2\2\3`\3\3\2\2\2ak\5\6\4\2bk\5\n\6\2ck")
        buf.write("\5\f\7\2dk\5\22\n\2ek\5\24\13\2fk\5\20\t\2gk\5\16\b\2")
        buf.write("hk\5H%\2ik\5\30\r\2ja\3\2\2\2jb\3\2\2\2jc\3\2\2\2jd\3")
        buf.write("\2\2\2je\3\2\2\2jf\3\2\2\2jg\3\2\2\2jh\3\2\2\2ji\3\2\2")
        buf.write("\2k\5\3\2\2\2lt\5\b\5\2mo\5*\26\2np\5\64\33\2on\3\2\2")
        buf.write("\2pq\3\2\2\2qo\3\2\2\2qr\3\2\2\2rt\3\2\2\2sl\3\2\2\2s")
        buf.write("m\3\2\2\2tu\3\2\2\2uv\7-\2\2vw\5\32\16\2wx\7\66\2\2x\7")
        buf.write("\3\2\2\2y\u0082\7=\2\2z{\5*\26\2{|\7\61\2\2|}\7=\2\2}")
        buf.write("\u0082\3\2\2\2~\177\7=\2\2\177\u0080\79\2\2\u0080\u0082")
        buf.write("\7<\2\2\u0081y\3\2\2\2\u0081z\3\2\2\2\u0081~\3\2\2\2\u0082")
        buf.write("\t\3\2\2\2\u0083\u0084\7\16\2\2\u0084\u0085\7\62\2\2\u0085")
        buf.write("\u0086\5\32\16\2\u0086\u0087\7\63\2\2\u0087\u0090\5\30")
        buf.write("\r\2\u0088\u0089\7\20\2\2\u0089\u008a\7\62\2\2\u008a\u008b")
        buf.write("\5\32\16\2\u008b\u008c\7\63\2\2\u008c\u008d\5\30\r\2\u008d")
        buf.write("\u008f\3\2\2\2\u008e\u0088\3\2\2\2\u008f\u0092\3\2\2\2")
        buf.write("\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0095\3")
        buf.write("\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094\7\23\2\2\u0094")
        buf.write("\u0096\5\30\r\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2")
        buf.write("\2\u0096\13\3\2\2\2\u0097\u0098\7\b\2\2\u0098\u0099\7")
        buf.write("\62\2\2\u0099\u009a\5\b\5\2\u009a\u009b\7\31\2\2\u009b")
        buf.write("\u009c\5\32\16\2\u009c\u009d\7\60\2\2\u009d\u00a0\5\32")
        buf.write("\16\2\u009e\u009f\7\32\2\2\u009f\u00a1\5\32\16\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\u00a3\7\63\2\2\u00a3\u00a4\5\30\r\2\u00a4\r\3\2")
        buf.write("\2\2\u00a5\u00a6\7\7\2\2\u00a6\u00a7\7\66\2\2\u00a7\17")
        buf.write("\3\2\2\2\u00a8\u00a9\7\13\2\2\u00a9\u00aa\7\66\2\2\u00aa")
        buf.write("\21\3\2\2\2\u00ab\u00ad\7\27\2\2\u00ac\u00ae\5\32\16\2")
        buf.write("\u00ad\u00ac\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\3")
        buf.write("\2\2\2\u00af\u00b0\7\66\2\2\u00b0\23\3\2\2\2\u00b1\u00b5")
        buf.write("\5,\27\2\u00b2\u00b4\5\26\f\2\u00b3\u00b2\3\2\2\2\u00b4")
        buf.write("\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6\u00b8\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\7")
        buf.write("\61\2\2\u00b9\u00ba\7=\2\2\u00ba\u00bb\5\62\32\2\u00bb")
        buf.write("\u00c1\3\2\2\2\u00bc\u00bd\7=\2\2\u00bd\u00be\79\2\2\u00be")
        buf.write("\u00bf\7<\2\2\u00bf\u00c1\5\62\32\2\u00c0\u00b1\3\2\2")
        buf.write("\2\u00c0\u00bc\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3")
        buf.write("\7\66\2\2\u00c3\25\3\2\2\2\u00c4\u00c5\7\61\2\2\u00c5")
        buf.write("\u00c7\7=\2\2\u00c6\u00c8\5\62\32\2\u00c7\u00c6\3\2\2")
        buf.write("\2\u00c7\u00c8\3\2\2\2\u00c8\27\3\2\2\2\u00c9\u00cd\7")
        buf.write("\64\2\2\u00ca\u00cc\5\4\3\2\u00cb\u00ca\3\2\2\2\u00cc")
        buf.write("\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2")
        buf.write("\u00ce\u00d0\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\7")
        buf.write("\65\2\2\u00d1\31\3\2\2\2\u00d2\u00d3\5\34\17\2\u00d3\u00d4")
        buf.write("\t\2\2\2\u00d4\u00d5\5\34\17\2\u00d5\u00d8\3\2\2\2\u00d6")
        buf.write("\u00d8\5\34\17\2\u00d7\u00d2\3\2\2\2\u00d7\u00d6\3\2\2")
        buf.write("\2\u00d8\33\3\2\2\2\u00d9\u00da\5\36\20\2\u00da\u00db")
        buf.write("\t\3\2\2\u00db\u00dc\5\36\20\2\u00dc\u00df\3\2\2\2\u00dd")
        buf.write("\u00df\5\36\20\2\u00de\u00d9\3\2\2\2\u00de\u00dd\3\2\2")
        buf.write("\2\u00df\35\3\2\2\2\u00e0\u00e1\b\20\1\2\u00e1\u00e2\5")
        buf.write(" \21\2\u00e2\u00e8\3\2\2\2\u00e3\u00e4\f\4\2\2\u00e4\u00e5")
        buf.write("\t\4\2\2\u00e5\u00e7\5 \21\2\u00e6\u00e3\3\2\2\2\u00e7")
        buf.write("\u00ea\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2")
        buf.write("\u00e9\37\3\2\2\2\u00ea\u00e8\3\2\2\2\u00eb\u00ec\b\21")
        buf.write("\1\2\u00ec\u00ed\5\"\22\2\u00ed\u00f3\3\2\2\2\u00ee\u00ef")
        buf.write("\f\4\2\2\u00ef\u00f0\t\5\2\2\u00f0\u00f2\5\"\22\2\u00f1")
        buf.write("\u00ee\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2")
        buf.write("\u00f3\u00f4\3\2\2\2\u00f4!\3\2\2\2\u00f5\u00f3\3\2\2")
        buf.write("\2\u00f6\u00f7\b\22\1\2\u00f7\u00f8\5$\23\2\u00f8\u00fe")
        buf.write("\3\2\2\2\u00f9\u00fa\f\4\2\2\u00fa\u00fb\t\6\2\2\u00fb")
        buf.write("\u00fd\5$\23\2\u00fc\u00f9\3\2\2\2\u00fd\u0100\3\2\2\2")
        buf.write("\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff#\3\2\2")
        buf.write("\2\u0100\u00fe\3\2\2\2\u0101\u0102\7$\2\2\u0102\u0105")
        buf.write("\5$\23\2\u0103\u0105\5&\24\2\u0104\u0101\3\2\2\2\u0104")
        buf.write("\u0103\3\2\2\2\u0105%\3\2\2\2\u0106\u0107\7 \2\2\u0107")
        buf.write("\u010a\5&\24\2\u0108\u010a\5(\25\2\u0109\u0106\3\2\2\2")
        buf.write("\u0109\u0108\3\2\2\2\u010a\'\3\2\2\2\u010b\u010c\b\25")
        buf.write("\1\2\u010c\u010d\5*\26\2\u010d\u0116\3\2\2\2\u010e\u0110")
        buf.write("\f\4\2\2\u010f\u0111\5\64\33\2\u0110\u010f\3\2\2\2\u0111")
        buf.write("\u0112\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2")
        buf.write("\u0113\u0115\3\2\2\2\u0114\u010e\3\2\2\2\u0115\u0118\3")
        buf.write("\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117)")
        buf.write("\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011a\b\26\1\2\u011a")
        buf.write("\u011b\5,\27\2\u011b\u0124\3\2\2\2\u011c\u011d\f\4\2\2")
        buf.write("\u011d\u011e\7\61\2\2\u011e\u0120\7=\2\2\u011f\u0121\5")
        buf.write("\62\32\2\u0120\u011f\3\2\2\2\u0120\u0121\3\2\2\2\u0121")
        buf.write("\u0123\3\2\2\2\u0122\u011c\3\2\2\2\u0123\u0126\3\2\2\2")
        buf.write("\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125+\3\2\2")
        buf.write("\2\u0126\u0124\3\2\2\2\u0127\u0128\7=\2\2\u0128\u0129")
        buf.write("\79\2\2\u0129\u012b\7<\2\2\u012a\u012c\5\62\32\2\u012b")
        buf.write("\u012a\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012f\3\2\2\2")
        buf.write("\u012d\u012f\5.\30\2\u012e\u0127\3\2\2\2\u012e\u012d\3")
        buf.write("\2\2\2\u012f-\3\2\2\2\u0130\u0131\7\30\2\2\u0131\u0132")
        buf.write("\7=\2\2\u0132\u0135\5\62\32\2\u0133\u0135\5\60\31\2\u0134")
        buf.write("\u0130\3\2\2\2\u0134\u0133\3\2\2\2\u0135/\3\2\2\2\u0136")
        buf.write("\u013f\5V,\2\u0137\u013f\7\36\2\2\u0138\u013f\7\n\2\2")
        buf.write("\u0139\u013f\7=\2\2\u013a\u013b\7\62\2\2\u013b\u013c\5")
        buf.write("\32\16\2\u013c\u013d\7\63\2\2\u013d\u013f\3\2\2\2\u013e")
        buf.write("\u0136\3\2\2\2\u013e\u0137\3\2\2\2\u013e\u0138\3\2\2\2")
        buf.write("\u013e\u0139\3\2\2\2\u013e\u013a\3\2\2\2\u013f\61\3\2")
        buf.write("\2\2\u0140\u0142\7\62\2\2\u0141\u0143\5J&\2\u0142\u0141")
        buf.write("\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0144\3\2\2\2\u0144")
        buf.write("\u0145\7\63\2\2\u0145\63\3\2\2\2\u0146\u0147\7\67\2\2")
        buf.write("\u0147\u0148\5\32\16\2\u0148\u0149\78\2\2\u0149\65\3\2")
        buf.write("\2\2\u014a\u014b\7\33\2\2\u014b\u014e\7=\2\2\u014c\u014d")
        buf.write("\7:\2\2\u014d\u014f\7=\2\2\u014e\u014c\3\2\2\2\u014e\u014f")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0154\7\64\2\2\u0151")
        buf.write("\u0153\58\35\2\u0152\u0151\3\2\2\2\u0153\u0156\3\2\2\2")
        buf.write("\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0157\3")
        buf.write("\2\2\2\u0156\u0154\3\2\2\2\u0157\u0158\7\65\2\2\u0158")
        buf.write("\67\3\2\2\2\u0159\u015e\5> \2\u015a\u015e\5D#\2\u015b")
        buf.write("\u015e\5:\36\2\u015c\u015e\5<\37\2\u015d\u0159\3\2\2\2")
        buf.write("\u015d\u015a\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015c\3")
        buf.write("\2\2\2\u015e9\3\2\2\2\u015f\u0160\7\34\2\2\u0160\u0162")
        buf.write("\7\62\2\2\u0161\u0163\5@!\2\u0162\u0161\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\7\63\2")
        buf.write("\2\u0165\u0166\5\30\r\2\u0166;\3\2\2\2\u0167\u0168\7\35")
        buf.write("\2\2\u0168\u0169\7\62\2\2\u0169\u016a\7\63\2\2\u016a\u016b")
        buf.write("\5\30\r\2\u016b=\3\2\2\2\u016c\u016d\t\7\2\2\u016d\u016f")
        buf.write("\7\62\2\2\u016e\u0170\5@!\2\u016f\u016e\3\2\2\2\u016f")
        buf.write("\u0170\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0172\7\63\2")
        buf.write("\2\u0172\u0173\5\30\r\2\u0173?\3\2\2\2\u0174\u0175\5B")
        buf.write("\"\2\u0175\u0176\7:\2\2\u0176\u017e\5L\'\2\u0177\u0178")
        buf.write("\7\66\2\2\u0178\u0179\5B\"\2\u0179\u017a\7:\2\2\u017a")
        buf.write("\u017b\5L\'\2\u017b\u017d\3\2\2\2\u017c\u0177\3\2\2\2")
        buf.write("\u017d\u0180\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3")
        buf.write("\2\2\2\u017fA\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0186")
        buf.write("\7=\2\2\u0182\u0183\7;\2\2\u0183\u0185\7=\2\2\u0184\u0182")
        buf.write("\3\2\2\2\u0185\u0188\3\2\2\2\u0186\u0184\3\2\2\2\u0186")
        buf.write("\u0187\3\2\2\2\u0187C\3\2\2\2\u0188\u0186\3\2\2\2\u0189")
        buf.write("\u018a\t\b\2\2\u018a\u0190\5F$\2\u018b\u018c\7;\2\2\u018c")
        buf.write("\u018d\b#\1\2\u018d\u018f\5F$\2\u018e\u018b\3\2\2\2\u018f")
        buf.write("\u0192\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2")
        buf.write("\u0191\u0193\3\2\2\2\u0192\u0190\3\2\2\2\u0193\u0194\7")
        buf.write(":\2\2\u0194\u01a1\5L\'\2\u0195\u0196\7-\2\2\u0196\u0197")
        buf.write("\b#\1\2\u0197\u019e\5\32\16\2\u0198\u0199\6#\7\3\u0199")
        buf.write("\u019a\7;\2\2\u019a\u019b\b#\1\2\u019b\u019d\5\32\16\2")
        buf.write("\u019c\u0198\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3")
        buf.write("\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0\u019e")
        buf.write("\3\2\2\2\u01a1\u0195\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01a7\3\2\2\2\u01a3\u01a4\6#\b\3\u01a4\u01a8\7\66\2\2")
        buf.write("\u01a5\u01a6\6#\t\3\u01a6\u01a8\7\66\2\2\u01a7\u01a3\3")
        buf.write("\2\2\2\u01a7\u01a5\3\2\2\2\u01a8E\3\2\2\2\u01a9\u01aa")
        buf.write("\t\7\2\2\u01aaG\3\2\2\2\u01ab\u01ac\t\b\2\2\u01ac\u01b2")
        buf.write("\7=\2\2\u01ad\u01ae\7;\2\2\u01ae\u01af\b%\1\2\u01af\u01b1")
        buf.write("\7=\2\2\u01b0\u01ad\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2")
        buf.write("\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2")
        buf.write("\u01b4\u01b2\3\2\2\2\u01b5\u01b6\7:\2\2\u01b6\u01c3\5")
        buf.write("L\'\2\u01b7\u01b8\7-\2\2\u01b8\u01b9\b%\1\2\u01b9\u01c0")
        buf.write("\5\32\16\2\u01ba\u01bb\6%\n\3\u01bb\u01bc\7;\2\2\u01bc")
        buf.write("\u01bd\b%\1\2\u01bd\u01bf\5\32\16\2\u01be\u01ba\3\2\2")
        buf.write("\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3")
        buf.write("\u01b7\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c9\3\2\2\2")
        buf.write("\u01c5\u01c6\6%\13\3\u01c6\u01ca\7\66\2\2\u01c7\u01c8")
        buf.write("\6%\f\3\u01c8\u01ca\7\66\2\2\u01c9\u01c5\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01caI\3\2\2\2\u01cb\u01d0\5\32\16\2\u01cc")
        buf.write("\u01cd\7;\2\2\u01cd\u01cf\5\32\16\2\u01ce\u01cc\3\2\2")
        buf.write("\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1")
        buf.write("\3\2\2\2\u01d1K\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01da")
        buf.write("\7\22\2\2\u01d4\u01da\7\t\2\2\u01d5\u01da\7\24\2\2\u01d6")
        buf.write("\u01da\5N(\2\u01d7\u01da\7\r\2\2\u01d8\u01da\7=\2\2\u01d9")
        buf.write("\u01d3\3\2\2\2\u01d9\u01d4\3\2\2\2\u01d9\u01d5\3\2\2\2")
        buf.write("\u01d9\u01d6\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01d8\3")
        buf.write("\2\2\2\u01daM\3\2\2\2\u01db\u01dc\7\21\2\2\u01dc\u01e2")
        buf.write("\7\67\2\2\u01dd\u01e3\5N(\2\u01de\u01e3\7\22\2\2\u01df")
        buf.write("\u01e3\7\t\2\2\u01e0\u01e3\7\24\2\2\u01e1\u01e3\7\r\2")
        buf.write("\2\u01e2\u01dd\3\2\2\2\u01e2\u01de\3\2\2\2\u01e2\u01df")
        buf.write("\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e1\3\2\2\2\u01e3")
        buf.write("\u01e4\3\2\2\2\u01e4\u01e5\7;\2\2\u01e5\u01e6\6(\r\2\u01e6")
        buf.write("\u01e7\7\3\2\2\u01e7\u01e8\78\2\2\u01e8O\3\2\2\2\u01e9")
        buf.write("\u01ea\7\21\2\2\u01ea\u01ec\7\62\2\2\u01eb\u01ed\5T+\2")
        buf.write("\u01ec\u01eb\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01ee\3")
        buf.write("\2\2\2\u01ee\u01ef\7\63\2\2\u01efQ\3\2\2\2\u01f0\u01f1")
        buf.write("\7\21\2\2\u01f1\u01f2\5\62\32\2\u01f2S\3\2\2\2\u01f3\u01f8")
        buf.write("\5R*\2\u01f4\u01f5\7;\2\2\u01f5\u01f7\5R*\2\u01f6\u01f4")
        buf.write("\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8")
        buf.write("\u01f9\3\2\2\2\u01f9U\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fb")
        buf.write("\u0202\7\3\2\2\u01fc\u0202\7\4\2\2\u01fd\u0202\5X-\2\u01fe")
        buf.write("\u0202\7\5\2\2\u01ff\u0202\5R*\2\u0200\u0202\5P)\2\u0201")
        buf.write("\u01fb\3\2\2\2\u0201\u01fc\3\2\2\2\u0201\u01fd\3\2\2\2")
        buf.write("\u0201\u01fe\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0200\3")
        buf.write("\2\2\2\u0202W\3\2\2\2\u0203\u0204\t\t\2\2\u0204Y\3\2\2")
        buf.write("\2\64]jqs\u0081\u0090\u0095\u00a0\u00ad\u00b5\u00c0\u00c7")
        buf.write("\u00cd\u00d7\u00de\u00e8\u00f3\u00fe\u0104\u0109\u0112")
        buf.write("\u0116\u0120\u0124\u012b\u012e\u0134\u013e\u0142\u014e")
        buf.write("\u0154\u015d\u0162\u016f\u017e\u0186\u0190\u019e\u01a1")
        buf.write("\u01a7\u01b2\u01c0\u01c3\u01c9\u01d0\u01d9\u01e2\u01ec")
        buf.write("\u01f8\u0201")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'Break'", "'Foreach'", "'Boolean'", "'Null'", 
                     "'Continue'", "'True'", "'String'", "'If'", "'False'", 
                     "'Elseif'", "'Array'", "'Int'", "'Else'", "'Float'", 
                     "'Var'", "'Val'", "'Return'", "'New'", "'In'", "'By'", 
                     "'Class'", "'Constructor'", "'Destructor'", "'Self'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'||'", "'&&'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'='", 
                     "'==.'", "'+.'", "'..'", "'.'", "'('", "')'", "'{'", 
                     "'}'", "';'", "'['", "']'", "'::'", "':'", "','" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "STRING", "COMMENT", 
                      "BREAKTYPE", "FOREACHTYPE", "BOOLEANTYPE", "NULLTYPE", 
                      "CONTINUETYPE", "TRUETYPE", "STRINGTYPE", "IF", "FALSETYPE", 
                      "ELSEIF", "ARRAYTYPE", "INTTYPE", "ELSE", "FLOATTYPE", 
                      "VARTYPE", "CONSTTYPE", "RETURNTYPE", "NEW", "INKEY", 
                      "BYKEY", "CLASSTYPE", "CONSTRUCTORTYPE", "DESTRUCTORTYPE", 
                      "SELFTYPE", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                      "OR", "AND", "EQUAL", "NOTEQUAL", "LESS", "GREATER", 
                      "LESSEQUAL", "GREATEREQUAL", "ASSIGN", "STRINGEQUAL", 
                      "CONCATENATION", "DOTDOT", "DOT", "LB", "RB", "LP", 
                      "RP", "SEMI", "LSB", "RSB", "TWOCOLON", "COLON", "COMMA", 
                      "DOLLAR_ID", "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_lhs = 2
    RULE_scalavar = 3
    RULE_ifstatement = 4
    RULE_forstatement = 5
    RULE_breakstatement = 6
    RULE_continuestatement = 7
    RULE_returnstatement = 8
    RULE_invokemethod = 9
    RULE_partinvoke = 10
    RULE_blockstatement = 11
    RULE_exp = 12
    RULE_exp1 = 13
    RULE_exp2 = 14
    RULE_exp3 = 15
    RULE_exp4 = 16
    RULE_exp5 = 17
    RULE_exp6 = 18
    RULE_exp7 = 19
    RULE_exp8 = 20
    RULE_exp9 = 21
    RULE_exp10 = 22
    RULE_operands = 23
    RULE_paramexp = 24
    RULE_indexop = 25
    RULE_classname = 26
    RULE_memclass = 27
    RULE_construct = 28
    RULE_destruct = 29
    RULE_method = 30
    RULE_parameters = 31
    RULE_idlist = 32
    RULE_attr = 33
    RULE_idattr = 34
    RULE_vardecl = 35
    RULE_explist = 36
    RULE_datatype = 37
    RULE_arraynested = 38
    RULE_multiarrayindex = 39
    RULE_arrayindex = 40
    RULE_indexlist = 41
    RULE_value = 42
    RULE_booln = 43

    ruleNames =  [ "program", "statement", "lhs", "scalavar", "ifstatement", 
                   "forstatement", "breakstatement", "continuestatement", 
                   "returnstatement", "invokemethod", "partinvoke", "blockstatement", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "exp9", "exp10", "operands", "paramexp", 
                   "indexop", "classname", "memclass", "construct", "destruct", 
                   "method", "parameters", "idlist", "attr", "idattr", "vardecl", 
                   "explist", "datatype", "arraynested", "multiarrayindex", 
                   "arrayindex", "indexlist", "value", "booln" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    STRING=3
    COMMENT=4
    BREAKTYPE=5
    FOREACHTYPE=6
    BOOLEANTYPE=7
    NULLTYPE=8
    CONTINUETYPE=9
    TRUETYPE=10
    STRINGTYPE=11
    IF=12
    FALSETYPE=13
    ELSEIF=14
    ARRAYTYPE=15
    INTTYPE=16
    ELSE=17
    FLOATTYPE=18
    VARTYPE=19
    CONSTTYPE=20
    RETURNTYPE=21
    NEW=22
    INKEY=23
    BYKEY=24
    CLASSTYPE=25
    CONSTRUCTORTYPE=26
    DESTRUCTORTYPE=27
    SELFTYPE=28
    ADD=29
    SUB=30
    MUL=31
    DIV=32
    MOD=33
    NOT=34
    OR=35
    AND=36
    EQUAL=37
    NOTEQUAL=38
    LESS=39
    GREATER=40
    LESSEQUAL=41
    GREATEREQUAL=42
    ASSIGN=43
    STRINGEQUAL=44
    CONCATENATION=45
    DOTDOT=46
    DOT=47
    LB=48
    RB=49
    LP=50
    RP=51
    SEMI=52
    LSB=53
    RSB=54
    TWOCOLON=55
    COLON=56
    COMMA=57
    DOLLAR_ID=58
    ID=59
    WS=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62
    ERROR_TOKEN=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def classname(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ClassnameContext)
            else:
                return self.getTypedRuleContext(D96Parser.ClassnameContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 88
                self.classname()
                self.state = 91 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASSTYPE):
                    break

            self.state = 93
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def ifstatement(self):
            return self.getTypedRuleContext(D96Parser.IfstatementContext,0)


        def forstatement(self):
            return self.getTypedRuleContext(D96Parser.ForstatementContext,0)


        def returnstatement(self):
            return self.getTypedRuleContext(D96Parser.ReturnstatementContext,0)


        def invokemethod(self):
            return self.getTypedRuleContext(D96Parser.InvokemethodContext,0)


        def continuestatement(self):
            return self.getTypedRuleContext(D96Parser.ContinuestatementContext,0)


        def breakstatement(self):
            return self.getTypedRuleContext(D96Parser.BreakstatementContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(D96Parser.VardeclContext,0)


        def blockstatement(self):
            return self.getTypedRuleContext(D96Parser.BlockstatementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.lhs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.ifstatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.forstatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.returnstatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 99
                self.invokemethod()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 100
                self.continuestatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 101
                self.breakstatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 102
                self.vardecl()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 103
                self.blockstatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def scalavar(self):
            return self.getTypedRuleContext(D96Parser.ScalavarContext,0)


        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def indexop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IndexopContext)
            else:
                return self.getTypedRuleContext(D96Parser.IndexopContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 106
                self.scalavar()
                pass

            elif la_ == 2:
                self.state = 107
                self.exp8(0)
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 108
                    self.indexop()
                    self.state = 111 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.LSB):
                        break

                pass


            self.state = 115
            self.match(D96Parser.ASSIGN)
            self.state = 116
            self.exp()
            self.state = 117
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalavarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def TWOCOLON(self):
            return self.getToken(D96Parser.TWOCOLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_scalavar




    def scalavar(self):

        localctx = D96Parser.ScalavarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_scalavar)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.exp8(0)
                self.state = 121
                self.match(D96Parser.DOT)
                self.state = 122
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.match(D96Parser.ID)
                self.state = 125
                self.match(D96Parser.TWOCOLON)
                self.state = 126
                self.match(D96Parser.DOLLAR_ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LB)
            else:
                return self.getToken(D96Parser.LB, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RB)
            else:
                return self.getToken(D96Parser.RB, i)

        def blockstatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.BlockstatementContext)
            else:
                return self.getTypedRuleContext(D96Parser.BlockstatementContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ELSEIF)
            else:
                return self.getToken(D96Parser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_ifstatement




    def ifstatement(self):

        localctx = D96Parser.IfstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(D96Parser.IF)
            self.state = 130
            self.match(D96Parser.LB)
            self.state = 131
            self.exp()
            self.state = 132
            self.match(D96Parser.RB)
            self.state = 133
            self.blockstatement()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 134
                self.match(D96Parser.ELSEIF)
                self.state = 135
                self.match(D96Parser.LB)
                self.state = 136
                self.exp()
                self.state = 137
                self.match(D96Parser.RB)
                self.state = 138
                self.blockstatement()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 145
                self.match(D96Parser.ELSE)
                self.state = 146
                self.blockstatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACHTYPE(self):
            return self.getToken(D96Parser.FOREACHTYPE, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def scalavar(self):
            return self.getTypedRuleContext(D96Parser.ScalavarContext,0)


        def INKEY(self):
            return self.getToken(D96Parser.INKEY, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def DOTDOT(self):
            return self.getToken(D96Parser.DOTDOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstatement(self):
            return self.getTypedRuleContext(D96Parser.BlockstatementContext,0)


        def BYKEY(self):
            return self.getToken(D96Parser.BYKEY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forstatement




    def forstatement(self):

        localctx = D96Parser.ForstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_forstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(D96Parser.FOREACHTYPE)
            self.state = 150
            self.match(D96Parser.LB)
            self.state = 151
            self.scalavar()
            self.state = 152
            self.match(D96Parser.INKEY)
            self.state = 153
            self.exp()
            self.state = 154
            self.match(D96Parser.DOTDOT)
            self.state = 155
            self.exp()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BYKEY:
                self.state = 156
                self.match(D96Parser.BYKEY)
                self.state = 157
                self.exp()


            self.state = 160
            self.match(D96Parser.RB)
            self.state = 161
            self.blockstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAKTYPE(self):
            return self.getToken(D96Parser.BREAKTYPE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_breakstatement




    def breakstatement(self):

        localctx = D96Parser.BreakstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_breakstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(D96Parser.BREAKTYPE)
            self.state = 164
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUETYPE(self):
            return self.getToken(D96Parser.CONTINUETYPE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continuestatement




    def continuestatement(self):

        localctx = D96Parser.ContinuestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_continuestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(D96Parser.CONTINUETYPE)
            self.state = 167
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURNTYPE(self):
            return self.getToken(D96Parser.RETURNTYPE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_returnstatement




    def returnstatement(self):

        localctx = D96Parser.ReturnstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_returnstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(D96Parser.RETURNTYPE)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.STRING) | (1 << D96Parser.NULLTYPE) | (1 << D96Parser.TRUETYPE) | (1 << D96Parser.FALSETYPE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.NEW) | (1 << D96Parser.SELFTYPE) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.ID))) != 0):
                self.state = 170
                self.exp()


            self.state = 173
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvokemethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def paramexp(self):
            return self.getTypedRuleContext(D96Parser.ParamexpContext,0)


        def TWOCOLON(self):
            return self.getToken(D96Parser.TWOCOLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def partinvoke(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.PartinvokeContext)
            else:
                return self.getTypedRuleContext(D96Parser.PartinvokeContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_invokemethod




    def invokemethod(self):

        localctx = D96Parser.InvokemethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_invokemethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 175
                self.exp9()
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 176
                        self.partinvoke() 
                    self.state = 181
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                self.state = 182
                self.match(D96Parser.DOT)
                self.state = 183
                self.match(D96Parser.ID)
                self.state = 184
                self.paramexp()
                pass

            elif la_ == 2:
                self.state = 186
                self.match(D96Parser.ID)
                self.state = 187
                self.match(D96Parser.TWOCOLON)
                self.state = 188
                self.match(D96Parser.DOLLAR_ID)
                self.state = 189
                self.paramexp()
                pass


            self.state = 192
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PartinvokeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def paramexp(self):
            return self.getTypedRuleContext(D96Parser.ParamexpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_partinvoke




    def partinvoke(self):

        localctx = D96Parser.PartinvokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_partinvoke)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(D96Parser.DOT)
            self.state = 195
            self.match(D96Parser.ID)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.LB:
                self.state = 196
                self.paramexp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StatementContext)
            else:
                return self.getTypedRuleContext(D96Parser.StatementContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_blockstatement




    def blockstatement(self):

        localctx = D96Parser.BlockstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_blockstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(D96Parser.LP)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.STRING) | (1 << D96Parser.BREAKTYPE) | (1 << D96Parser.FOREACHTYPE) | (1 << D96Parser.NULLTYPE) | (1 << D96Parser.CONTINUETYPE) | (1 << D96Parser.TRUETYPE) | (1 << D96Parser.IF) | (1 << D96Parser.FALSETYPE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.VARTYPE) | (1 << D96Parser.CONSTTYPE) | (1 << D96Parser.RETURNTYPE) | (1 << D96Parser.NEW) | (1 << D96Parser.SELFTYPE) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.ID))) != 0):
                self.state = 200
                self.statement()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp1Context,i)


        def CONCATENATION(self):
            return self.getToken(D96Parser.CONCATENATION, 0)

        def STRINGEQUAL(self):
            return self.getToken(D96Parser.STRINGEQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.exp1()
                self.state = 209
                _la = self._input.LA(1)
                if not(_la==D96Parser.STRINGEQUAL or _la==D96Parser.CONCATENATION):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 210
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp2Context,i)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(D96Parser.NOTEQUAL, 0)

        def LESS(self):
            return self.getToken(D96Parser.LESS, 0)

        def GREATER(self):
            return self.getToken(D96Parser.GREATER, 0)

        def LESSEQUAL(self):
            return self.getToken(D96Parser.LESSEQUAL, 0)

        def GREATEREQUAL(self):
            return self.getToken(D96Parser.GREATEREQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp1




    def exp1(self):

        localctx = D96Parser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.exp2(0)
                self.state = 216
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOTEQUAL) | (1 << D96Parser.LESS) | (1 << D96Parser.GREATER) | (1 << D96Parser.LESSEQUAL) | (1 << D96Parser.GREATEREQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 217
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 225
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 226
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OR or _la==D96Parser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 227
                    self.exp3(0) 
                self.state = 232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 236
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 237
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 238
                    self.exp4(0) 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp4



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 247
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 248
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 249
                    self.exp5() 
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp5




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp5)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(D96Parser.NOT)
                self.state = 256
                self.exp5()
                pass
            elif token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.STRING, D96Parser.NULLTYPE, D96Parser.TRUETYPE, D96Parser.FALSETYPE, D96Parser.ARRAYTYPE, D96Parser.NEW, D96Parser.SELFTYPE, D96Parser.SUB, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.exp6()
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


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp6




    def exp6(self):

        localctx = D96Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exp6)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(D96Parser.SUB)
                self.state = 261
                self.exp6()
                pass
            elif token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.STRING, D96Parser.NULLTYPE, D96Parser.TRUETYPE, D96Parser.FALSETYPE, D96Parser.ARRAYTYPE, D96Parser.NEW, D96Parser.SELFTYPE, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.exp7(0)
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


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def indexop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IndexopContext)
            else:
                return self.getTypedRuleContext(D96Parser.IndexopContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_exp7



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.exp8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 276
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 268
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 270 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 269
                            self.indexop()

                        else:
                            raise NoViableAltException(self)
                        self.state = 272 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
             
                self.state = 278
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def paramexp(self):
            return self.getTypedRuleContext(D96Parser.ParamexpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp8



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 282
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 283
                    self.match(D96Parser.DOT)
                    self.state = 284
                    self.match(D96Parser.ID)
                    self.state = 286
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        self.state = 285
                        self.paramexp()

             
                self.state = 292
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def TWOCOLON(self):
            return self.getToken(D96Parser.TWOCOLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def paramexp(self):
            return self.getTypedRuleContext(D96Parser.ParamexpContext,0)


        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp9




    def exp9(self):

        localctx = D96Parser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp9)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(D96Parser.ID)
                self.state = 294
                self.match(D96Parser.TWOCOLON)
                self.state = 295
                self.match(D96Parser.DOLLAR_ID)
                self.state = 297
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 296
                    self.paramexp()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.exp10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def paramexp(self):
            return self.getTypedRuleContext(D96Parser.ParamexpContext,0)


        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp10




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp10)
        try:
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.match(D96Parser.NEW)
                self.state = 303
                self.match(D96Parser.ID)
                self.state = 304
                self.paramexp()
                pass
            elif token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.STRING, D96Parser.NULLTYPE, D96Parser.TRUETYPE, D96Parser.FALSETYPE, D96Parser.ARRAYTYPE, D96Parser.SELFTYPE, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.operands()
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


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(D96Parser.ValueContext,0)


        def SELFTYPE(self):
            return self.getToken(D96Parser.SELFTYPE, 0)

        def NULLTYPE(self):
            return self.getToken(D96Parser.NULLTYPE, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operands




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_operands)
        try:
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.STRING, D96Parser.TRUETYPE, D96Parser.FALSETYPE, D96Parser.ARRAYTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.value()
                pass
            elif token in [D96Parser.SELFTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.match(D96Parser.SELFTYPE)
                pass
            elif token in [D96Parser.NULLTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 310
                self.match(D96Parser.NULLTYPE)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 311
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 312
                self.match(D96Parser.LB)
                self.state = 313
                self.exp()
                self.state = 314
                self.match(D96Parser.RB)
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


    class ParamexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def explist(self):
            return self.getTypedRuleContext(D96Parser.ExplistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_paramexp




    def paramexp(self):

        localctx = D96Parser.ParamexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_paramexp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(D96Parser.LB)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.STRING) | (1 << D96Parser.NULLTYPE) | (1 << D96Parser.TRUETYPE) | (1 << D96Parser.FALSETYPE) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.NEW) | (1 << D96Parser.SELFTYPE) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.ID))) != 0):
                self.state = 319
                self.explist()


            self.state = 322
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_indexop




    def indexop(self):

        localctx = D96Parser.IndexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_indexop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(D96Parser.LSB)
            self.state = 325
            self.exp()
            self.state = 326
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassnameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASSTYPE(self):
            return self.getToken(D96Parser.CLASSTYPE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def memclass(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.MemclassContext)
            else:
                return self.getTypedRuleContext(D96Parser.MemclassContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_classname




    def classname(self):

        localctx = D96Parser.ClassnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_classname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(D96Parser.CLASSTYPE)
            self.state = 329
            self.match(D96Parser.ID)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 330
                self.match(D96Parser.COLON)
                self.state = 331
                self.match(D96Parser.ID)


            self.state = 334
            self.match(D96Parser.LP)
            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VARTYPE) | (1 << D96Parser.CONSTTYPE) | (1 << D96Parser.CONSTRUCTORTYPE) | (1 << D96Parser.DESTRUCTORTYPE) | (1 << D96Parser.DOLLAR_ID) | (1 << D96Parser.ID))) != 0):
                self.state = 335
                self.memclass()
                self.state = 340
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 341
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemclassContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method(self):
            return self.getTypedRuleContext(D96Parser.MethodContext,0)


        def attr(self):
            return self.getTypedRuleContext(D96Parser.AttrContext,0)


        def construct(self):
            return self.getTypedRuleContext(D96Parser.ConstructContext,0)


        def destruct(self):
            return self.getTypedRuleContext(D96Parser.DestructContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_memclass




    def memclass(self):

        localctx = D96Parser.MemclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_memclass)
        try:
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOLLAR_ID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.method()
                pass
            elif token in [D96Parser.VARTYPE, D96Parser.CONSTTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.attr()
                pass
            elif token in [D96Parser.CONSTRUCTORTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.construct()
                pass
            elif token in [D96Parser.DESTRUCTORTYPE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 346
                self.destruct()
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


    class ConstructContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTORTYPE(self):
            return self.getToken(D96Parser.CONSTRUCTORTYPE, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstatement(self):
            return self.getTypedRuleContext(D96Parser.BlockstatementContext,0)


        def parameters(self):
            return self.getTypedRuleContext(D96Parser.ParametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_construct




    def construct(self):

        localctx = D96Parser.ConstructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_construct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(D96Parser.CONSTRUCTORTYPE)
            self.state = 350
            self.match(D96Parser.LB)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 351
                self.parameters()


            self.state = 354
            self.match(D96Parser.RB)
            self.state = 355
            self.blockstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTORTYPE(self):
            return self.getToken(D96Parser.DESTRUCTORTYPE, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstatement(self):
            return self.getTypedRuleContext(D96Parser.BlockstatementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destruct




    def destruct(self):

        localctx = D96Parser.DestructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_destruct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(D96Parser.DESTRUCTORTYPE)
            self.state = 358
            self.match(D96Parser.LB)
            self.state = 359
            self.match(D96Parser.RB)
            self.state = 360
            self.blockstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstatement(self):
            return self.getTypedRuleContext(D96Parser.BlockstatementContext,0)


        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def parameters(self):
            return self.getTypedRuleContext(D96Parser.ParametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method




    def method(self):

        localctx = D96Parser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            _la = self._input.LA(1)
            if not(_la==D96Parser.DOLLAR_ID or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 363
            self.match(D96Parser.LB)
            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 364
                self.parameters()


            self.state = 367
            self.match(D96Parser.RB)
            self.state = 368
            self.blockstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IdlistContext)
            else:
                return self.getTypedRuleContext(D96Parser.IdlistContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COLON)
            else:
                return self.getToken(D96Parser.COLON, i)

        def datatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.DatatypeContext)
            else:
                return self.getTypedRuleContext(D96Parser.DatatypeContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_parameters




    def parameters(self):

        localctx = D96Parser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.idlist()
            self.state = 371
            self.match(D96Parser.COLON)
            self.state = 372
            self.datatype()
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 373
                self.match(D96Parser.SEMI)
                self.state = 374
                self.idlist()
                self.state = 375
                self.match(D96Parser.COLON)
                self.state = 376
                self.datatype()
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_idlist




    def idlist(self):

        localctx = D96Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(D96Parser.ID)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 384
                self.match(D96Parser.COMMA)
                self.state = 385
                self.match(D96Parser.ID)
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.lst = []

        def idattr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IdattrContext)
            else:
                return self.getTypedRuleContext(D96Parser.IdattrContext,i)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def datatype(self):
            return self.getTypedRuleContext(D96Parser.DatatypeContext,0)


        def VARTYPE(self):
            return self.getToken(D96Parser.VARTYPE, 0)

        def CONSTTYPE(self):
            return self.getToken(D96Parser.CONSTTYPE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_attr




    def attr(self):

        localctx = D96Parser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_attr)
        getInvokingContext(33).lst = [0,0,0]
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARTYPE or _la==D96Parser.CONSTTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 392
            self.idattr()
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 393
                self.match(D96Parser.COMMA)
                getInvokingContext(33).lst[0] += 1
                self.state = 395
                self.idattr()
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 401
            self.match(D96Parser.COLON)
            self.state = 402
            self.datatype()
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 403
                self.match(D96Parser.ASSIGN)
                getInvokingContext(33).lst[1] = 1
                self.state = 405
                self.exp()
                self.state = 412
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 406
                        if not getInvokingContext(33).lst[2] < getInvokingContext(33).lst[0]:
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "$attr::lst[2] < $attr::lst[0]")
                        self.state = 407
                        self.match(D96Parser.COMMA)
                        getInvokingContext(33).lst[2] += 1
                        self.state = 409
                        self.exp() 
                    self.state = 414
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,37,self._ctx)



            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 417
                if not getInvokingContext(33).lst[0] == getInvokingContext(33).lst[2] and getInvokingContext(33).lst[1] == 1:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$attr::lst[0] == $attr::lst[2] and $attr::lst[1] == 1")
                self.state = 418
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.state = 419
                if not getInvokingContext(33).lst[1] == 0:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$attr::lst[1] == 0")
                self.state = 420
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdattrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_idattr




    def idattr(self):

        localctx = D96Parser.IdattrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_idattr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            _la = self._input.LA(1)
            if not(_la==D96Parser.DOLLAR_ID or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.lst = []

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def datatype(self):
            return self.getTypedRuleContext(D96Parser.DatatypeContext,0)


        def VARTYPE(self):
            return self.getToken(D96Parser.VARTYPE, 0)

        def CONSTTYPE(self):
            return self.getToken(D96Parser.CONSTTYPE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_vardecl




    def vardecl(self):

        localctx = D96Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_vardecl)
        getInvokingContext(35).lst = [0,0,0]
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARTYPE or _la==D96Parser.CONSTTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 426
            self.match(D96Parser.ID)
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 427
                self.match(D96Parser.COMMA)
                getInvokingContext(35).lst[0] += 1
                self.state = 429
                self.match(D96Parser.ID)
                self.state = 434
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 435
            self.match(D96Parser.COLON)
            self.state = 436
            self.datatype()
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 437
                self.match(D96Parser.ASSIGN)
                getInvokingContext(35).lst[1] = 1
                self.state = 439
                self.exp()
                self.state = 446
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 440
                        if not getInvokingContext(35).lst[2] < getInvokingContext(35).lst[0]:
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "$vardecl::lst[2] < $vardecl::lst[0]")
                        self.state = 441
                        self.match(D96Parser.COMMA)
                        getInvokingContext(35).lst[2] += 1
                        self.state = 443
                        self.exp() 
                    self.state = 448
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,41,self._ctx)



            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 451
                if not getInvokingContext(35).lst[0] == getInvokingContext(35).lst[2] and getInvokingContext(35).lst[1] == 1:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$vardecl::lst[0] == $vardecl::lst[2] and $vardecl::lst[1] == 1")
                self.state = 452
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.state = 453
                if not getInvokingContext(35).lst[1] == 0:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$vardecl::lst[1] == 0")
                self.state = 454
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_explist




    def explist(self):

        localctx = D96Parser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_explist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.exp()
            self.state = 462
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 458
                self.match(D96Parser.COMMA)
                self.state = 459
                self.exp()
                self.state = 464
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatatypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def BOOLEANTYPE(self):
            return self.getToken(D96Parser.BOOLEANTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(D96Parser.FLOATTYPE, 0)

        def arraynested(self):
            return self.getTypedRuleContext(D96Parser.ArraynestedContext,0)


        def STRINGTYPE(self):
            return self.getToken(D96Parser.STRINGTYPE, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_datatype




    def datatype(self):

        localctx = D96Parser.DatatypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_datatype)
        try:
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.match(D96Parser.INTTYPE)
                pass
            elif token in [D96Parser.BOOLEANTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.match(D96Parser.BOOLEANTYPE)
                pass
            elif token in [D96Parser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 467
                self.match(D96Parser.FLOATTYPE)
                pass
            elif token in [D96Parser.ARRAYTYPE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 468
                self.arraynested()
                pass
            elif token in [D96Parser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 469
                self.match(D96Parser.STRINGTYPE)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 470
                self.match(D96Parser.ID)
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


    class ArraynestedContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAYTYPE(self):
            return self.getToken(D96Parser.ARRAYTYPE, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def arraynested(self):
            return self.getTypedRuleContext(D96Parser.ArraynestedContext,0)


        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def BOOLEANTYPE(self):
            return self.getToken(D96Parser.BOOLEANTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(D96Parser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(D96Parser.STRINGTYPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arraynested




    def arraynested(self):

        localctx = D96Parser.ArraynestedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_arraynested)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(D96Parser.ARRAYTYPE)
            self.state = 474
            self.match(D96Parser.LSB)
            self.state = 480
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAYTYPE]:
                self.state = 475
                self.arraynested()
                pass
            elif token in [D96Parser.INTTYPE]:
                self.state = 476
                self.match(D96Parser.INTTYPE)
                pass
            elif token in [D96Parser.BOOLEANTYPE]:
                self.state = 477
                self.match(D96Parser.BOOLEANTYPE)
                pass
            elif token in [D96Parser.FLOATTYPE]:
                self.state = 478
                self.match(D96Parser.FLOATTYPE)
                pass
            elif token in [D96Parser.STRINGTYPE]:
                self.state = 479
                self.match(D96Parser.STRINGTYPE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 482
            self.match(D96Parser.COMMA)
            self.state = 483
            if not self._input.LT(1).text not in ["0", "00", "0x0", "0b0", "0X0", "0B0"]:
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self._input.LT(1).text not in [\"0\", \"00\", \"0x0\", \"0b0\", \"0X0\", \"0B0\"]")
            self.state = 484
            self.match(D96Parser.INT)
            self.state = 485
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiarrayindexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAYTYPE(self):
            return self.getToken(D96Parser.ARRAYTYPE, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def indexlist(self):
            return self.getTypedRuleContext(D96Parser.IndexlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_multiarrayindex




    def multiarrayindex(self):

        localctx = D96Parser.MultiarrayindexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_multiarrayindex)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(D96Parser.ARRAYTYPE)
            self.state = 488
            self.match(D96Parser.LB)
            self.state = 490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ARRAYTYPE:
                self.state = 489
                self.indexlist()


            self.state = 492
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayindexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAYTYPE(self):
            return self.getToken(D96Parser.ARRAYTYPE, 0)

        def paramexp(self):
            return self.getTypedRuleContext(D96Parser.ParamexpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arrayindex




    def arrayindex(self):

        localctx = D96Parser.ArrayindexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_arrayindex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(D96Parser.ARRAYTYPE)
            self.state = 495
            self.paramexp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayindex(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ArrayindexContext)
            else:
                return self.getTypedRuleContext(D96Parser.ArrayindexContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_indexlist




    def indexlist(self):

        localctx = D96Parser.IndexlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_indexlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.arrayindex()
            self.state = 502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 498
                self.match(D96Parser.COMMA)
                self.state = 499
                self.arrayindex()
                self.state = 504
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def booln(self):
            return self.getTypedRuleContext(D96Parser.BoolnContext,0)


        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def arrayindex(self):
            return self.getTypedRuleContext(D96Parser.ArrayindexContext,0)


        def multiarrayindex(self):
            return self.getTypedRuleContext(D96Parser.MultiarrayindexContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_value




    def value(self):

        localctx = D96Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_value)
        try:
            self.state = 511
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.match(D96Parser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 506
                self.match(D96Parser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 507
                self.booln()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 508
                self.match(D96Parser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 509
                self.arrayindex()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 510
                self.multiarrayindex()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUETYPE(self):
            return self.getToken(D96Parser.TRUETYPE, 0)

        def FALSETYPE(self):
            return self.getToken(D96Parser.FALSETYPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_booln




    def booln(self):

        localctx = D96Parser.BoolnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_booln)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            _la = self._input.LA(1)
            if not(_la==D96Parser.TRUETYPE or _la==D96Parser.FALSETYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.exp2_sempred
        self._predicates[15] = self.exp3_sempred
        self._predicates[16] = self.exp4_sempred
        self._predicates[19] = self.exp7_sempred
        self._predicates[20] = self.exp8_sempred
        self._predicates[33] = self.attr_sempred
        self._predicates[35] = self.vardecl_sempred
        self._predicates[38] = self.arraynested_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def attr_sempred(self, localctx:AttrContext, predIndex:int):
            if predIndex == 5:
                return getInvokingContext(33).lst[2] < getInvokingContext(33).lst[0]
         

            if predIndex == 6:
                return getInvokingContext(33).lst[0] == getInvokingContext(33).lst[2] and getInvokingContext(33).lst[1] == 1
         

            if predIndex == 7:
                return getInvokingContext(33).lst[1] == 0
         

    def vardecl_sempred(self, localctx:VardeclContext, predIndex:int):
            if predIndex == 8:
                return getInvokingContext(35).lst[2] < getInvokingContext(35).lst[0]
         

            if predIndex == 9:
                return getInvokingContext(35).lst[0] == getInvokingContext(35).lst[2] and getInvokingContext(35).lst[1] == 1
         

            if predIndex == 10:
                return getInvokingContext(35).lst[1] == 0
         

    def arraynested_sempred(self, localctx:ArraynestedContext, predIndex:int):
            if predIndex == 11:
                return self._input.LT(1).text not in ["0", "00", "0x0", "0b0", "0X0", "0B0"]
         




