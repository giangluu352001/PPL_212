import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_223_missing_colon(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                Var length, width: Int;
                getNumOfShape() {
                    Foreach (i In (1 + 2) .. (3+5) By 2) {
                        System.out.println(23);
                        If (i == 3) { } 
                        Elseif(i != 1) {
                            a = 1 + 2 - 5;
                            b = "abc" +. "1312";
                        }
                        Else { 
                            Return;
                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_101(self):
        self.assertTrue(TestParser.test("""Class Program {
            main() {
                Var w, s: Int;
                r = 2.0;
                Var a, b: Array[Array[Int,10], 5];
                If(r >= 1234.0123) {
                    r = r + 124;
                }
                Elseif(r == 134) {
                    a[0][1] = 555;
                } Else {
                    a[2][3] = a[4][5] + a[6][7]; 
                }
                Shape::$getName().X();
                Out.out.get.printInt().getName();
                System.println(a,b).foo(x).foo(a).X.get.getX(a).getName();
                Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Var $x, $y : Int = 0, 0;
                Foreach (x In 144 .. 66) {
                    Out.printInt(arr[x]);
                }
                A[3][4] = 1;
                Shape.x.y = 5;
                Return a;
            }
        }""","Error on line 18 col 20: $x",101))
    def test_102(self):
        self.assertTrue(TestParser.test("""
    Class Shape {
        $getNumOfShape() {
            Return Self.length * Self.width;
        }
        Var a: Array[Int, 5];
        main() {
            x = Array (
                Array(
                    Array("Volvo", "22", "18"),
                    Array("Saab", "5", "2"),
                    Array("Land Rover", "17", "15")
                ),
                Array(
                    Array("Volvo", "22", "18", "22"),
                    Array("Saab", "5", "2", "hehe"),
                    Array("Land Rover", "17", "15")
                )
            )[1][2][3] + A[5][5];
        }
    }
    ""","successful",102))
    def test_103(self):
        self.assertTrue(TestParser.test(""" 
        Class key {
            Val My1stCons, My2ndCons: Int = New X(a, b).Y(), 4;
        }""", "successful", 103))
    def test_104(self):
        self.assertTrue(TestParser.test(""" 
        Class X { 
            Var My1stCons, My2ndCons: Int = Shape::$1, X.$1234;
        }""", "Error on line 3 col 57: $1234", 104))
    def test_105(self):
        self.assertTrue(TestParser.test(""" Class test {
            Var My1stCons, My2ndCons: Int;
        }""", "successful", 105))
    def test_106(self):
        self.assertTrue(TestParser.test("""
        Class Name {
            Val My1stCons, a2, a3: Int = (1+1).X(), 2, 3;
        }
        """, "successful", 106)) 
    def test_107(self):
       self.assertTrue(TestParser.test(""" 
        Class X {
           Val a, b: Int = 1, 2, 3;
        }""", "Error on line 3 col 31: ,", 107))  
    def test_108(self):
        self.assertTrue(TestParser.test(""" 
        Class A{
            Constructor() {
                New X().list(a, b);
            }
        }""", "successful", 108))
    def test_109(self):
        self.assertTrue(TestParser.test(""" 
        Class X {
            Var a, $x: Array[Int, 0x000];
            Constructor(a,b,c: Int) {
                a = Shape::$a___q + Array(1,2,3);
            }
        }""", "Error on line 3 col 34: 0x0", 109))
    def test_110(self):
        self.assertTrue(TestParser.test(""" 
        Class X {
            main() {
                Foreach ($i In 1 .. 100 By 2) {
                    Out.printInt($i);
                }
            }
        }""", "Error on line 4 col 25: $i", 110))
    def test_111(self):
        self.assertTrue(TestParser.test("""
        Class Shape {
            Var x: Int;
        }
        Class Program {
            getName(x: Int) {
                Var b: Float = 0.3 + x;
                Var object: Shape = New Shape();
            }
            main() {
                If (a >= b) {
                    Var a: Int = 0;
                    Shape::$getShape()[3+x] = a[c[b[2]]] + 3;
                }
                Elseif (b >= c) {
                    Self.getName(a);
                }
                Elseif (12 >= g) {
                    Self.insert("String");
                }
                Else {
                    Return object;
                }
            }
        }
        """, "successful", 111))
    def test_112(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            $staticmethod(a,b,c: Int; x,y,z: Array[Int,5]) {
                Return Shape::getName();
            }
        }""", "Error on line 4 col 30: getName", 112))
    def test_113(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            Var $atrr : Int;
            $staticmethod(a,b,c: Int; x,y,z: Array[Int,5]) {
                Single::$atrr = a + b + Shape::$getName();
            }
        }""", "successful", 113))
    def test_114(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            staticmethod() {
                Var $x, $y: Int;
                Return $x + $y;
            }
        }""", "Error on line 4 col 20: $x", 114))
    def test_115(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            $Constructor(a: Int) {
                Return;
            }
        }""", "successful", 115))
    def test_116(self):
        self.assertTrue(TestParser.test("""
        Class Constructor {
            Val x: String = "abc" + "cdf";
        }""", "Error on line 2 col 14: Constructor", 116))
    def test_117(self):
        self.assertTrue(TestParser.test("""
        Class Tail {
            Destructor() {
                Var x: String = "a\\t" + Self.str(Shape::$getName());
            }
        }""", "successful", 117))
    def test_118(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            $getName {
                Return "This is a string";
            }
        }
        Class Program {
            main() {
                Out.print(Single::$getName());
            }
        }""", "Error on line 3 col 21: {", 118))
    def test_119(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            Var a,b,c: Int= 1, 2, 3;
            main() {
                If (a + b >= c) {
                    Return a;
                }
                Else {
                    Return b + 2*c;
                }
            }
        }""", "successful", 119))
    def test_120(self):
        self.assertTrue(TestParser.test("""
        Class Single: Shape {
            $staticmethod() {
                Foreach (X.getChar().X.Y In 10 .. 100) {
                    Shape::$x = X.foo() + New Shape().X(a,b);
                }
            }
        }""", "successful", 120))
    def test_121(self):
        self.assertTrue(TestParser.test("""
        Class Double {
            method(a: Array[Int, 5]) {
                If(a) {
                    Return a;
                }
                Elseif (Self.size(a) < 5) {
                    a = Array(1,2,3,4,5);
                    Break;
                }
            }
        }""", "successful", 121))
    def test_122(self):
        self.assertTrue(TestParser.test("""
        Class Double {
            Constructor() {
                Var x: Array[String, 5];
            }
            main() {
                If(Self.x[0] == "This") {
                    x = Array("This", "is", "a", "string", "!");
                }
            }
        }""", "successful", 122))
    def test_123(self):
        self.assertTrue(TestParser.test("""
        Class Double {
            $staticmethod(a,$b,c: Int) {
                Return $b;
            }
        }""", "Error on line 3 col 28: $b", 123))
    def test_124(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            Var x: Array[Array[String, 5], 5];
            main() {
                x = x[a + 3 == 1] + x[c[b[5]]];
            }
        }""", "successful", 124))
    def test_125(self):
        self.assertTrue(TestParser.test("""
        Class A {
            main() {
                Foreach ($_ in 0x00 .. 0x55) {
                    Out.convert($_);
                }
            }
        }""", "Error on line 4 col 25: $_", 125))
    def test_126(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            Val x, $y: String = "a", "yz";
            Continue x;
        }""", "Error on line 4 col 12: Continue", 126))
    def test_127(self):
        self.assertTrue(TestParser.test("""
        Class Single {
        }
        Class X: Single {
            main() { }
        }""", "successful", 127))
    def test_128(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            A(a: Int) {
                Return a;
            }
            B(b:String) {
                If(b +. "String" == "abcString") {
                    Break;
                }
            }
        }""", "successful", 128))
    def test_129(self):
        self.assertTrue(TestParser.test("""Class $x { }""", "Error on line 1 col 6: $x", 129))
    def test_130(self):
        self.assertTrue(TestParser.test(""" Class X: Y, Z { }""", "Error on line 1 col 11: ,", 130))
    def test_131(self):
        self.assertTrue(TestParser.test("""
        Class One {
            Main() {
                Var a, b: Int;
                a = b + 1.00e-0004 * 0x200;
            }
        }""", "successful", 131))
    def test_132(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            $static() {
                Self.x = Self.y + Shape::$X().Y();
            }
        }""", "successful", 132))
    def test_133(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            Destructor(a, b, c: Int) {
            }
        }""", "Error on line 3 col 23: a", 133))
    def test_134(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            $static() {
                Self.x = (1+2).y() + New X(a,b).Y(Shape::$x);
            }
        }""", "successful", 134))
    def test_135(self):
        self.assertTrue(TestParser.test("""
        Class Double {
            Class Name {
                Val a: Int = 1, 2;
            }
        }""", "Error on line 3 col 12: Class", 135))
    def test_136(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            $static() {
                Var r: Float;
                r = 123_34.e-10;
                r = r*s*Self.x;
                a[0][0] = r + Self.y;
            }
        }""", "successful", 136))
    def test_137(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            $static() {
                main() {
                    Return Self::$x;
                }
            }
        }""", "Error on line 4 col 20: (", 137))
    def test_138(self):
        self.assertTrue(TestParser.test("""
        Class Single {
            get(a: String) {
                If(Self.compare(a, "String") == 0) {
                    Continue;
                }
                Else {
                    Return A::$x + A::$y;
                }
            }
        }""", "successful", 138))
    def test_139(self):
        self.assertTrue(TestParser.test("""
        Class A {
            $static() {
                Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(arr[i][i+2*i - 2]);
                }
            }
        }""", "successful", 139))
    def test_140(self):
        self.assertTrue(TestParser.test("""
        Class A {
            Val $x, $y: Int = 1 + _.foo(1,4), 0;
            method() {
               Val x: String = "a\\\\";
               Return x + Self.str(S::$x) + Self.str(S::$y); 
            }
        }""", "successful", 140))
    def test_141(self):
        self.assertTrue(TestParser.test("""
        Class A {
            $static() {
                X.foo(A.value);
            }
        }""", "successful", 141))
    def test_142(self):
        self.assertTrue(TestParser.test("""
        Class A {
            $name() {
                Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(i);
                
            }
        }""", "Error on line 8 col 9: <EOF>", 142))
    def test_143(self):
        self.assertTrue(TestParser.test("""
        Class A {
            static(a: Int, b: String) {
            }
        }""", "Error on line 3 col 25: ,", 143))
    def test_144(self):
        self.assertTrue(TestParser.test("""
        Class A {
            Float() {
                Break;
            }
        }""", "Error on line 3 col 12: Float", 144))
    def test_145(self):
        self.assertTrue(TestParser.test("""
        Class A {
            Val x: Array[Int, 2] = Array(1,2);
            method(a: Int) {
                If(Self.x[a + 2] <= 100) {
                    Self.x = Self.get()[(a+2)*5];
            }
        }""", "Error on line 8 col 9: <EOF>", 145))
    def test_146(self):
        self.assertTrue(TestParser.test("""
        Class A {
            Constructor() {}
            Constructor() {}
            Destructor() {}
            Destructor() {}
        }""", "successful", 146))
    def test_147(self):
        self.assertTrue(TestParser.test("""
        Class A {
            Constructor() {
                Self.x[(Self.y[x+3]).getFoo()] = 1 + 4;
            }
            Destructor() { 
                Return False;
            }
        }""", "successful", 147))
    def test_148(self):
        self.assertTrue(TestParser.test("""
        Class A {
            Constructor() {
                Return Self + Self;
            }
            Destructor(a: Int) { }
        }""", "Error on line 6 col 23: a", 148))
    def test_149(self):
        self.assertTrue(TestParser.test("""
        Class X {
            main(foo: Array[Array[String, 5], 2]) {
                If(foo[0][2] == 1 + 3) {
                    Return foo[x+ Self.y];
                }
                Elseif(!foo) {
                    foo[0][1] = -45.e-10;
                } 
            }
        }""", "successful", 149))
    def test_150(self):
        self.assertTrue(TestParser.test("""
        Class A {
            Val x: Int = 1;
            Var $y, u: String = Self.str(1) + "abc", Self.str(x);
        }""", "successful", 150))
    def test_151(self):
        self.assertTrue(TestParser.test("""
        Class A {
            Val x,y,z: Float;
            x = x + 2;
        }""", "Error on line 4 col 14: =", 151))
    def test_152(self):
        self.assertTrue(TestParser.test("""
        Class Name {
            Constructor(A: Int; B: String) {
                Self.x = New X(A,B);
                Return Self.x;
            }
        }""", "successful", 152))
    def test_153(self):
        self.assertTrue(TestParser.test("""
        Class B: A {}
        Class C: B {
            Val arr: Array[String, 2];
            method() {
                Self.arr = Array(1,2,3) + Array(4,5,6);
                Self.arr[0] = "string";
            }
        }""", "successful", 153))
    def test_154(self):
        self.assertTrue(TestParser.test("""
        Class A {
            method() {
                foo = Self.get()[3+x] + Array(1,2,3);
            }
        }""", "successful", 154))
    def test_155(self):
        self.assertTrue(TestParser.test(""" Class A { $x() { Break } } """,
         "Error on line 1 col 24: }", 155))
    def test_156(self):
        self.assertTrue(TestParser.test(""" 
        Class A {
            Var x,y: Int = 1;
        } """, "Error on line 3 col 28: ;", 156))
    def test_157(self):
        self.assertTrue(TestParser.test("""Class A {Var u: Array[Int, 0];}""", "Error on line 1 col 27: 0", 157))
    def test_158(self):
        self.assertTrue(TestParser.test(""" Class Done {method() { Return foo(Self.x); } }""",
         "Error on line 1 col 34: (", 158))
    def test_159(self):
        self.assertTrue(TestParser.test("""
        Class Done {
            Val x: Boolean;
            method() {
                Return (x+1)::$foo();
            }
        }""", "Error on line 5 col 28: ::", 159))
    def test_160(self):
        self.assertTrue(TestParser.test("""
        Class Done {
            setName(a: Boolean) {
                If(a) {
                    Return (x+1).foo(a) + 2;
                }
                Elseif(!a) {
                    Continue;
                }
            }
        }""", "successful", 160))
    def test_161(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Var a: Int = Self.x[1][2].getName();
            }
        }
        """, "Error on line 4 col 41: .", 161))
    def test_162(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Var a: Int = Self.x[1][2][a[x+4]];
                a = a + 1_234.e-1;
                Return a;
            }
        }
        """, "successful", 162))
    def test_163(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Var a: Int = Shape.getName();
                If(!Shape::$get() && !(x+3 == 10) || Self.x != "abc") {
                    Break;
                }
            }
        }
        """, "successful", 163))
    def test_164(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Var a: Int = -1 - 10.e-4;
                Var b: Int = -10.e-10 + -.e-005;
            }
        }
        """, "successful", 164))
    def test_165(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Var a: Int = x % 4 == 0;
                Var b: Int = (x / 4 % 3 == 0) && (x<=3)*10;  
            }
        }
        """, "successful", 165))
    def test_166(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                If((Self.x <= 10.e-10) || (-X.getName().get < 0)) {
                    X = X[A[x+2*i]] % 3;
                }
            }
        }
        """, "successful", 166))
    def test_167(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Var x, $y: Int;
                Return x;
            }
        }
        """, "Error on line 4 col 23: $y", 167))
    def test_168(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            $_(a,b: String) {
                If(a != "String" || ((a-5)*A[x[v.getIndex(a)]] <= 10)) {
                    Continue;
                }
            }
        }
        """, "successful", 168))
    def test_169(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            $_() {
                a = (New X(x)[1][1]).getName();
            }
        }
        """, "successful", 169))
    def test_170(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Var a: Int = New Shape() :: $setName();
            }
        }
        """, "Error on line 4 col 41: ::", 170))
    def test_171(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Val x: Int = New X().Y().Shape;
            }
        }
        """, "successful", 171))
    def test_172(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Var a: Int = (New Shape().getClass()).Shape();
            }
        }
        """, "successful", 172))
    def test_173(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                x = ("abc\\n" +. "xyz\\t").Y()[1];
            }
        }
        """, "successful", 173))
    def test_174(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Var a: Int = (X+3).Y(Array(1,2,3,4));
            }
        }
        """, "successful", 174))
    def test_175(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Var a: Int = New X()::$Shape;
            }
        }
        """, "Error on line 4 col 36: ::", 175))
    def test_176(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Var a: Int = Self::$x + Self::$y;
            }
        }
        """, "Error on line 4 col 33: ::", 176))
    def test_177(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() { }
            getName() {
                Return x == 5 || (!x && x <= x - 3);
            }
        }
        """, "successful", 177))
    def test_178(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                out.println("Hello World");
                x.print();
            }
        }
        """, "successful", 178))
    def test_179(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            Constructor() {
                If(x/2/3 == 0 +. "abc") {
                    Foreach(I In 0b0 .. 0b11) {
                        Break;
                    }
                }
            }
        }
        """, "successful", 179))
    def test_180(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            class(): Program {
                Return x;
            }
        }
        """, "Error on line 3 col 19: :", 180))
    def test_181(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                x = x == 5 && (x+3) +. "abc" || x == a[5] && y ==. "xyz";
            }
        }
        """, "Error on line 4 col 63: ==.", 181))
    def test_182(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Var x: Int = (x+3)*2/2 == 0 && x.get().shape()[A[x]] != 0;
            }
        }
        """, "Error on line 4 col 69: !=", 182))
    def test_183(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Val x: String = !Self.bool && !A[d[x+3]] || Shape::$name() != A.get(i);
            }
        }
        """, "successful", 183))
    def test_184(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Val temp: Boolean = 
                !New X(a,b).getCheck() && New Y().get(!a + b);
            }
        }
        """, "successful", 184))
    def test_185(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Var x: Array[Int, 5] = Array(x+3, !getName.X(), -x-5+3, 1);
            }
        }
        """, "successful", 185))
    def test_186(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                Var x: Array[String, 2] = 
                Array("abc" +. "xyz", x+3 != !(x-5));
            }
        }
        """, "successful", 186))
    def test_187(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                If(Array(1,2,3) == Array(x+3, !A[x[2]])) {
                    Out.println("\\n");
                }
            }
        }
        """, "successful", 187))
    def test_188(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            main() {
                If(Array(Array(1,2,3), Array(4,5,6)) != (Array(1,2,3))) {
                    Break;
                    Out.raise("error");
                }
            }
        }
        """, "successful", 188))
    def test_189(self):
        self.assertTrue(TestParser.test("""
        Class Program {
            Val x: Int = "abc" +. "xyz" ==. "abcxyz" || x == 4 && !x == True;
        }
        """, "Error on line 3 col 40: ==.", 189))
    def test_190(self):
        self.assertTrue(TestParser.test("""
        Class Shape {
            $getName() {
                Return name;
            }
        }
        Class Program {
            main() {
                Var x, y: Shape = New Shape(), Null;
            }
        }
        """, "successful", 190))
    def test_191(self):
        self.assertTrue(TestParser.test("""
        Class A { Val v, $x: Int; }
        Class Shape {
            $getName(a,b: A) {
                A::$x = a.v + b.v;
            }
        }
        """, "successful", 191))
    def test_192(self):
        self.assertTrue(TestParser.test("""
        Class Shape {
            $getName(a,b: Shape; x,y: Rectangle) {
                Return New X() + New Y() - New Z().get();
            }
        }
        """, "successful", 192))
    def test_193(self):
        self.assertTrue(TestParser.test("""
        Class Shape {
            $getName(a: A) {
                A::$x = A::$x == 0 || A::$x != 2;
            }
        }
        """, "Error on line 4 col 44: !=", 193))
    def test_194(self):
        self.assertTrue(TestParser.test("""
        Class Shape {
            Val x, $y: Rectangle = Null, Null;
            main() {
                If(x == Null && (Shape::$y != Null)) {
                    Return x;
            }
        }
        """, "Error on line 9 col 8: <EOF>", 194))
    def test_195(self):
        self.assertTrue(TestParser.test("""
        Class Shape {
            $getName(a,b: A;c: Shape) {
                c::$x = a == -2 - 5 || a +. X.getString != !x; 
            }
        }
        """, "successful", 195))
    def test_196(self):
        self.assertTrue(TestParser.test("""
        Class Shape: X {
            _() {
                If(!x && !(x+3)*2) {
                    (Shape::$x == 1).X=3;
                }
            }
        }
        """, "successful", 196))
    def test_197(self):
        self.assertTrue(TestParser.test("""
        Class Shape {
            Shape::$x = a + b;
        }
        """, "Error on line 3 col 17: ::", 197))
    def test_198(self):
        self.assertTrue(TestParser.test("""
        Class Shape {
            $getName() {
                Out.print();
            }
            Shape.getName();
        }
        """, "Error on line 6 col 17: .", 198))
    def test_199(self):
        self.assertTrue(TestParser.test("""
        Class Shape {
            Val x, y: X ;
            getName() {
                v = x.get() == y.get();
            }
        }
        """, "successful", 199))
    def test_200(self):
        self.assertTrue(TestParser.test("""
        Class Shape {
            $getName() {
                Foreach((x+3).Y() In 100 .. 200) {
                    Return New X((x+3).Y());
                }
            }
        }
        """, "Error on line 4 col 34: In", 200))

    '''def test_204_more_complex_program(self):
        """More complex program"""
        input = """
        Class Shape {
            Val $numOfShape: Int = expr;
            Val immutableAttribute: Int = expr;
            Var length, width: Int;
            $getNumOfShape() {}
        }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,204))
    
    def test_205_more_complex_program(self):
        """More complex program"""
        input = """
        Class Shape {
            Val $numOfShape: Int = expr;
            Val immutableAttribute: Int = expr;
            Var length, width: Int;
            $getNumOfShape() {
                length = expr;
                width = expr;
                Var length, width: Int;
                If (expr) {
                    length = expr;
                }
            }
            
        }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,205))
    
    def test_206_more_complex_program(self):
        """More complex program"""
        input = """
        Class Shape {
            Var length, width: Int;
            $getNumOfShape() {
                length = expr;
                If (expr) {
                    length = expr;
                }
            }
            
        }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,206))
    
    def test_207_more_complex_program(self):
        """More complex program"""
        input = """
        Class Shape {
            Var length, width: Int;
            $getNumOfShape() {
                length = expr;
                If (expr) {
                    length = expr;
                } Elseif (expr) {
                    Var length, width: Int = expr, expr;
                }
            }
            
        }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,207))

    def test_208_more_complex_program(self):
        """More complex program"""
        input = """
        Class Shape {
            Var length, width: Int;
            $getNumOfShape() {
                length = expr;
                If (expr) {
                    length = expr;
                } Elseif (expr) {
                    Var length, width: Int = expr, expr;
                }
            }
            
        }

        Class Vari:Shape {
            Var length, width: Int;
            $getNumOfShape() {
                length = expr;
                If (expr) {
                    length = expr;
                } Else {
                    Var length, width: Int = expr, expr;
                }
            }
            
        }

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,208))
    
    def test_209_more_complex_program(self):
        """More complex program"""
        input = """
        Class Vari:Shape {
            Var length, width: Int;
            $getNumOfShape() {
                length = expr;
                If (expr) {
                    length = expr;
                } Else {
                    Var length, width: Int;
                }
            }
            
        }

        """
        expect = "successfull"
        self.assertTrue(TestAST.test(input,expect,209))
    
    def test_210_more_complex_program(self):
        """More complex program"""
        input = """
        Class Vari:Shape {
            Var length, width: Int;
            getNumOfShape() {
                length = expr;
                If (expr) {
                    length = expr;
                } Else {
                    Var length, width: Int = expr, expr;
                }
                expr[expr] = expr;
            }
            
        }

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,210))
    
    def test_211_more_complex_program(self):
        """More complex program"""
        input = """
        Class Vari:Shape {
            Var length, width: Int;
            getNumOfShape() {
                length = expr;
                If (expr) {
                    expr[expr] = expr;
                } Else {
                    Var length, width: Int = expr, expr;
                }
                expr[expr] = expr;
            }
            
        }

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,211))
    
    def test_212_more_complex_program(self):
        """More complex program"""
        input = """
        Class Vari:Shape {
            Var length, width: Int;
            getNumOfShape() {
                length = expr;
                expr[expr][expr] = expr;
            }
            
        }

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,212))
    
    def test_213_more_complex_program(self):
        """More complex program"""
        input = """
        Class Vari:Shape {
            Var length, width: Int;
            getNumOfShape() {
                length = 1+2/5 + !3;
                a = New B();
                expr[2][3] = 1 + \"sss\" + abc.abc;
                bc::$css();
                Foreach (i In 1 .. 2 By 3) {
                    expr::$getNumOfShape();
                    Break;
                    Return 1 + 2;
                }
            }
            
        }

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,213))
    
    def test_214_more_complex_program(self):
        """More complex program"""
        input = """
        Class Vari:Shape {
            Var length, width: Int;
            getNumOfShape() {
                length = 1+2/5 + !3 -- 2 ;
                a = New B();
                expr[2][3] = 1 + \"sss\" + Self.length + (blue + sky)[1];
                Foreach (i In 1 .. 2 By 3) {
                    expr::$getNumOfShape(2,3);
                    Break;
                    Return 1 + 2;
                    If (x > 4) {
                        Break;
                    } Elseif (x >= 5) {
                        Continue;
                    }
                }
            }
            
        }

        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,214))
    
    def test_218_invoke(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
            Var length, width: Int;
            getNumOfShape() {
                length = 1+2/5 + !3;
                a = New B();
                a.blue = (a::$a(a, 2).c + 2 + (1 + 2));
                a.green();
            }
            
        }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,218))
    
    def test_219_invoke(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
            Var length, width: Int;
            getNumOfShape() {
                length = 1+2/5 + !3;
                a = New B();
                a.blue = a.b((a::$a(a, 2).c + 2 + (1 + 2)));
                a.green();
            }
            
        }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,219))
    
    def test_220_keyword_self(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
            Var length, width: Int;
            getNumOfShape() {
                Self.length = Self.length + 3 - 2/123_13.0;
            }
            
        }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,220))
    
    def test_224_empty_class_members(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
            }
            Class Varia {
                Constructor(a:Int; b:Blue) {

                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,224))
    
    def test_226_static_decl(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                
                $play() {

                }
            }
            Class Varia {
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,226))
    
    def test_227_semantic_error(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                
                $play() {
                    a = 1 + "123";
                }
            }
            Class Varia {
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,227))

    def test_228_main_program(self):
        """More complex program"""
        input = """
            Class Program {
                main() {
                    Out.printInt(Shape::$numOfShape);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,228))
    
    def test_229_ignore_semantic_error(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                
                $play() {
                    Blue::$a();
                    a.constructor().blue();
                    a = "1" + "2" + 3;
                }
            }
            Class Varia {
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,229))

    def test_230_ignore_semantic_error(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                
                Constructor(a:Int; b:Int) {
                    
                }
            }
            Class Varia {
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,230))
    
    def test_231_ignore_semantic_error(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                
                Constructor(a:Int; b:Int) {
                    b = "123" + a.d() + b.d();
                }
            }
            Class Varia {
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,231))
    
    def test_232_ignore_semantic_error(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                
                Constructor(a:Int; b:Int) {
                    b = ("123" + a.d()).close() + b.d();
                }
            }
            Class Varia {
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,232))
    
    def test_233_syntax_error(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                
                Constructor(a:Int; b:Int) {
                    b = ("123" + a.d()).close() + b.d();
                }
            }
            Class Varia {
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,233))
    
    def test_234_empty_param_destructor(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                
                Destructor() {
                    b = ("123" + a.d()).close() + b.d();
                }
            }
            Class Varia {
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,234))
    
    def test_235_empty_param_destructor(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                
                Destructor() {
                    b = ("123" + a.d()).close() + b.d();
                }
            }
            Class Varia {
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,235))
    
    def test_236_invoke_method(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                
                Destructor() {
                    
                    a = a.Blue() + 2;
                    Return X::$numOfShapes;
                }
            }
            Class Varia {
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,236))
    
    def test_239_complex_attr_decl(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                
                Destructor() {
                    
                    Val length, width: int = expr, expr + (1+2) + a.foo();
                }
            }
            Class Varia {
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,239))
    
    def test_240_empty_class_members(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,240))
    
    def test_241_call_static_method(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                Constructor() {
                    a::$foo = 2;
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,241))

    def test_242_call_static_method(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                Constructor() {
                    a::$foo = 2;
                    A = a::$foo() + 3;
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,242))
    
    def test_243_call_static_method(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                Constructor() {
                    a::$foo = 2;
                    a::$foo();
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,243))
    
    def test_244_assign_on_data_return(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                Constructor() {
                    a::$foo = 2;
                    a::$foo().b = 3;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,244))
    
    def test_245_invalid_use_static(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                Constructor(a:Int) {
                    a::$foo = 2;
                    a::$foo().b = 3;
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,245))
    
    def test_246_array_size(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                Constructor(a:Int) {
                    a::$foo = 02;
                    a::$foo().b = 3;
                    Val a:Array[Int, 02];
                    a = Array(1,2);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,246))
    
    def test_247_empty_array(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                Constructor(a:Int) {
                    a::$foo = 02;
                    a::$foo().b = 3;
                    Val a:Array[Int, 10];
                    a = Array() + 2 + 00 + 0x0 + 0E1;
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,247))
    
    def test_248_sign_op(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                Constructor(a:Int) {
                    a::$foo = 02;
                    a::$foo().b = 3;
                    Val a:Array[Int, 02];
                    a = -1;
                    cd = 1 + 2 + 3 - 5 * 6 / 4 + 2;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,248))
    
    def test_249_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                Constructor(a:Int) {
                    a = (cd[12][3]).get() + 2;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,249))
    
    def test_250_syntax(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                Var $a, b, $c : Array[Int, 2];
                Constructor(a:Int) {
                    a = (cd[12][3]).get() + 2;
                    a = cd.get();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,250))
    
    def test_251_syntax_error(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                Var $a, b, $c : Array[Int, 2];
                Constructor(a:Int) {
                    a = (cd[12][3]).get() + 2;
                    a = cd.get();
                    a = New X()[2];
                    arr[2][3][4] = (a[1]).get(3) + a[2];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,251))
    
    def test_252_syntax_error(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                Var $a, b, $c : Array[Int, 2];
                Constructor(a:Int) {
                    Var a, b, c : Array[Int, 2];
                    a = (cd[12][3]).get() + 2;
                    a = cd::$get();
                    a = New X()[2];
                    arr[2][3][4] = (a[1]).get(3) + a[2];
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,252))
    
    def test_256_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                func() {
                    a = 1 + 2 % 3;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,256))

    def test_257_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                func() {
                    a = 1 + 2 % 3 + New A(a, b) + Array("123", "123");
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,257))
    
    def test_258_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                func() {
                    a = 1 + 2 % 3 + New A(a, b) + Array("123", "123");
                }
            }
            Class Vari:Shape {
                func() {
                    a = 1 + 2 % 3 + New A(a, b) + Array("123", "123");
                }
            }
            Class Vari:Shape {
                func() {
                    a = 1 + 2 % 3 + New A(a, b) + Array("123", "123");
                    {

                    }
                    {

                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,258))
    
    def test_259_complex_expr(self):
        """More complex program"""
        input = """
        
            Class Vari:Shape {
                func() {
                    a = 1 + 2 % 3 + New A(a, b) + Array("123", "123") + !a - 3;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,259))
    
    def test_260_complex_expr(self):
        """More complex program"""
        input = """
        
            Class Vari:Shape {
                Var a: String;
                func() {
                    If (current == "01/01/2022") {
                        System.print("Happy new year");
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,260))
    
    def test_261_complex_expr(self):
        """More complex program"""
        input = """
        
            Class Vari:Shape {
                Var a: String;
                func() {
                    If (current == "01/01/2022") {
                        System.print("Happy new year");
                    } Else {
                        System.print("Let's study together");
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,261))

    def test_262_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari:Shape {
                Var a: String;
                func() {
                    a = 3 || a;
                    If (current == "01/01/2022") {
                        System.print("Happy new year");
                    } Elseif((a != 3) || (a == 3)) {
                        System.print("Let's study together");
                    }
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,262))
    
    def test_263_complex_expr(self):
        """More complex program"""
        input = """
        
            Class Vari:Shape {
                Var a: String;
                func() {
                    a = 3 || a;
                    Foreach (i In 1 .. 100 By 2) {
                        Out.printInt(i);
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,263))
    
    def test_264_complex_expr(self):
        """More complex program"""
        input = """
        
            Class Vari:Shape {
                Var a: String;
                func() {
                    a = 3 || a;
                    Foreach (i In 1 .. 100 By expr) {
                        Out.printInt(i);
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,264))
    
    def test_265_complex_expr(self):
        """More complex program"""
        input = """
        
            Class Vari:Shape {
                Var a: String;
                func() {
                    a = 3 || a;
                    Foreach (i In 1 .. 100) {
                        Out.printInt(i);
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,265))
    
    def test_265_complex_expr(self):
        """More complex program"""
        input = """
        
            Class Vari:Shape {
                Var a: String;
                func() {
                    a = 3 || a;
                    Foreach (i In 1 .. 100) {
                        Out.printInt(i);
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,265))
    
    def test_266_complex_expr(self):
        """More complex program"""
        input = """
        
            Class Vari:Shape {
                Var a: String;
                func() {
                    a = 3 || a;
                    Foreach (i In 1 .. 100) {
                        Out.printInt(i);
                        a = 3 + 2 / 1 * 5 % 2;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,266))
    
    def test_267_complex_expr(self):
        """More complex program"""
        input = """
        
            Class Vari:Shape {
                Var a: String;
                $func() {
                    a = Self.a + 2 - 1;    
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,267))

    def test_268_complex_expr(self):
        """More complex program"""
        input = """
        
            Class Vari:Shape {
                Var a: String;
                $func() {
                    a = Self.a + 2 - 1;  
                    Return Vari::$func(1,2);  
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,268))

    def test_270_complex_expr(self):
        """More complex program"""
        input = """
        
            Class Vari:Shape {
            }
            Class Vari:Shape {
            }
            Class Vari:Shape {
            }
            Class Vari:Shape {

                func() {
                    A::$a();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,270))
    
    def test_271_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari:Shape {

                func() {
                    A::$a();
                    b = a - 1 + Array(1, "13131", Array(1,2,3));
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,271))
    
    def test_272_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari:Shape {

                func() {
                    b = a - 1 + Array(1, "13131", Array(1,2,3));
                    Foreach (i In 1 .. 2) {
                        Continue;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,272))
    
    def test_273_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {

                func() {
                    b = a - 1 + Array(1, "13131", Array(1,2,3));
                    Foreach (i In 1 .. 2) {
                        a = 100;
                    }
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,273))
    
    def test_274_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {

                func() {
                    If (1 < 2) {
                        System::$print("Find this interested!");
                    } Elseif(2 > 1) {
                        System::$print("Find this interested!");
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,274))
    
    def test_275_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {

                func() {
                    a = "123" +. "123a";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,275))
    
    def test_276_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {

                func() {
                    a = "123" +. "123a";
                    a = a.get()[a] + b[2];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,276))

    def test_277_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {

                func() {
                    a = "123" +. "123a";
                    a = a.get()[a] + b[2];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,277))
    
    def test_278_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {

                func() {
                    Var a,b : Vari = New Vari(), New Vari();
                    a = "123" +. "123a";
                }
                $func() {
                    a = "123" +. "123a";
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,278))
    
    def test_279_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {

                func() {
                    Var a,b : Vari = New Vari(), New Vari();
                    a = "123" +. "123a";
                }
                $func() {
                    a = "123" +. "123a";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,279))
    
    def test_280_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari = New Vari(), New Vari();
                func() {
                    Var a,b : Vari = New Vari(), New Vari();
                    a = "123" +. "123a";
                }
                $func() {
                    a = "123" +. "123a";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,280))

    def test_281_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari = New Vari(), "123";
                func() {
                    Var a,b : Vari = New Vari(), New Vari();
                    a = "123" +. "123a";
                }
                $func() {
                    a = "123" +. "123a";
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,281))
    
    def test_282_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                func() {
                    Var a,b : Vari = New Vari(), New Vari();
                    a = "123" +. "123a";
                    {
                        A::$print();
                    }
                }
                $func() {
                    a = "123" +. "123a";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,282))
    
    def test_283_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                func() {
                    Var a,b : Vari = New Vari(), New Vari();
                    a = "123" +. "123a";
                    {
                        A::$print();
                    }
                }
                $func() {
                    a = "123" +. "123a";
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,283))
    
    def test_284_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                func() {
                    Var a,b : Vari = New Vari(), New Vari();
                    a = ("123" +. "123a") ==. "123";
                    {
                        A::$print();
                    }
                }
                $func() {
                    a = "123" +. "123a";
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,284))

    def test_287_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                Val $A1,$A2,$A3: Int = 100_000,0123_567,0B10111;
                func() {
                    Var a,b : Vari = New Vari(), New Vari();
                    
                    a = ("123" +. "123a") ==. "123";
                    {
                        A::$print();
                        a = X.b();
                    }
                }
                $func() {
                    a = "123" +. "123a";
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,287))
    
    def test_288_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                Val $A1,$A2,$A3: Int = 100_000,0123_567,0B10111;
                func() {
                    Var a,b : Vari = New Vari(), New Vari();
                    
                    arr = Array (
                        Array("Volvo", "22", "18"),
                        Array("Saab", "5", "2"),
                        Array("Land Rover", "17", "15")
                        );
                }
                $func() {
                    a = "123" +. "123a";
                
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,288))
    
    def test_290_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                Val $A1,$A2,$A3: Array[Int,3] = 100_000,0123_567,0B10111;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,290))
    
    def test_291_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                Val $A1,$A2,$A3: Array[Int, 3] = 100_000,0123_567,0B10111;
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,291))
    
    def test_292_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                Var a:Int = Array(1 + 2, 3, 5, "123" + 2);
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,292))
    
    def test_293_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                Var a:Int = Array(1 + 2, 3, 5, "123" + 2);
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,293))
    
    def test_294_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                Var a:Int = Array(1 + 2, 3, 5, "123" + 2);
                $success() {

                    Return "Success" + Self.success;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,294))
    
    def test_295_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                Var a:Int = Array(1 + 2, 3, 5, "123" + 2);
                $success() {

                    (Vari::$success).get().a = 2;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,295))
    
    def test_296_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                Var a:Int = Array(1 + 2, 3, 5, "123" + 2);
                $success() {

                    (Vari::$success).get().a = 2;
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,296))
    
    def test_297_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                Var a:Int = Array(1 + 2, 3, 5, "123" + 2);
                $success() {

                    X.success();
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,297))
    
    def test_298_complex_expr(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                Var a:Int = Array(1 + 2, 3, 5, "123" + 2);
                $success() {

                   Return self.play();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect,298))
    
    def test_300_greeting(self):
        """More complex program"""
        input = """
            Class Vari {
                Var a, $b : Vari;
                Var a:Int = Array(1 + 2, 3, 5, "123" + 2);
                $greeting() {
                   If (Date::$LunarDate(current) == Date::$LunarNewYear) {
                       Console.writeLn("Chuc mung nam moi");
                   }
                   Else {
                       Console.writeLn("Fix bug di");
                   }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.test(input,expect, 300))
    def test_223_missing_colon(self):
        """More complex program"""
        input = """
            Class Pro:Shape {
                Var length, width: Int;
                getNumOfShape() {
                    Foreach (i In (1 + 2) .. (3+5) By 2) {
                        System.getName(1, a);
                        X.getName(a).get.foo(1,2).Call.by.reset();
                        If (i == 3) { } 
                        Elseif(i != 1) {
                            a = 1 + 2 - 5;
                            b = "abc" +. "1312";
                        }
                        Else { 
                            Return;
                        }
                    }
                }
                main() {
                    Return Null;
                }
            }
        """
        expect = ""
        self.assertTrue(TestAST.test(input,expect,223)) '''
    