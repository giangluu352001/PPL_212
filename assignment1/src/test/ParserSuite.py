import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
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
                Out.printInt(Shape::$numOfShape);
                Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Var $x, $y : Int = 0, 0;
                Foreach (x In 144 .. 66) {
                    Out.printInt(arr[x]);
                }
                Return a;
            }
        }""","Error on line 16 col 20: $x",101))
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
        """, "Error on line 5 col 30: ==", 196))
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