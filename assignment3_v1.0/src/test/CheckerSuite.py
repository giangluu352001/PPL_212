import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        input = """
        Class Shape {
            Var h, $x: Int = 4, 5;
            Val w: Shape = New Shape();
            Var $r: Shape = New Shape();
            Var k: String;
            Val m: Int = 100;
            hi(){
                Return 5 + Self.w.m;
            }
        }
        Class Rectangle: Shape{
            Val k: Int = 1;
        }
        Class Program: Shape{
            Val k: Int = 1;
            Var x: Int;
            Val class: Shape = New Shape();
            Constructor(a:Int) {
                Self.x = a;
                Return;
            }
            getName(u: Int;w:Int) {
                Var b: Shape = New Shape();
                Val a: Int = Self.class.w.hi() + 1 ;
                ##b = New Shape();##
                ##b = New Program(1)
                Self.class = b;##
                Self.x = Self.class.hi() + 1 + Shape::$x + b.hi();
                Return;
                {
                    Var giang: Int = 5 + b.hi();
                    Var arr: Array[Float, 5];
                    ##arr = Array(giang + 1, u*w, 4*giang/w , 100, 20 + 12 + w);##
                    giang = 5*u + w;
                    ##Return giang + 2;##
                }
            }
            $hello() {
                Return 100;
            }
            getType(a: Array[Array[Array[Int, 3], 3], 2]; b: Program; c: Int) {
                Return a[0];
            }
            main() {
                Var check: String = "hehe";
                Var isBool: Boolean = True;
                Var c: Program = New Program(1);
                Var x,y: Int = 1, 3;
                Var a: Int = 1;
                ##Val hoho: Int = 5 + 6*x;##
                If (Self.x >= a) {
                    Val arr: Array[Array[Array[Int, 3], 3], 2] = Array (
                        Array(
                            Array(1, 2, 3),
                            Array(4, 5, 6 + Self.x),
                            Array(7, 8, 9)
                        ),
                        Array(
                            Array(10, 11, 12),
                            Array(13, 14, 15),
                            Array(16, 17, 18)
                        )
                    );
                    Val u: Int = arr[Self.x][1][2];
                    Val a: Int = 1 + Program::$hello() + Self.getType(arr, c, 1)[0][0];
                    Shape::$x = arr[a + 1][Self.x + 5][0] + 3;
                    arr[0][1] = Array(100, 200, 300);
                    Foreach (a In 5 .. 2) {
                        If (arr[x][y][y+2] == 5) {
                            Break;
                        }
                    }
                }
                Elseif (check ==. ("abb" +. "qq")) {
                    Self.getName(x, y);
                }
                Elseif (!isBool) {
                    Self.getName(x, x+2);
                }
                Else {
                    Return;
                }
            }
        }"""
        expect = "Illegal Constant Expression: ArrayCell(Id(arr),[FieldAccess(Self(),Id(x)),IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Class Program: Shape {
            Var a, $y, $x: Int =  1, 4, 5;
            Val $giang: Float = 1.e-4;
            $method(param: String) {
              Self.a = Shape::$getName() + New X().toString(a,b,c);
              Var a, b: Int;
              Foreach(i In (1+9/2) .. (3*4+2)) {

              }
              If(a > 3) {
                Return a;
              }
              Elseif(a < 3) {
                Return b;
              }
              Else {
                Return c;
              }
            }
            }"""
        expect = "Undeclared Class: Shape"
        self.assertTrue(TestChecker.test(input,expect,300))
    def testSample(self):
        self.assertTrue(TestChecker.test("""Class Program {
        main() {
          If (a) {
            Return;
          }
          Elseif(b) {
            Continue;
          }
          Elseif(c) {
            Return x;
          }
        }
      }""", "Undeclared Identifier: a", 301))
    def testCall(self):
      self.assertTrue(TestChecker.test("""Class Rectangle {
        main() {
            X::$shape().getName().callme();
        }
    }""", "Undeclared Class: X", 302))
    def test_101(self):
        self.assertTrue(TestChecker.test("""Class Program {
            Var temp, $x: Int = 1,2;
            main(a, b: Int; c,d: String) {
                Var w, s: Int = 10.2, 5.32;
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
                Out.printInt().getName();
                Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Var x, y : Int = 0, 0;
                Foreach (x In 144 .. 66) {
                    Out.printInt(arr[x]);
                }
                A[3][4] = 1;
                Shape.x.y = 5;
                Return a;
            }
        }""","Type Mismatch In Statement: VarDecl(Id(w),IntType,FloatLit(10.2))",101))
    def test_102(self):
        self.assertTrue(TestChecker.test("""
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
    ""","Illegal Member Access: FieldAccess(Self(),Id(length))",102))
    def test_103(self):
        self.assertTrue(TestChecker.test(""" 
        Class key {
            Val My1stCons, My2ndCons: Int = New X(a, b).Y(), 4;
        }""", "Undeclared Class: X", 103))
    def test_104(self):
        self.assertTrue(TestChecker.test(""" 
        Class X { 
            Var My1stCons, My2ndCons: Int = Shape::$1, X.A1234;
        }""", "Undeclared Class: Shape", 104))
    def test_105(self):
        self.assertTrue(TestChecker.test(""" Class test {
            Var My1stCons, My2ndCons: Int;
        }""", "No Entry Point", 105))
    def test_106(self):
        self.assertTrue(TestChecker.test("""
        Class Name {
            Val My1stCons, a2, a3: Int = (1+1).X(), 2, 3;
        }
        """, "Type Mismatch In Expression: CallExpr(BinaryOp(+,IntLit(1),IntLit(1)),Id(X),[])", 106))
    def test_107(self):
       self.assertTrue(TestChecker.test(""" 
        Class X {
           Val a, b: Int = 1, 2;
        }""", "No Entry Point", 107))  
    def test_108(self):
        self.assertTrue(TestChecker.test(""" 
        Class A{
            Constructor() {
                New X().list();
            }
        }""", "Undeclared Class: X", 108))
    def test_109(self):
        self.assertTrue(TestChecker.test(""" 
        Class X {
            Var a, $x: Array[Int, 0x1];
            Constructor(a,b,c: Int) {
                a = Shape::$a___q + Array(1,2,3);
            }
        }""", "Undeclared Class: Shape", 109))
    def test_110(self):
        self.assertTrue(TestChecker.test(""" 
        Class X {
            main() {
                Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(i);
                }
            }
        }""", "Undeclared Identifier: i", 110)) 
    def test_111(self):
        self.assertTrue(TestChecker.test("""
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
        """, "Undeclared Identifier: a", 111))
    def test_112(self):
        self.assertTrue(TestChecker.test("""
        Class Single {
            $staticmethod(a,b,c: Int; x,y,z: Array[Int,5]) {
                Return Shape::$getName();
            }
        }""", "Undeclared Class: Shape", 112))
    def test_113(self):
        self.assertTrue(TestChecker.test("""
        Class Single {
            Var $atrr : Int;
            $staticmethod(a,b,c: Int; x,y,z: Array[Int,5]) {
                Single::$atrr = a + b + Shape::$getName();
            }
        }""", "Undeclared Class: Shape", 113))
    def test_114(self):
        self.assertTrue(TestChecker.test("""
        Class Single {
            staticmethod() {
                Var x, y: Int;
                Return x + y;
            }
        }""", "No Entry Point", 114))
    def test_115(self):
        self.assertTrue(TestChecker.test("""
        Class Single {
            $Constructor(a: Int) {
                Return;
            }
        }""", "No Entry Point", 115))
    def test_116(self):
        self.assertTrue(TestChecker.test("""
        Class Name {
            Val x: String = "abc" + "cdf";
        }""", "Type Mismatch In Expression: BinaryOp(+,StringLit(abc),StringLit(cdf))", 116))
    def test_117(self):
        self.assertTrue(TestChecker.test("""
        Class Tail {
            Destructor() {
                Var x: String = "a\\t" + Self.str(Shape::$getName());
            }
        }""", "Undeclared Class: Shape", 117))
    def test_118(self):
        self.assertTrue(TestChecker.test("""
        Class Single {
            $getName() {
                Return "This is a string";
            }
        }
        Class Program {
            main() {
                Out.print(Single::$getName());
            }
        }""", "Undeclared Identifier: Out", 118))
    def test_119(self):
        self.assertTrue(TestChecker.test("""
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
        }""", "Undeclared Identifier: a", 119))
    def test_120(self):
        self.assertTrue(TestChecker.test("""
        Class Single: Shape {
            $staticmethod() {
                Foreach (X In 10 .. 100) {
                    Shape::$x = X.foo() + New Shape().X(a,b);
                }
            }
        }""", "Undeclared Class: Shape", 120))
    def test_121(self):
        self.assertTrue(TestChecker.test("""
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
        }""", "Type Mismatch In Statement: If(Id(a),Block([Return(Id(a))]),If(BinaryOp(<,CallExpr(Self(),Id(size),[Id(a)]),IntLit(5)),Block([AssignStmt(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]),Break])))", 121))
    def test_122(self):
        self.assertTrue(TestChecker.test("""
        Class Double {
            Constructor() {
                Var x: Array[String, 5];
            }
            main() {
                If(Self.x[0] == "This") {
                    x = Array("This", "is", "a", "string", "!");
                }
            }
        }""", "Undeclared Attribute: x", 122))
    def test_123(self):
        self.assertTrue(TestChecker.test("""
        Class Double {
            $staticmethod(a,b,c: Int) {
                Return b;
            }
        }""", "No Entry Point", 123))
    def test_124(self):
        self.assertTrue(TestChecker.test("""
        Class Single {
            Var x: Array[Array[String, 5], 5];
            main() {
                x = x[a + 3 == 1] + x[c[b[5]]];
            }
        }""", "Undeclared Identifier: x", 124))
    def test_125(self):
        self.assertTrue(TestChecker.test("""
        Class A {
            main() {
                Foreach (_ In 0x11 .. 0x55) {
                    Out.convert(_);
                }
            }
        }""", "Undeclared Identifier: _", 125))
    def test_126(self):
        self.assertTrue(TestChecker.test("""
        Class Single {
            Val x, $y: String = "a", "yz";
        }""", "No Entry Point", 126))
    def test_127(self):
        self.assertTrue(TestChecker.test("""
        Class Single {
        }
        Class X: Single {
            main() { }
        }""", "No Entry Point", 127))
    def test_128(self):
        self.assertTrue(TestChecker.test("""
        Class Single {
            A(a: Int) {
                Return a;
            }
            B(b:String) {
                If(b +. "String" == "abcString") {
                    Break;
                }
            }
        }""", "Type Mismatch In Expression: BinaryOp(==,StringLit(String),StringLit(abcString))", 128))
    def test_129(self):
        self.assertTrue(TestChecker.test("""Class x { }""", "No Entry Point", 129))
    def test_130(self):
        self.assertTrue(TestChecker.test(""" Class X: Y{ }""", "Undeclared Class: Y", 130))
    def test_131(self):
        self.assertTrue(TestChecker.test("""
        Class One {
            Main() {
                Var a, b: Int;
                a = b + 1.00e-0004 * 0x200;
            }
        }""", "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,Id(b),BinaryOp(*,FloatLit(0.0001),IntLit(512))))", 131))
    def test_132(self):
        self.assertTrue(TestChecker.test("""
        Class Single {
            $static() {
                Self.x = Self.y + Shape::$X().Y();
            }
        }""", "Illegal Member Access: FieldAccess(Self(),Id(x))", 132))
        self.assertTrue(TestChecker.test("""
        Class Single {
            Destructor() {
            }
        }""", "No Entry Point", 133))
    def test_134(self):
        self.assertTrue(TestChecker.test("""
        Class Single {
            $static() {
                Self.x = (1+2).y() + New X(a,b).Y(Shape::$x);
            }
        }""", "Illegal Member Access: FieldAccess(Self(),Id(x))", 134))
    def test_135(self):
        self.assertTrue(TestChecker.test("""
        Class Double {
             Name() {
                Val a: Int = 1;
            }
        }""", "No Entry Point", 135))
    def test_136(self):
        self.assertTrue(TestChecker.test("""
        Class Single {
            $static() {
                Var r: Float;
                r = 123_34.e-10;
                r = r*s*Self.x;
                a[0][0] = r + Self.y;
            }
        }""", "Undeclared Identifier: s", 136))
    def test_137(self):
        self.assertTrue(TestChecker.test("""
        Class Single {
            $static() {
            }
        }""", "No Entry Point", 137))
    def test_138(self):
        self.assertTrue(TestChecker.test("""
        Class Single {
            get(a: String) {
                If(Self.compare(a, "String") == 0) {
                    Continue;
                }
                Else {
                    Return A::$x + A::$y;
                }
            }
        }""", "Undeclared Method: compare", 138))
    def test_139(self):
        self.assertTrue(TestChecker.test("""
        Class A {
            $static() {
                Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(arr[i][i+2*i - 2]);
                }
            }
        }""", "Undeclared Identifier: i", 139))
    def test_140(self):
        self.assertTrue(TestChecker.test("""
        Class A {
            Val $x, $y: Int = 1 + _.foo(1,4), 0;
            method() {
               Val x: String = "a\\\\";
               Return x + Self.str(S::$x) + Self.str(S::$y); 
            }
        }""", "Undeclared Identifier: _", 140))
    def test_141(self):
        self.assertTrue(TestChecker.test("""
        Class A {
            $static() {
                X.foo(A.value);
            }
        }""", "Undeclared Identifier: A", 141))
    def test_142(self):
        self.assertTrue(TestChecker.test("""
        Class A {
            $name() {
                Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(i);
                }
            }
        }""", "Undeclared Identifier: i", 142))
    def test_143(self):
        self.assertTrue(TestChecker.test("""
        Class A {
            static(a: Int; b: String) {
            }
        }""", "No Entry Point", 143))
    def test_144(self):
        self.assertTrue(TestChecker.test("""
        Class A {
            float() {
                Break;
            }
        }""", "Break Not In Loop", 144))
    def test_145(self):
        self.assertTrue(TestChecker.test("""
        Class A {
            Val x: Array[Int, 2] = Array(1,2);
            method(a: Int) {
                If(Self.x[a + 2] <= 100) {
                    Self.x = Self.get()[(a+2)*5];
                }
            }
        }""", "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(x)),ArrayCell(CallExpr(Self(),Id(get),[]),[BinaryOp(*,BinaryOp(+,Id(a),IntLit(2)),IntLit(5))]))", 145))
    def test_146(self):
        self.assertTrue(TestChecker.test("""
        Class A {
            Constructor() {}
            Constructor() {}
            Destructor() {}
            Destructor() {}
        }""", "Redeclared Special Method: Constructor", 146))
    def test_147(self):
        self.assertTrue(TestChecker.test("""
        Class A {
            Constructor() {
                Self.x[(Self.y[x+3]).getFoo()] = 1 + 4;
            }
            Destructor() { 
                Return False;
            }
        }""", "Undeclared Attribute: x", 147))
    def test_148(self):
        self.assertTrue(TestChecker.test("""
        Class A {
            Constructor() {
                Return Self + Self;
            }
            Destructor() { }
        }""", "Type Mismatch In Statement: Return(BinaryOp(+,Self(),Self()))", 148))
    def test_149(self):
        self.assertTrue(TestChecker.test("""
        Class X {
            main(foo: Array[Array[String, 5], 2]) {
                If(foo[0][2] == 1 + 3) {
                    Return foo[x+ Self.y];
                }
                Elseif(!foo) {
                    foo[0][1] = -45.e-10;
                } 
            }
        }""", "Type Mismatch In Expression: BinaryOp(==,ArrayCell(Id(foo),[IntLit(0),IntLit(2)]),BinaryOp(+,IntLit(1),IntLit(3)))", 149))
    def test_150(self):
        self.assertTrue(TestChecker.test("""
        Class A {
            Val x: Int = 1;
            Var $y, u: String = Self.str(1) + "abc", Self.str(x);
        }""", "Undeclared Method: str", 150))
    def test_151(self):
        self.assertTrue(TestChecker.test("""
        Class A {
            Val x,y,z: Float;
            main() {
              x = x + 2;
            }
        }""", "Illegal Constant Expression: None", 151))
    def test_152(self):
        self.assertTrue(TestChecker.test("""
        Class Name {
            Constructor(A: Int; B: String) {
                Self.x = New X(A,B);
                Return Self.x;
            }
        }""", "Undeclared Attribute: x", 152))
    def test_153(self):
        self.assertTrue(TestChecker.test("""
        Class B: A {}
        Class C: B {
            Val arr: Array[String, 2];
            method() {
                Self.arr = Array(1,2,3) + Array(4,5,6);
                Self.arr[0] = "string";
            }
        }""", "Undeclared Class: A", 153))
    def test_154(self):
        self.assertTrue(TestChecker.test("""
        Class A {
            method() {
                foo = Self.get()[3+x] + Array(1,2,3);
            }
        }""", "Undeclared Identifier: foo", 154))
    def test_155(self):
        self.assertTrue(TestChecker.test(""" Class A { $x() { Break; } } """,
         "Break Not In Loop", 155))
    def test_156(self):
        self.assertTrue(TestChecker.test(""" 
        Class A {
            Var x,y: Int = 1, 2;
        } """, "No Entry Point", 156))
    def test_157(self):
        self.assertTrue(TestChecker.test("""Class A {Var u: Array[Int, 1];}""", "No Entry Point", 157))
    def test_158(self):
        self.assertTrue(TestChecker.test(""" Class Done {method() { Return X.foo(Self.x); } }""",
         "Undeclared Attribute: x", 158))
    def test_159(self):
        self.assertTrue(TestChecker.test("""
        Class Done {
            Val x: Boolean;
            method() {
                Return Shape::$foo();
            }
        }""", "Illegal Constant Expression: None", 159))
    def test_160(self):
        self.assertTrue(TestChecker.test("""
        Class Done {
            setName(a: Boolean) {
                If(a) {
                    Return (x+1).foo(a) + 2;
                }
                Elseif(!a) {
                    Continue;
                }
            }
        }""", "Undeclared Identifier: x", 160))
    def test_161(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Var a: Int = (Self.x[1][2]).getName();
            }
        }
        """, "Undeclared Attribute: x", 161))
    def test_162(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Var a: Int = Self.x[1][2][a[x+4]];
                a = a + 1_234.e-1;
                Return a;
            }
        }
        """, "Undeclared Attribute: x", 162))
    def test_163(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Var a: Int = Shape.getName();
                If(!Shape::$get() && !(x+3 == 10) || Self.x != "abc") {
                    Break;
                }
            }
        }
        """, "Undeclared Identifier: Shape", 163))
    def test_164(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main(a: Int) {
                Var a: Float = -1 - 10.e-4;
                Var b: Float = -10.e-10 + -1.e-005;
            }
        }
        """, "Redeclared Variable: a", 164))
    def test_165(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Var a: Int = x % 4 == 0;
                Var b: Int = (x / 4 % 3 == 0) && (x<=3)*10;  
            }
        }
        """, "Undeclared Identifier: x", 165))
    def test_166(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                If((Self.x <= 10.e-10) || (-X.getName().get < 0)) {
                    X = X[A[x+2*i]] % 3;
                }
            }
        }
        """, "Undeclared Attribute: x", 166))
    def test_167(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Var x, y: Int;
                Return x;
            }
        }
        """, "Type Mismatch In Statement: Return(Id(x))", 167))
    def test_168(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            $_(a,b: String) {
                If(a != "String" || ((a-5)*A[x[v.getIndex(a)]] <= 10)) {
                    Continue;
                }
            }
        }
        """, "Type Mismatch In Expression: BinaryOp(-,Id(a),IntLit(5))", 168))
    def test_169(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            $_() {
                a = (New X(x)[1][1]).getName();
            }
        }
        """, "Undeclared Identifier: a", 169))
    def test_170(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Var a: Int = A::$setName();
            }
        }
        """, "Undeclared Class: A", 170))
    def test_171(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Val x: Int = New X().Y().Shape;
            }
        }
        """, "Undeclared Class: X", 171))
    def test_172(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Var a: Int = (New Shape().getClass()).Shape();
            }
        }
        """, "Undeclared Class: Shape", 172))
    def test_173(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                x = ("abc\\n" +. "xyz\\t").Y()[1];
            }
        }
        """, "Undeclared Identifier: x", 173))
    def test_174(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Var a: Int = (X+3).Y(Array(1,2,3,4));
            }
        }
        """, "Undeclared Identifier: X", 174))
    def test_175(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Var a: Int = X::$Shape;
            }
        }
        """, "Undeclared Class: X", 175))
    def test_176(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Var a: Int = no::$x + no::$y;
            }
        }
        """, "Undeclared Class: no", 176))
    def test_177(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() { }
            getName() {
                Return x == 5 || (!x && x <= x - 3);
            }
        }
        """, "Undeclared Identifier: x", 177))
    def test_178(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                out.println("Hello World");
                x.print();
            }
        }
        """, "Undeclared Identifier: out", 178))
    def test_179(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            Constructor() {
                If(x/2/3 == 0 +. "abc") {
                    Foreach(I In 0b0 .. 0b11) {
                        Break;
                    }
                }
            }
        }
        """, "Undeclared Identifier: x", 179))
    def test_180(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            program() {
                Return x;
            }
        }
        """, "Undeclared Identifier: x", 180))
    def test_181(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                x = (x == 5 && (x+3) +. "abc") || (x == a[5] && y ==. "xyz");
            }
        }
        """, "Undeclared Identifier: x", 181))
    def test_182(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Var x: Int = (x+3)*2/2 == 0 && (x.get().shape()[A[x]] != 0);
            }
        }
        """, "Undeclared Identifier: x", 182))
    def test_183(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Val x: String = !Self.bool && !A[d[x+3]] || Shape::$name() != A.get(i);
            }
        }
        """, "Undeclared Attribute: bool", 183))
    def test_184(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Val temp: Boolean = 
                !New X(a,b).getCheck() && New Y().get(!a + b);
            }
        }
        """, "Undeclared Class: X", 184))
    def test_185(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Var x: Array[Int, 5] = Array(x+3, !getName.X(), -x-5+3, 1);
            }
        }
        """, "Undeclared Identifier: x", 185))
    def test_186(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                Var x: Array[String, 2] = 
                Array("abc" +. "xyz", x+3 != !(x-5));
            }
        }
        """, "Undeclared Identifier: x", 186))
    def test_187(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                If(Array(1,2,3) == Array(x+3, !A[x[2]])) {
                    Out.println("\\n");
                }
            }
        }
        """, "Undeclared Identifier: x", 187))
    def test_188(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            main() {
                If(Array(Array(1,2,3), Array(4,5,6)) != (Array(1,2,3))) {
                    Break;
                    Out.raise("error");
                }
            }
        }
        """, "Type Mismatch In Expression: BinaryOp(!=,[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4),IntLit(5),IntLit(6)]],[IntLit(1),IntLit(2),IntLit(3)])", 188))
    def test_189(self):
        self.assertTrue(TestChecker.test("""
        Class Program {
            Val x: Int = (("abc" +. "xyz") ==. "abcxyz") || (x == 4 && !x);
        }
        """, "Undeclared Identifier: x", 189))
    def test_190(self):
        self.assertTrue(TestChecker.test("""
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
        """, "Undeclared Identifier: name", 190))
    def test_191(self):
        self.assertTrue(TestChecker.test("""
        Class A { Val v, $x: Int; }
        Class Shape {
            $getName(a,b: A) {
                A::$x = a.v + b.v;
            }
        }
        """, "Illegal Constant Expression: None", 191))
    def test_192(self):
        self.assertTrue(TestChecker.test("""
        Class Shape {
            $getName(a,b: Shape; x,y: Rectangle) {
                Return New X() + New Y() - New Z().get();
            }
        }
        """, "Undeclared Class: X", 192))
    def test_193(self):
        self.assertTrue(TestChecker.test("""
        Class Shape {
            $getName(a: A) {
                A::$x = (A::$x == 0) || (A::$x != 2);
            }
        }
        """, "Undeclared Class: A", 193))
    def test_194(self):
        self.assertTrue(TestChecker.test("""
        Class Shape {
            Val x, $y: Rectangle = Null, Null;
            main() {
                If(x == Null && (Shape::$y != Null)) {
                    Return x;
                }
            }
        }
        """, "Undeclared Class: Rectangle", 194))
    def test_195(self):
        self.assertTrue(TestChecker.test("""
        Class Shape {
            $getName(a,b,d: Int; c,f: Shape) {
                (a[2])[2] = 1;
                a[2][2] = 2;
                X.getFoo().getName();
            }
        }
        """, "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(2)])", 196))
    def test_197(self):
        self.assertTrue(TestChecker.test("""
        Class Shape {
            main() {
              Shape::$x = a + b;
            }
        }
        """, "Undeclared Attribute: $x", 197))
    def test_198(self):
        self.assertTrue(TestChecker.test("""
        Class Shape {
            $getName() {
                Out.print();
            }
        }
        """, "Undeclared Identifier: Out", 198))
    def test_199(self):
        self.assertTrue(TestChecker.test("""
        Class Shape {
            Val x, y: X ;
            getName() {
                v = x.get() == y.get();
            }
        }
        """, "Undeclared Class: X", 199))
    def test_200(self):
        self.assertTrue(TestChecker.test("""
        Class Shape {
            $getName() {
                Var x: Shape;
                Val y: Star;
                Foreach(Y In 100 .. 200) {
                   
                }
            }
        }
        """, "Undeclared Class: Star", 200)) 

    def test_223_missing_colon(self):
        """More complex program"""
        input = """
            Class Pro:Shape {
                Var length, width: Int;
                getNumOfShape() {
                    Foreach (i In (1+2*3) .. (3-5/2) By 2) {
                        System.getName(1, a);
                        X.getName(a).get.foo(1,2).Call.by.reset();
                        If (i == 3) { } 
                        Elseif(i != 1) {
                            a = 1 + New X().field;
                            b = ("abc" +. "1312") ==. "string";
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
        expect = "Undeclared Class: Shape"
        self.assertTrue(TestChecker.test(input,expect,220))