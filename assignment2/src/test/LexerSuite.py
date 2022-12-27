import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_1(self):
        self.assertTrue(TestLexer.test("000112 0x22_32_12 0b0012_234 0156593", "00,0112,0x223212,0b0,012234,01565,93,<EOF>", 1))
    def test_2(self):
        self.assertTrue(TestLexer.test("1_23_23 0x0_112 0b_56367 0_1234 00_679486 ", "12323,0x0,_112,0,b_56367,0,_1234,00,_679486,<EOF>", 2))
    def test_3(self):
        self.assertTrue(TestLexer.test("0.00975 01_43.0112 0123.56367 1234.e4 .56e-10", "0.00975,0143,.,0112,0123,.,56367,1234.e4,.56e-10,<EOF>", 3))
    def test_4(self):
        self.assertTrue(TestLexer.test("1. 0.0000e4 123_345.e0000 5.6646e-0001 0.0000 4e-10", "1.,0.0000e4,123345.e0000,5.6646e-0001,0.0000,4e-10,<EOF>", 4))
    def test_5(self):
        self.assertTrue(TestLexer.test(".2 .0003e0001 1_2_3.e 0.e+123 12_3. 000x0000 0b001020200", ".,2,.0003e0001,123.,e,0.e+123,123.,00,0x0,00,0,0b0,01020200,<EOF>", 5))
    def test_6(self):
        self.assertTrue(TestLexer.test("0b_1234_3444 000_111_2222 123.e+01 0x12_22_34 .12334e2111", "0,b_1234_3444,00,0,_111_2222,123.e+01,0x122234,.12334e2111,<EOF>", 6))
    def test_7(self):
        self.assertTrue(TestLexer.test(""" "abc \\nuabc" """, "abc \\nuabc,<EOF>", 7))
    def test_8(self):
        self.assertTrue(TestLexer.test(""" "123\' \'\"dhf" """, """123' '"dhf,<EOF>""", 8))
    def test_9(self):
        self.assertTrue(TestLexer.test(""" "\' abcdfe\\n \\\\" """, "' abcdfe\\n \\\\,<EOF>", 9))
    def test_10(self):
        self.assertTrue(TestLexer.test(""" " \\b\\r\\n\'\" xy_123" """, " \\b\\r\\n\'\" xy_123,<EOF>", 10))
    def test_11(self):
        self.assertTrue(TestLexer.test(""" " xyz____\\h" """, "Illegal Escape In String:  xyz____\h", 11))
    def test_12(self):
        self.assertTrue(TestLexer.test(""" "xyz \'\"  """, """Unclosed String: xyz '"  """, 12))
    def test_13(self):
        self.assertTrue(TestLexer.test(""" " \\r\\\"\\\\" """, "Illegal Escape In String:  \\r\\\"", 13))
    def test_14(self):
        self.assertTrue(TestLexer.test(""" " \\\n\\'\\"abc " """, "Illegal Escape In String:  \\\n", 14))
    def test_15(self):
        self.assertTrue(TestLexer.test(""" " abc \\q\\\ " """, """Illegal Escape In String:  abc \q""", 15))
    def test_16(self):
        self.assertTrue(TestLexer.test(""" " 123abc ///\\nrxy  """, "Unclosed String:  123abc ///\\nrxy  ", 16))
    def test_17(self):
        self.assertTrue(TestLexer.test(""" " abc\n\r\f " """, "Unclosed String:  abc", 17))
    def test_18(self):
        self.assertTrue(TestLexer.test(""" " ghi\\\m\' " """, " ghi\\\m' ,<EOF>", 18))
    def test_19(self):
        self.assertTrue(TestLexer.test(""" " hello's \'\"\"\" " """, """ hello's '", ,<EOF>""", 19))
    def test_20(self):
        self.assertTrue(TestLexer.test(""" " abc \\n string  """, "Unclosed String:  abc \\n string  ", 20))
    def test_21(self):
        self.assertTrue(TestLexer.test(" +-*/ >=<= == = < > ", "+,-,*,/,>=,<=,==,=,<,>,<EOF>", 21))
    def test_22(self):
        self.assertTrue(TestLexer.test(" ++// >= <= :: != ! .,abc ", "+,+,/,/,>=,<=,::,!=,!,.,,,abc,<EOF>", 22))
    def test_23(self):
        self.assertTrue(TestLexer.test(" {) }( {()} [[]]; (::) ", "{,),},(,{,(,),},[,[,],],;,(,::,),<EOF>", 23))
    def test_24(self):
        self.assertTrue(TestLexer.test("5/2+3*3 - (4+5)*9/5/5", "5,/,2,+,3,*,3,-,(,4,+,5,),*,9,/,5,/,5,<EOF>", 24))
    def test_25(self):
        self.assertTrue(TestLexer.test("1 == 5 && (3-5)*4 <= 5", "1,==,5,&&,(,3,-,5,),*,4,<=,5,<EOF>", 25))
    def test_26(self):
        self.assertTrue(TestLexer.test("___abc$xdfr 123_wwer__345", "___abc,$xdfr,123,_wwer__345,<EOF>", 26))
    def test_27(self):
        self.assertTrue(TestLexer.test("$w$______abc0000111122 $xxxAAA", "$w,$______abc0000111122,$xxxAAA,<EOF>", 27))
    def test_28(self):
        self.assertTrue(TestLexer.test("abc !=_1334_34654 $", "abc,!=,_1334_34654,Error Token $", 28))
    def test_29(self):
        self.assertTrue(TestLexer.test("a!=b==c<=___abc>=u/2-34", "a,!=,b,==,c,<=,___abc,>=,u,/,2,-,34,<EOF>", 29))
    def test_30(self):
        self.assertTrue(TestLexer.test("x*y*z%%123.454e16", "x,*,y,*,z,%,%,123.454e16,<EOF>", 30))
    def test_31(self):
        self.assertTrue(TestLexer.test("## this is a comment ##", "<EOF>", 31))
    def test_32(self):
        self.assertTrue(TestLexer.test("## comment in program ## abc ##", "abc,Error Token #", 32))
    def test_33(self):
        self.assertTrue(TestLexer.test("#### comment abc ##", "comment,abc,Error Token #", 33))
    def test_34(self):
        self.assertTrue(TestLexer.test("Var x, y, x: Int;", "Var,x,,,y,,,x,:,Int,;,<EOF>", 34))
    def test_35(self):
        self.assertTrue(TestLexer.test(""" Var $x, y, z: Array[Int, 5];""", "Var,$x,,,y,,,z,:,Array,[,Int,,,5,],;,<EOF>", 35))
    def test_36(self):
        self.assertTrue(TestLexer.test("method(x: Int, y: Array) { }", "method,(,x,:,Int,,,y,:,Array,),{,},<EOF>", 36))
    def test_37(self):
        self.assertTrue(TestLexer.test("""
        Class Program {
            methodA(A: Int) {
                return A*2;
            }
            Var x: Int;
        } """, "Class,Program,{,methodA,(,A,:,Int,),{,return,A,*,2,;,},Var,x,:,Int,;,},<EOF>", 37))
    def test_38(self):
        self.assertTrue(TestLexer.test("main() { Val $xyz: Bool = True;}", "main,(,),{,Val,$xyz,:,Bool,=,True,;,},<EOF>", 38))
    def test_39(self):
        self.assertTrue(TestLexer.test("""
        method(x); 
        A.shape(a,b,c);
        x = x+ 1;
        """, "method,(,x,),;,A,.,shape,(,a,,,b,,,c,),;,x,=,x,+,1,;,<EOF>", 39))
    def test_40(self):
        self.assertTrue(TestLexer.test("""
        Var x: Int = 5;
        If (x > 5 && x<= 9) {
            x = x*2;
        }
        """, "Var,x,:,Int,=,5,;,If,(,x,>,5,&&,x,<=,9,),{,x,=,x,*,2,;,},<EOF>", 40))
    def test_41(self):
        self.assertTrue(TestLexer.test(""" If(True) {
            Return False;
        } """, "If,(,True,),{,Return,False,;,},<EOF>", 41))
    def test_42(self):
        self.assertTrue(TestLexer.test("""
        Var a: Shape = New Shape();
        Continue;
        """, "Var,a,:,Shape,=,New,Shape,(,),;,Continue,;,<EOF>", 42))
    def test_43(self):
        self.assertTrue(TestLexer.test("""
        If ($xyz > 0) { }
        Elseif (y < 0) {
            Return y;
        }
        """, "If,(,$xyz,>,0,),{,},Elseif,(,y,<,0,),{,Return,y,;,},<EOF>", 43))
    def test_44(self):
        self.assertTrue(TestLexer.test("""
        Class $xyz: Shape { }
        """, "Class,$xyz,:,Shape,{,},<EOF>", 44))
    def test_45(self):
        self.assertTrue(TestLexer.test("""
        Class ABC {
            $add(a: Int, b: Boolean) {
                a = a + 2;
            }
        }
        """, "Class,ABC,{,$add,(,a,:,Int,,,b,:,Boolean,),{,a,=,a,+,2,;,},},<EOF>", 45))
    def test_46(self):
        self.assertTrue(TestLexer.test("""
        Var X: Shape;
        X::$getShape(a);
        """, "Var,X,:,Shape,;,X,::,$getShape,(,a,),;,<EOF>", 46))
    def test_47(self):
        self.assertTrue(TestLexer.test("Continue;Break,If, Elseif,Self.$xyz", "Continue,;,Break,,,If,,,Elseif,,,Self,.,$xyz,<EOF>", 47))
    def test_48(self):
        self.assertTrue(TestLexer.test("Foreach..Continue;{ } A[[2]]", "Foreach,..,Continue,;,{,},A,[,[,2,],],<EOF>", 48))
    def test_49(self):
        self.assertTrue(TestLexer.test("""
        Array(1, 5, 7, 12) || 
        Array("Kangxi", "Yongzheng", "Qianlong")
        """, "Array,(,1,,,5,,,7,,,12,),||,Array,(,Kangxi,,,Yongzheng,,,Qianlong,),<EOF>", 49))
    def test_50(self):
        self.assertTrue(TestLexer.test("""
        a = "abc" +. "xyz";
        a = a ==. "qqw";
         """, "a,=,abc,+.,xyz,;,a,=,a,==.,qqw,;,<EOF>", 50))
    def test_51(self):
        self.assertTrue(TestLexer.test("""
        Array (
        Array("Volvo", "22", "18"),
        Array("Saab", "5", "2"),
        Array("Land Rover", "17", "15")
        )
        """, "Array,(,Array,(,Volvo,,,22,,,18,),,,Array,(,Saab,,,5,,,2,),,,Array,(,Land Rover,,,17,,,15,),),<EOF>", 51))
    def test_52(self):
        self.assertTrue(TestLexer.test(""" $x = $a + r;
        Return $x; 
        $x = $x / A[1][2][3];
        """, "$x,=,$a,+,r,;,Return,$x,;,$x,=,$x,/,A,[,1,],[,2,],[,3,],;,<EOF>", 52))
    def test_53(self):
        self.assertTrue(TestLexer.test("""
        Foreach (x In 5 .. 2) {
            Out.printInt(arr[x]);
        }
        """, "Foreach,(,x,In,5,..,2,),{,Out,.,printInt,(,arr,[,x,],),;,},<EOF>", 53))
    def test_54(self):
        self.assertTrue(TestLexer.test("""
        Foreach ($u In 0x22 .. 0x55) {
            insertValue($u);
            If($u == 2) {
                Return;
            }
        }
        """, "Foreach,(,$u,In,0x22,..,0x55,),{,insertValue,(,$u,),;,If,(,$u,==,2,),{,Return,;,},},<EOF>", 54))
    def test_55(self):
        self.assertTrue(TestLexer.test("""
        Foreach (__ In 0b000 .. 00123) {
            PrintX();
        }
        """, "Foreach,(,__,In,0b0,00,..,00,123,),{,PrintX,(,),;,},<EOF>", 55))
    def test_56(self):
        self.assertTrue(TestLexer.test("Int Float x == 4, Boolean String = -+", "Int,Float,x,==,4,,,Boolean,String,=,-,+,<EOF>", 56))
    def test_57(self):
        self.assertTrue(TestLexer.test("""
        Val x: Int = 5;
        x += "abc\\n";
        """, "Val,x,:,Int,=,5,;,x,+,=,abc\\n,;,<EOF>", 57))
    def test_58(self):
        self.assertTrue(TestLexer.test(""" "abc" + "\\r" /2 -!!! """, "abc,+,\\r,/,2,-,!,!,!,<EOF>", 58))
    def test_59(self):
        self.assertTrue(TestLexer.test("abc.getValue(); Return this;## $$##", "abc,.,getValue,(,),;,Return,this,;,<EOF>", 59))
    def test_60(self):
        self.assertTrue(TestLexer.test("X::Shape abc$x$x $", "X,::,Shape,abc,$x,$x,Error Token $", 60))
    def test_61(self):
        self.assertTrue(TestLexer.test("X = -1 + x.shape(a);", "X,=,-,1,+,x,.,shape,(,a,),;,<EOF>", 61))
    def test_62(self):
        self.assertTrue(TestLexer.test("""
        A = A/2*3*b[4][5] - Z.get(a, b, $x - 2);
        """, "A,=,A,/,2,*,3,*,b,[,4,],[,5,],-,Z,.,get,(,a,,,b,,,$x,-,2,),;,<EOF>", 62))
    def test_63(self):
        self.assertTrue(TestLexer.test(" abc\'\\m\\h\" ", "abc,Error Token '", 63))
    def test_64(self):
        self.assertTrue(TestLexer.test("123E-10+e-120 .0e+1+2 -abc!", "123E-10,+,e,-,120,.0e+1,+,2,-,abc,!,<EOF>", 64))
    def test_65(self):
        self.assertTrue(TestLexer.test(" $_123E-10 !&&a__&&$_x (%))", "$_123E,-,10,!,&&,a__,&&,$_x,(,%,),),<EOF>", 65))
    def test_66(self):
        self.assertTrue(TestLexer.test(""" " _abc \\\\'\'\" '\" " """, """ _abc \\\\''" '" ,<EOF>""", 66))
    def test_67(self):
        self.assertTrue(TestLexer.test(""" "abc\\r\\n\'\" """, """Unclosed String: abc\\r\\n'" """, 67))
    def test_68(self):
        self.assertTrue(TestLexer.test(" $xxxx____- $ ", "$xxxx____,-,Error Token $", 68))
    def test_69(self):
        self.assertTrue(TestLexer.test(""" " !!@##$%&*()))\\\\t dfh " """, " !!@##$%&*()))\\\\t dfh ,<EOF>", 69))
    def test_70(self):
        self.assertTrue(TestLexer.test(""" " *$$$$~~~---+=== ){}{}\'\"" """, """ *$$$$~~~---+=== ){}{}'",<EOF>""", 70))
    def test_71(self):
        self.assertTrue(TestLexer.test(""" 
        X = -1 + 10.e-2 % 10;
        Var x: Int = c;
        """, "X,=,-,1,+,10.e-2,%,10,;,Var,x,:,Int,=,c,;,<EOF>", 71))
    def test_72(self):
        self.assertTrue(TestLexer.test("""
        ## Comment in this class ## 
        main() {
            Return Self.get();
        }
        """, "main,(,),{,Return,Self,.,get,(,),;,},<EOF>", 72))
    def test_73(self):
        self.assertTrue(TestLexer.test("({_ 10+e10e-10 .210x00021 (}*$", "(,{,_,10,+,e10e,-,10,.,210,x00021,(,},*,Error Token $", 73))
    def test_74(self):
        self.assertTrue(TestLexer.test("$xyz $_1234$11 {&&!!~~", "$xyz,$_1234,$11,{,&&,!,!,Error Token ~", 74))
    def test_75(self):
        self.assertTrue(TestLexer.test(""" " \t\r\n\\t\\\' \\'\" """, "Unclosed String:  ", 75))
    def test_76(self):
        self.assertTrue(TestLexer.test("where are you??? !~ '\" ", "where,are,you,Error Token ?", 76))
    def test_77(self):
        self.assertTrue(TestLexer.test("""
        a = 1 && 2 && 3 && 0;
        a = True || False;
        """, "a,=,1,&&,2,&&,3,&&,0,;,a,=,True,||,False,;,<EOF>", 77))
    def test_78(self):
        self.assertTrue(TestLexer.test(""" 
        " xyz? == a && b && c * 12 @@ \"
         """, " xyz? == a && b && c * 12 @@ ,<EOF>", 78))
    def test_79(self):
        self.assertTrue(TestLexer.test("<>==+= /*+-__abc -xyz <=>= []", "<,>=,=,+,=,/,*,+,-,__abc,-,xyz,<=,>=,[,],<EOF>", 79))
    def test_80(self):
        self.assertTrue(TestLexer.test(""" " \\'\\\" tyz \[} " """, "Illegal Escape In String:  \\'\\\"", 80))
    def test_81(self):
        self.assertTrue(TestLexer.test(""" class Name {
            Self.x = New A(a, x == 5);
            Break;
        } """, "class,Name,{,Self,.,x,=,New,A,(,a,,,x,==,5,),;,Break,;,},<EOF>", 81))
    def test_82(self):
        self.assertTrue(TestLexer.test("Var x: Array[Array[Int, 5], 10];", "Var,x,:,Array,[,Array,[,Int,,,5,],,,10,],;,<EOF>", 82))
    def test_83(self):
        self.assertTrue(TestLexer.test("Self.x + Self.y <= Self.z -= 2", "Self,.,x,+,Self,.,y,<=,Self,.,z,-,=,2,<EOF>", 83))
    def test_84(self):
        self.assertTrue(TestLexer.test("Foreach () ..{ Return If Stmt == True", "Foreach,(,),..,{,Return,If,Stmt,==,True,<EOF>", 84))
    def test_85(self):
        self.assertTrue(TestLexer.test("""
        If(a >b -c) {
            Break;
        }
        Elseif() {
           Continue $x;
        }
        """, "If,(,a,>,b,-,c,),{,Break,;,},Elseif,(,),{,Continue,$x,;,},<EOF>", 85))
    def test_86(self):
        self.assertTrue(TestLexer.test("$_.e++123_456 Continue Int: x; 0x010101 =+..10", "$_,.,e,+,+,123456,Continue,Int,:,x,;,0x0,10101,=,+.,.,10,<EOF>", 86))
    def test_87(self):
        self.assertTrue(TestLexer.test(""" " && ## this is comment ## " """, " && ## this is comment ## ,<EOF>", 87))
    def test_88(self):
        self.assertTrue(TestLexer.test(""" ## " string in comment " ## ## """, "Error Token #", 88))
    def test_89(self):
        self.assertTrue(TestLexer.test(""" " //;:%!! ``&& $$  """, "Unclosed String:  //;:%!! ``&& $$  ", 89))
    def test_90(self):
        self.assertTrue(TestLexer.test("If Self::$getValue() Return { Array[Int] }", "If,Self,::,$getValue,(,),Return,{,Array,[,Int,],},<EOF>", 90))   
    def test_91(self):
        self.assertTrue(TestLexer.test("Var x, y, $xyz: Int = $; ", "Var,x,,,y,,,$xyz,:,Int,=,Error Token $", 91))
    def test_92(self):
        self.assertTrue(TestLexer.test("declare Class(a, b, c: Int; y,z: Array[Int,5]);", "declare,Class,(,a,,,b,,,c,:,Int,;,y,,,z,:,Array,[,Int,,,5,],),;,<EOF>", 92))
    def test_93(self):
        self.assertTrue(TestLexer.test("""
        class main() {
            main() {
                f = g compose g;
            }
        }
        """, "class,main,(,),{,main,(,),{,f,=,g,compose,g,;,},},<EOF>", 93))
    def test_94(self):
        self.assertTrue(TestLexer.test("A[$abc][$123] + x - 00001*.e_3424", "A,[,$abc,],[,$123,],+,x,-,00,00,1,*,.,e_3424,<EOF>", 94))
    def test_95(self):
        self.assertTrue(TestLexer.test("Return:Continue, break x;Foreach method..() []", "Return,:,Continue,,,break,x,;,Foreach,method,..,(,),[,],<EOF>", 95))
    def test_96(self):
        self.assertTrue(TestLexer.test(""" "!%## __a \\t^^$"+String: a;""", "!%## __a \\t^^$,+,String,:,a,;,<EOF>", 96))
    def test_97(self):
        self.assertTrue(TestLexer.test("$x(4+5)/2/2-3-5+6.e+56", "$x,(,4,+,5,),/,2,/,2,-,3,-,5,+,6.e+56,<EOF>", 97))
    def test_98(self):
        self.assertTrue(TestLexer.test("Int,Float,StringBoolean, TrueFalse$", "Int,,,Float,,,StringBoolean,,,TrueFalse,Error Token $", 98))
    def test_99(self):
        self.assertTrue(TestLexer.test(""" Array().New().method{getString() +. Return String() """, "Array,(,),.,New,(,),.,method,{,getString,(,),+.,Return,String,(,),<EOF>", 99))
    def test_100(self):
        self.assertTrue(TestLexer.test("X::$shape::a.oneString('getNew')", "X,::,$shape,::,a,.,oneString,(,Error Token '", 100))