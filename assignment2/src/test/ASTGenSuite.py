import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Class Program: Shape {
            Var a, $y, $x: Int =  1, 4, 5;
            Val $giang: Float = 1.e-4;
            $method(param: String) {
              x = Shape::$getName() + New X().toString(a,b,c);
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
        expect = "Program([ClassDecl(Id(Program),Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(4))),AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(5))),AttributeDecl(Static,ConstDecl(Id($giang),FloatType,FloatLit(0.0001))),MethodDecl(Id($method),Static,[param(Id(param),StringType)],Block([AssignStmt(Id(x),BinaryOp(+,CallExpr(Id(Shape),Id($getName),[]),CallExpr(NewExpr(Id(X),[]),Id(toString),[Id(a),Id(b),Id(c)]))),VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),For(Id(i),BinaryOp(+,IntLit(1),BinaryOp(/,IntLit(9),IntLit(2))),BinaryOp(+,BinaryOp(*,IntLit(3),IntLit(4)),IntLit(2)),IntLit(1),Block([])]),If(BinaryOp(>,Id(a),IntLit(3)),Block([Return(Id(a))]),If(BinaryOp(<,Id(a),IntLit(3)),Block([Return(Id(b))]),Block([Return(Id(c))])))]))])])"
        self.assertTrue(TestAST.test(input,expect,300))
    def testSample(self):
      self.assertTrue(TestAST.test("""Class Program {
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
      }""", "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(Id(a),Block([Return()]),If(Id(b),Block([Continue]),If(Id(c),Block([Return(Id(x))]))))]))])])", 301))
    def testCall(self):
      self.assertTrue(TestAST.test("""Class Rectangle {
        main() {
            X::$shape().getName().callme();
        }
    }""", "Program([ClassDecl(Id(Rectangle),[MethodDecl(Id(main),Instance,[],Block([Call(CallExpr(CallExpr(Id(X),Id($shape),[]),Id(getName),[]),Id(callme),[])]))])])", 302))
    def test_101(self):
        self.assertTrue(TestAST.test("""Class Program {
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
        }""","Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(temp),IntType,IntLit(1))),AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(2))),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),StringType),param(Id(d),StringType)],Block([VarDecl(Id(w),IntType,FloatLit(10.2)),VarDecl(Id(s),IntType,FloatLit(5.32)),AssignStmt(Id(r),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,ArrayType(10,IntType))),VarDecl(Id(b),ArrayType(5,ArrayType(10,IntType))),If(BinaryOp(>=,Id(r),FloatLit(1234.0123)),Block([AssignStmt(Id(r),BinaryOp(+,Id(r),IntLit(124)))]),If(BinaryOp(==,Id(r),IntLit(134)),Block([AssignStmt(ArrayCell(Id(a),[IntLit(0),IntLit(1)]),IntLit(555))]),Block([AssignStmt(ArrayCell(Id(a),[IntLit(2),IntLit(3)]),BinaryOp(+,ArrayCell(Id(a),[IntLit(4),IntLit(5)]),ArrayCell(Id(a),[IntLit(6),IntLit(7)])))]))),Call(CallExpr(Id(Shape),Id($getName),[]),Id(X),[]),Call(CallExpr(Id(Out),Id(printInt),[]),Id(getName),[]),ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(5))),ConstDecl(Id(My2ndCons),IntType,IntLit(2)),VarDecl(Id(x),IntType,IntLit(0)),VarDecl(Id(y),IntType,IntLit(0)),For(Id(x),IntLit(144),IntLit(66),IntLit(1),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])]),AssignStmt(ArrayCell(Id(A),[IntLit(3),IntLit(4)]),IntLit(1)),AssignStmt(FieldAccess(FieldAccess(Id(Shape),Id(x)),Id(y)),IntLit(5)),Return(Id(a))]))])])",101))
    def test_102(self):
        self.assertTrue(TestAST.test("""
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
    ""","Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))])),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(x),BinaryOp(+,ArrayCell([[[StringLit(Volvo),StringLit(22),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]],[[StringLit(Volvo),StringLit(22),StringLit(18),StringLit(22)],[StringLit(Saab),StringLit(5),StringLit(2),StringLit(hehe)],[StringLit(Land Rover),StringLit(17),StringLit(15)]]],[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(Id(A),[IntLit(5),IntLit(5)])))]))])])",102))
    def test_103(self):
        self.assertTrue(TestAST.test(""" 
        Class key {
            Val My1stCons, My2ndCons: Int = New X(a, b).Y(), 4;
        }""", "Program([ClassDecl(Id(key),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,CallExpr(NewExpr(Id(X),[Id(a),Id(b)]),Id(Y),[]))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(4)))])])", 103))
    def test_104(self):
        self.assertTrue(TestAST.test(""" 
        Class X { 
            Var My1stCons, My2ndCons: Int = Shape::$1, X.A1234;
        }""", "Program([ClassDecl(Id(X),[AttributeDecl(Instance,VarDecl(Id(My1stCons),IntType,FieldAccess(Id(Shape),Id($1)))),AttributeDecl(Instance,VarDecl(Id(My2ndCons),IntType,FieldAccess(Id(X),Id(A1234))))])])", 104))
    def test_105(self):
        self.assertTrue(TestAST.test(""" Class test {
            Var My1stCons, My2ndCons: Int;
        }""", "Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(My1stCons),IntType)),AttributeDecl(Instance,VarDecl(Id(My2ndCons),IntType))])])", 105))
    def test_106(self):
        self.assertTrue(TestAST.test("""
        Class Name {
            Val My1stCons, a2, a3: Int = (1+1).X(), 2, 3;
        }
        """, "Program([ClassDecl(Id(Name),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,CallExpr(BinaryOp(+,IntLit(1),IntLit(1)),Id(X),[]))),AttributeDecl(Instance,ConstDecl(Id(a2),IntType,IntLit(2))),AttributeDecl(Instance,ConstDecl(Id(a3),IntType,IntLit(3)))])])", 106))
    def test_107(self):
       self.assertTrue(TestAST.test(""" 
        Class X {
           Val a, b: Int = 1, 2;
        }""", "Program([ClassDecl(Id(X),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(2)))])])", 107))  
    def test_108(self):
        self.assertTrue(TestAST.test(""" 
        Class A{
            Constructor() {
                New X().list(a, b);
            }
        }""", "Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[],Block([Call(NewExpr(Id(X),[]),Id(list),[Id(a),Id(b)])]))])])", 108))
    def test_109(self):
        self.assertTrue(TestAST.test(""" 
        Class X {
            Var a, $x: Array[Int, 0x1];
            Constructor(a,b,c: Int) {
                a = Shape::$a___q + Array(1,2,3);
            }
        }""", "Program([ClassDecl(Id(X),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(1,IntType))),AttributeDecl(Static,VarDecl(Id($x),ArrayType(1,IntType))),MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([AssignStmt(Id(a),BinaryOp(+,FieldAccess(Id(Shape),Id($a___q)),[IntLit(1),IntLit(2),IntLit(3)]))]))])])", 109))
    def test_110(self):
        self.assertTrue(TestAST.test(""" 
        Class X {
            main() {
                Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(i);
                }
            }
        }""", "Program([ClassDecl(Id(X),[MethodDecl(Id(main),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]))])])", 110)) 
    def test_111(self):
        self.assertTrue(TestAST.test("""
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
        """, "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(x),IntType))]),ClassDecl(Id(Program),[MethodDecl(Id(getName),Instance,[param(Id(x),IntType)],Block([VarDecl(Id(b),FloatType,BinaryOp(+,FloatLit(0.3),Id(x))),VarDecl(Id(object),ClassType(Id(Shape)),NewExpr(Id(Shape),[]))])),MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>=,Id(a),Id(b)),Block([VarDecl(Id(a),IntType,IntLit(0)),AssignStmt(ArrayCell(CallExpr(Id(Shape),Id($getShape),[]),[BinaryOp(+,IntLit(3),Id(x))]),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(c),[ArrayCell(Id(b),[IntLit(2)])])]),IntLit(3)))]),If(BinaryOp(>=,Id(b),Id(c)),Block([Call(Self(),Id(getName),[Id(a)])]),If(BinaryOp(>=,IntLit(12),Id(g)),Block([Call(Self(),Id(insert),[StringLit(String)])]),Block([Return(Id(object))]))))]))])])", 111))
    def test_112(self):
        self.assertTrue(TestAST.test("""
        Class Single {
            $staticmethod(a,b,c: Int; x,y,z: Array[Int,5]) {
                Return Shape::$getName();
            }
        }""", "Program([ClassDecl(Id(Single),[MethodDecl(Id($staticmethod),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(x),ArrayType(5,IntType)),param(Id(y),ArrayType(5,IntType)),param(Id(z),ArrayType(5,IntType))],Block([Return(CallExpr(Id(Shape),Id($getName),[]))]))])])", 112))
    def test_113(self):
        self.assertTrue(TestAST.test("""
        Class Single {
            Var $atrr : Int;
            $staticmethod(a,b,c: Int; x,y,z: Array[Int,5]) {
                Single::$atrr = a + b + Shape::$getName();
            }
        }""", "Program([ClassDecl(Id(Single),[AttributeDecl(Static,VarDecl(Id($atrr),IntType)),MethodDecl(Id($staticmethod),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(x),ArrayType(5,IntType)),param(Id(y),ArrayType(5,IntType)),param(Id(z),ArrayType(5,IntType))],Block([AssignStmt(FieldAccess(Id(Single),Id($atrr)),BinaryOp(+,BinaryOp(+,Id(a),Id(b)),CallExpr(Id(Shape),Id($getName),[])))]))])])", 113))
    def test_114(self):
        self.assertTrue(TestAST.test("""
        Class Single {
            staticmethod() {
                Var x, y: Int;
                Return x + y;
            }
        }""", "Program([ClassDecl(Id(Single),[MethodDecl(Id(staticmethod),Instance,[],Block([VarDecl(Id(x),IntType),VarDecl(Id(y),IntType),Return(BinaryOp(+,Id(x),Id(y)))]))])])", 114))
    def test_115(self):
        self.assertTrue(TestAST.test("""
        Class Single {
            $Constructor(a: Int) {
                Return;
            }
        }""", "Program([ClassDecl(Id(Single),[MethodDecl(Id($Constructor),Static,[param(Id(a),IntType)],Block([Return()]))])])", 115))
    def test_116(self):
        self.assertTrue(TestAST.test("""
        Class Name {
            Val x: String = "abc" + "cdf";
        }""", "Program([ClassDecl(Id(Name),[AttributeDecl(Instance,ConstDecl(Id(x),StringType,BinaryOp(+,StringLit(abc),StringLit(cdf))))])])", 116))
    def test_117(self):
        self.assertTrue(TestAST.test("""
        Class Tail {
            Destructor() {
                Var x: String = "a\\t" + Self.str(Shape::$getName());
            }
        }""", "Program([ClassDecl(Id(Tail),[MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(x),StringType,BinaryOp(+,StringLit(a\\t),CallExpr(Self(),Id(str),[CallExpr(Id(Shape),Id($getName),[])])))]))])])", 117))
    def test_118(self):
        self.assertTrue(TestAST.test("""
        Class Single {
            $getName() {
                Return "This is a string";
            }
        }
        Class Program {
            main() {
                Out.print(Single::$getName());
            }
        }""", "Program([ClassDecl(Id(Single),[MethodDecl(Id($getName),Static,[],Block([Return(StringLit(This is a string))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(print),[CallExpr(Id(Single),Id($getName),[])])]))])])", 118))
    def test_119(self):
        self.assertTrue(TestAST.test("""
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
        }""", "Program([ClassDecl(Id(Single),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(3))),MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(>=,BinaryOp(+,Id(a),Id(b)),Id(c)),Block([Return(Id(a))]),Block([Return(BinaryOp(+,Id(b),BinaryOp(*,IntLit(2),Id(c))))]))]))])])", 119))
    def test_120(self):
        self.assertTrue(TestAST.test("""
        Class Single: Shape {
            $staticmethod() {
                Foreach (X In 10 .. 100) {
                    Shape::$x = X.foo() + New Shape().X(a,b);
                }
            }
        }""", "Program([ClassDecl(Id(Single),Id(Shape),[MethodDecl(Id($staticmethod),Static,[],Block([For(Id(X),IntLit(10),IntLit(100),IntLit(1),Block([AssignStmt(FieldAccess(Id(Shape),Id($x)),BinaryOp(+,CallExpr(Id(X),Id(foo),[]),CallExpr(NewExpr(Id(Shape),[]),Id(X),[Id(a),Id(b)])))])])]))])])", 120))
    def test_121(self):
        self.assertTrue(TestAST.test("""
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
        }""", "Program([ClassDecl(Id(Double),[MethodDecl(Id(method),Instance,[param(Id(a),ArrayType(5,IntType))],Block([If(Id(a),Block([Return(Id(a))]),If(BinaryOp(<,CallExpr(Self(),Id(size),[Id(a)]),IntLit(5)),Block([AssignStmt(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]),Break])))]))])])", 121))
    def test_122(self):
        self.assertTrue(TestAST.test("""
        Class Double {
            Constructor() {
                Var x: Array[String, 5];
            }
            main() {
                If(Self.x[0] == "This") {
                    x = Array("This", "is", "a", "string", "!");
                }
            }
        }""", "Program([ClassDecl(Id(Double),[MethodDecl(Id(Constructor),Instance,[],Block([VarDecl(Id(x),ArrayType(5,StringType))])),MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(==,ArrayCell(FieldAccess(Self(),Id(x)),[IntLit(0)]),StringLit(This)),Block([AssignStmt(Id(x),[StringLit(This),StringLit(is),StringLit(a),StringLit(string),StringLit(!)])]))]))])])", 122))
    def test_123(self):
        self.assertTrue(TestAST.test("""
        Class Double {
            $staticmethod(a,b,c: Int) {
                Return b;
            }
        }""", "Program([ClassDecl(Id(Double),[MethodDecl(Id($staticmethod),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([Return(Id(b))]))])])", 123))
    def test_124(self):
        self.assertTrue(TestAST.test("""
        Class Single {
            Var x: Array[Array[String, 5], 5];
            main() {
                x = x[a + 3 == 1] + x[c[b[5]]];
            }
        }""", "Program([ClassDecl(Id(Single),[AttributeDecl(Instance,VarDecl(Id(x),ArrayType(5,ArrayType(5,StringType)))),MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(x),BinaryOp(+,ArrayCell(Id(x),[BinaryOp(==,BinaryOp(+,Id(a),IntLit(3)),IntLit(1))]),ArrayCell(Id(x),[ArrayCell(Id(c),[ArrayCell(Id(b),[IntLit(5)])])])))]))])])", 124))
    def test_125(self):
        self.assertTrue(TestAST.test("""
        Class A {
            main() {
                Foreach (_ In 0x11 .. 0x55) {
                    Out.convert(_);
                }
            }
        }""", "Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([For(Id(_),IntLit(17),IntLit(85),IntLit(1),Block([Call(Id(Out),Id(convert),[Id(_)])])])]))])])", 125))
    def test_126(self):
        self.assertTrue(TestAST.test("""
        Class Single {
            Val x, $y: String = "a", "yz";
        }""", "Program([ClassDecl(Id(Single),[AttributeDecl(Instance,ConstDecl(Id(x),StringType,StringLit(a))),AttributeDecl(Static,ConstDecl(Id($y),StringType,StringLit(yz)))])])", 126))
    def test_127(self):
        self.assertTrue(TestAST.test("""
        Class Single {
        }
        Class X: Single {
            main() { }
        }""", "Program([ClassDecl(Id(Single),[]),ClassDecl(Id(X),Id(Single),[MethodDecl(Id(main),Instance,[],Block([]))])])", 127))
    def test_128(self):
        self.assertTrue(TestAST.test("""
        Class Single {
            A(a: Int) {
                Return a;
            }
            B(b:String) {
                If(b +. "String" == "abcString") {
                    Break;
                }
            }
        }""", "Program([ClassDecl(Id(Single),[MethodDecl(Id(A),Instance,[param(Id(a),IntType)],Block([Return(Id(a))])),MethodDecl(Id(B),Instance,[param(Id(b),StringType)],Block([If(BinaryOp(+.,Id(b),BinaryOp(==,StringLit(String),StringLit(abcString))),Block([Break]))]))])])", 128))
    def test_129(self):
        self.assertTrue(TestAST.test("""Class x { }""", "Program([ClassDecl(Id(x),[])])", 129))
    def test_130(self):
        self.assertTrue(TestAST.test(""" Class X: Y{ }""", "Program([ClassDecl(Id(X),Id(Y),[])])", 130))
    def test_131(self):
        self.assertTrue(TestAST.test("""
        Class One {
            Main() {
                Var a, b: Int;
                a = b + 1.00e-0004 * 0x200;
            }
        }""", "Program([ClassDecl(Id(One),[MethodDecl(Id(Main),Instance,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),AssignStmt(Id(a),BinaryOp(+,Id(b),BinaryOp(*,FloatLit(0.0001),IntLit(512))))]))])])", 131))
    def test_132(self):
        self.assertTrue(TestAST.test("""
        Class Single {
            $static() {
                Self.x = Self.y + Shape::$X().Y();
            }
        }""", "Program([ClassDecl(Id(Single),[MethodDecl(Id($static),Static,[],Block([AssignStmt(FieldAccess(Self(),Id(x)),BinaryOp(+,FieldAccess(Self(),Id(y)),CallExpr(CallExpr(Id(Shape),Id($X),[]),Id(Y),[])))]))])])", 132))
    def test_133(self):
        self.assertTrue(TestAST.test("""
        Class Single {
            Destructor() {
            }
        }""", "Program([ClassDecl(Id(Single),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])", 133))
    def test_134(self):
        self.assertTrue(TestAST.test("""
        Class Single {
            $static() {
                Self.x = (1+2).y() + New X(a,b).Y(Shape::$x);
            }
        }""", "Program([ClassDecl(Id(Single),[MethodDecl(Id($static),Static,[],Block([AssignStmt(FieldAccess(Self(),Id(x)),BinaryOp(+,CallExpr(BinaryOp(+,IntLit(1),IntLit(2)),Id(y),[]),CallExpr(NewExpr(Id(X),[Id(a),Id(b)]),Id(Y),[FieldAccess(Id(Shape),Id($x))])))]))])])", 134))
    def test_135(self):
        self.assertTrue(TestAST.test("""
        Class Double {
             Name() {
                Val a: Int = 1;
            }
        }""", "Program([ClassDecl(Id(Double),[MethodDecl(Id(Name),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(1))]))])])", 135))
    def test_136(self):
        self.assertTrue(TestAST.test("""
        Class Single {
            $static() {
                Var r: Float;
                r = 123_34.e-10;
                r = r*s*Self.x;
                a[0][0] = r + Self.y;
            }
        }""", "Program([ClassDecl(Id(Single),[MethodDecl(Id($static),Static,[],Block([VarDecl(Id(r),FloatType),AssignStmt(Id(r),FloatLit(1.2334e-06)),AssignStmt(Id(r),BinaryOp(*,BinaryOp(*,Id(r),Id(s)),FieldAccess(Self(),Id(x)))),AssignStmt(ArrayCell(Id(a),[IntLit(0),IntLit(0)]),BinaryOp(+,Id(r),FieldAccess(Self(),Id(y))))]))])])", 136))
    def test_137(self):
        self.assertTrue(TestAST.test("""
        Class Single {
            $static() {
            }
        }""", "Program([ClassDecl(Id(Single),[MethodDecl(Id($static),Static,[],Block([]))])])", 137))
    def test_138(self):
        self.assertTrue(TestAST.test("""
        Class Single {
            get(a: String) {
                If(Self.compare(a, "String") == 0) {
                    Continue;
                }
                Else {
                    Return A::$x + A::$y;
                }
            }
        }""", "Program([ClassDecl(Id(Single),[MethodDecl(Id(get),Instance,[param(Id(a),StringType)],Block([If(BinaryOp(==,CallExpr(Self(),Id(compare),[Id(a),StringLit(String)]),IntLit(0)),Block([Continue]),Block([Return(BinaryOp(+,FieldAccess(Id(A),Id($x)),FieldAccess(Id(A),Id($y))))]))]))])])", 138))
    def test_139(self):
        self.assertTrue(TestAST.test("""
        Class A {
            $static() {
                Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(arr[i][i+2*i - 2]);
                }
            }
        }""", "Program([ClassDecl(Id(A),[MethodDecl(Id($static),Static,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(i),BinaryOp(-,BinaryOp(+,Id(i),BinaryOp(*,IntLit(2),Id(i))),IntLit(2))])])])])]))])])", 139))
    def test_140(self):
        self.assertTrue(TestAST.test("""
        Class A {
            Val $x, $y: Int = 1 + _.foo(1,4), 0;
            method() {
               Val x: String = "a\\\\";
               Return x + Self.str(S::$x) + Self.str(S::$y); 
            }
        }""", "Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($x),IntType,BinaryOp(+,IntLit(1),CallExpr(Id(_),Id(foo),[IntLit(1),IntLit(4)])))),AttributeDecl(Static,ConstDecl(Id($y),IntType,IntLit(0))),MethodDecl(Id(method),Instance,[],Block([ConstDecl(Id(x),StringType,StringLit(a\\\\)),Return(BinaryOp(+,BinaryOp(+,Id(x),CallExpr(Self(),Id(str),[FieldAccess(Id(S),Id($x))])),CallExpr(Self(),Id(str),[FieldAccess(Id(S),Id($y))])))]))])])", 140))
    def test_141(self):
        self.assertTrue(TestAST.test("""
        Class A {
            $static() {
                X.foo(A.value);
            }
        }""", "Program([ClassDecl(Id(A),[MethodDecl(Id($static),Static,[],Block([Call(Id(X),Id(foo),[FieldAccess(Id(A),Id(value))])]))])])", 141))
    def test_142(self):
        self.assertTrue(TestAST.test("""
        Class A {
            $name() {
                Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(i);
                }
            }
        }""", "Program([ClassDecl(Id(A),[MethodDecl(Id($name),Static,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]))])])", 142))
    def test_143(self):
        self.assertTrue(TestAST.test("""
        Class A {
            static(a: Int; b: String) {
            }
        }""", "Program([ClassDecl(Id(A),[MethodDecl(Id(static),Instance,[param(Id(a),IntType),param(Id(b),StringType)],Block([]))])])", 143))
    def test_144(self):
        self.assertTrue(TestAST.test("""
        Class A {
            float() {
                Break;
            }
        }""", "Program([ClassDecl(Id(A),[MethodDecl(Id(float),Instance,[],Block([Break]))])])", 144))
    def test_145(self):
        self.assertTrue(TestAST.test("""
        Class A {
            Val x: Array[Int, 2] = Array(1,2);
            method(a: Int) {
                If(Self.x[a + 2] <= 100) {
                    Self.x = Self.get()[(a+2)*5];
                }
            }
        }""", "Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(x),ArrayType(2,IntType),[IntLit(1),IntLit(2)])),MethodDecl(Id(method),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(<=,ArrayCell(FieldAccess(Self(),Id(x)),[BinaryOp(+,Id(a),IntLit(2))]),IntLit(100)),Block([AssignStmt(FieldAccess(Self(),Id(x)),ArrayCell(CallExpr(Self(),Id(get),[]),[BinaryOp(*,BinaryOp(+,Id(a),IntLit(2)),IntLit(5))]))]))]))])])", 145))
    def test_146(self):
        self.assertTrue(TestAST.test("""
        Class A {
            Constructor() {}
            Constructor() {}
            Destructor() {}
            Destructor() {}
        }""", "Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])", 146))
    def test_147(self):
        self.assertTrue(TestAST.test("""
        Class A {
            Constructor() {
                Self.x[(Self.y[x+3]).getFoo()] = 1 + 4;
            }
            Destructor() { 
                Return False;
            }
        }""", "Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(x)),[CallExpr(ArrayCell(FieldAccess(Self(),Id(y)),[BinaryOp(+,Id(x),IntLit(3))]),Id(getFoo),[])]),BinaryOp(+,IntLit(1),IntLit(4)))])),MethodDecl(Id(Destructor),Instance,[],Block([Return(BooleanLit(False))]))])])", 147))
    def test_148(self):
        self.assertTrue(TestAST.test("""
        Class A {
            Constructor() {
                Return Self + Self;
            }
            Destructor() { }
        }""", "Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[],Block([Return(BinaryOp(+,Self(),Self()))])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])", 148))
    def test_149(self):
        self.assertTrue(TestAST.test("""
        Class X {
            main(foo: Array[Array[String, 5], 2]) {
                If(foo[0][2] == 1 + 3) {
                    Return foo[x+ Self.y];
                }
                Elseif(!foo) {
                    foo[0][1] = -45.e-10;
                } 
            }
        }""", "Program([ClassDecl(Id(X),[MethodDecl(Id(main),Instance,[param(Id(foo),ArrayType(2,ArrayType(5,StringType)))],Block([If(BinaryOp(==,ArrayCell(Id(foo),[IntLit(0),IntLit(2)]),BinaryOp(+,IntLit(1),IntLit(3))),Block([Return(ArrayCell(Id(foo),[BinaryOp(+,Id(x),FieldAccess(Self(),Id(y)))]))]),If(UnaryOp(!,Id(foo)),Block([AssignStmt(ArrayCell(Id(foo),[IntLit(0),IntLit(1)]),UnaryOp(-,FloatLit(4.5e-09)))])))]))])])", 149))
    def test_150(self):
        self.assertTrue(TestAST.test("""
        Class A {
            Val x: Int = 1;
            Var $y, u: String = Self.str(1) + "abc", Self.str(x);
        }""", "Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(x),IntType,IntLit(1))),AttributeDecl(Static,VarDecl(Id($y),StringType,BinaryOp(+,CallExpr(Self(),Id(str),[IntLit(1)]),StringLit(abc)))),AttributeDecl(Instance,VarDecl(Id(u),StringType,CallExpr(Self(),Id(str),[Id(x)])))])])", 150))
    def test_151(self):
        self.assertTrue(TestAST.test("""
        Class A {
            Val x,y,z: Float;
            main() {
              x = x + 2;
            }
        }""", "Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(x),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(y),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(z),FloatType,None)),MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(x),BinaryOp(+,Id(x),IntLit(2)))]))])])", 151))
    def test_152(self):
        self.assertTrue(TestAST.test("""
        Class Name {
            Constructor(A: Int; B: String) {
                Self.x = New X(A,B);
                Return Self.x;
            }
        }""", "Program([ClassDecl(Id(Name),[MethodDecl(Id(Constructor),Instance,[param(Id(A),IntType),param(Id(B),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(x)),NewExpr(Id(X),[Id(A),Id(B)])),Return(FieldAccess(Self(),Id(x)))]))])])", 152))
    def test_153(self):
        self.assertTrue(TestAST.test("""
        Class B: A {}
        Class C: B {
            Val arr: Array[String, 2];
            method() {
                Self.arr = Array(1,2,3) + Array(4,5,6);
                Self.arr[0] = "string";
            }
        }""", "Program([ClassDecl(Id(B),Id(A),[]),ClassDecl(Id(C),Id(B),[AttributeDecl(Instance,ConstDecl(Id(arr),ArrayType(2,StringType),None)),MethodDecl(Id(method),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(arr)),BinaryOp(+,[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4),IntLit(5),IntLit(6)])),AssignStmt(ArrayCell(FieldAccess(Self(),Id(arr)),[IntLit(0)]),StringLit(string))]))])])", 153))
    def test_154(self):
        self.assertTrue(TestAST.test("""
        Class A {
            method() {
                foo = Self.get()[3+x] + Array(1,2,3);
            }
        }""", "Program([ClassDecl(Id(A),[MethodDecl(Id(method),Instance,[],Block([AssignStmt(Id(foo),BinaryOp(+,ArrayCell(CallExpr(Self(),Id(get),[]),[BinaryOp(+,IntLit(3),Id(x))]),[IntLit(1),IntLit(2),IntLit(3)]))]))])])", 154))
    def test_155(self):
        self.assertTrue(TestAST.test(""" Class A { $x() { Break; } } """,
         "Program([ClassDecl(Id(A),[MethodDecl(Id($x),Static,[],Block([Break]))])])", 155))
    def test_156(self):
        self.assertTrue(TestAST.test(""" 
        Class A {
            Var x,y: Int = 1, 2;
        } """, "Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(y),IntType,IntLit(2)))])])", 156))
    def test_157(self):
        self.assertTrue(TestAST.test("""Class A {Var u: Array[Int, 1];}""", "Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(u),ArrayType(1,IntType)))])])", 157))
    def test_158(self):
        self.assertTrue(TestAST.test(""" Class Done {method() { Return X.foo(Self.x); } }""",
         "Program([ClassDecl(Id(Done),[MethodDecl(Id(method),Instance,[],Block([Return(CallExpr(Id(X),Id(foo),[FieldAccess(Self(),Id(x))]))]))])])", 158))
    def test_159(self):
        self.assertTrue(TestAST.test("""
        Class Done {
            Val x: Boolean;
            method() {
                Return Shape::$foo();
            }
        }""", "Program([ClassDecl(Id(Done),[AttributeDecl(Instance,ConstDecl(Id(x),BoolType,None)),MethodDecl(Id(method),Instance,[],Block([Return(CallExpr(Id(Shape),Id($foo),[]))]))])])", 159))
    def test_160(self):
        self.assertTrue(TestAST.test("""
        Class Done {
            setName(a: Boolean) {
                If(a) {
                    Return (x+1).foo(a) + 2;
                }
                Elseif(!a) {
                    Continue;
                }
            }
        }""", "Program([ClassDecl(Id(Done),[MethodDecl(Id(setName),Instance,[param(Id(a),BoolType)],Block([If(Id(a),Block([Return(BinaryOp(+,CallExpr(BinaryOp(+,Id(x),IntLit(1)),Id(foo),[Id(a)]),IntLit(2)))]),If(UnaryOp(!,Id(a)),Block([Continue])))]))])])", 160))
    def test_161(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Var a: Int = (Self.x[1][2]).getName();
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,CallExpr(ArrayCell(FieldAccess(Self(),Id(x)),[IntLit(1),IntLit(2)]),Id(getName),[]))]))])])", 161))
    def test_162(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Var a: Int = Self.x[1][2][a[x+4]];
                a = a + 1_234.e-1;
                Return a;
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,ArrayCell(FieldAccess(Self(),Id(x)),[IntLit(1),IntLit(2),ArrayCell(Id(a),[BinaryOp(+,Id(x),IntLit(4))])])),AssignStmt(Id(a),BinaryOp(+,Id(a),FloatLit(123.4))),Return(Id(a))]))])])", 162))
    def test_163(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Var a: Int = Shape.getName();
                If(!Shape::$get() && !(x+3 == 10) || Self.x != "abc") {
                    Break;
                }
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,CallExpr(Id(Shape),Id(getName),[])),If(BinaryOp(!=,BinaryOp(||,BinaryOp(&&,UnaryOp(!,CallExpr(Id(Shape),Id($get),[])),UnaryOp(!,BinaryOp(==,BinaryOp(+,Id(x),IntLit(3)),IntLit(10)))),FieldAccess(Self(),Id(x))),StringLit(abc)),Block([Break]))]))])])", 163))
    def test_164(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Var a: Float = -1 - 10.e-4;
                Var b: Float = -10.e-10 + -1.e-005;
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),FloatType,BinaryOp(-,UnaryOp(-,IntLit(1)),FloatLit(0.001))),VarDecl(Id(b),FloatType,BinaryOp(+,UnaryOp(-,FloatLit(1e-09)),UnaryOp(-,FloatLit(1e-05))))]))])])", 164))
    def test_165(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Var a: Int = x % 4 == 0;
                Var b: Int = (x / 4 % 3 == 0) && (x<=3)*10;  
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,BinaryOp(==,BinaryOp(%,Id(x),IntLit(4)),IntLit(0))),VarDecl(Id(b),IntType,BinaryOp(&&,BinaryOp(==,BinaryOp(%,BinaryOp(/,Id(x),IntLit(4)),IntLit(3)),IntLit(0)),BinaryOp(*,BinaryOp(<=,Id(x),IntLit(3)),IntLit(10))))]))])])", 165))
    def test_166(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                If((Self.x <= 10.e-10) || (-X.getName().get < 0)) {
                    X = X[A[x+2*i]] % 3;
                }
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(||,BinaryOp(<=,FieldAccess(Self(),Id(x)),FloatLit(1e-09)),BinaryOp(<,UnaryOp(-,FieldAccess(CallExpr(Id(X),Id(getName),[]),Id(get))),IntLit(0))),Block([AssignStmt(Id(X),BinaryOp(%,ArrayCell(Id(X),[ArrayCell(Id(A),[BinaryOp(+,Id(x),BinaryOp(*,IntLit(2),Id(i)))])]),IntLit(3)))]))]))])])", 166))
    def test_167(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Var x, y: Int;
                Return x;
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),IntType),VarDecl(Id(y),IntType),Return(Id(x))]))])])", 167))
    def test_168(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            $_(a,b: String) {
                If(a != "String" || ((a-5)*A[x[v.getIndex(a)]] <= 10)) {
                    Continue;
                }
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id($_),Static,[param(Id(a),StringType),param(Id(b),StringType)],Block([If(BinaryOp(!=,Id(a),BinaryOp(||,StringLit(String),BinaryOp(<=,BinaryOp(*,BinaryOp(-,Id(a),IntLit(5)),ArrayCell(Id(A),[ArrayCell(Id(x),[CallExpr(Id(v),Id(getIndex),[Id(a)])])])),IntLit(10)))),Block([Continue]))]))])])", 168))
    def test_169(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            $_() {
                a = (New X(x)[1][1]).getName();
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id($_),Static,[],Block([AssignStmt(Id(a),CallExpr(ArrayCell(NewExpr(Id(X),[Id(x)]),[IntLit(1),IntLit(1)]),Id(getName),[]))]))])])", 169))
    def test_170(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Var a: Int = A::$setName();
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,CallExpr(Id(A),Id($setName),[]))]))])])", 170))
    def test_171(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Val x: Int = New X().Y().Shape;
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(x),IntType,FieldAccess(CallExpr(NewExpr(Id(X),[]),Id(Y),[]),Id(Shape)))]))])])", 171))
    def test_172(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Var a: Int = (New Shape().getClass()).Shape();
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,CallExpr(CallExpr(NewExpr(Id(Shape),[]),Id(getClass),[]),Id(Shape),[]))]))])])", 172))
    def test_173(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                x = ("abc\\n" +. "xyz\\t").Y()[1];
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(x),ArrayCell(CallExpr(BinaryOp(+.,StringLit(abc\\n),StringLit(xyz\\t)),Id(Y),[]),[IntLit(1)]))]))])])", 173))
    def test_174(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Var a: Int = (X+3).Y(Array(1,2,3,4));
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,CallExpr(BinaryOp(+,Id(X),IntLit(3)),Id(Y),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]]))]))])])", 174))
    def test_175(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Var a: Int = X::$Shape;
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,FieldAccess(Id(X),Id($Shape)))]))])])", 175))
    def test_176(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Var a: Int = no::$x + no::$y;
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,BinaryOp(+,FieldAccess(Id(no),Id($x)),FieldAccess(Id(no),Id($y))))]))])])", 176))
    def test_177(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() { }
            getName() {
                Return x == 5 || (!x && x <= x - 3);
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(getName),Instance,[],Block([Return(BinaryOp(==,Id(x),BinaryOp(||,IntLit(5),BinaryOp(<=,BinaryOp(&&,UnaryOp(!,Id(x)),Id(x)),BinaryOp(-,Id(x),IntLit(3))))))]))])])", 177))
    def test_178(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                out.println("Hello World");
                x.print();
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(out),Id(println),[StringLit(Hello World)]),Call(Id(x),Id(print),[])]))])])", 178))
    def test_179(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            Constructor() {
                If(x/2/3 == 0 +. "abc") {
                    Foreach(I In 0b0 .. 0b11) {
                        Break;
                    }
                }
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([If(BinaryOp(+.,BinaryOp(==,BinaryOp(/,BinaryOp(/,Id(x),IntLit(2)),IntLit(3)),IntLit(0)),StringLit(abc)),Block([For(Id(I),IntLit(0),IntLit(3),IntLit(1),Block([Break])])]))]))])])", 179))
    def test_180(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            program() {
                Return x;
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(program),Instance,[],Block([Return(Id(x))]))])])", 180))
    def test_181(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                x = (x == 5 && (x+3) +. "abc") || (x == a[5] && y ==. "xyz");
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(x),BinaryOp(||,BinaryOp(+.,BinaryOp(==,Id(x),BinaryOp(&&,IntLit(5),BinaryOp(+,Id(x),IntLit(3)))),StringLit(abc)),BinaryOp(==.,BinaryOp(==,Id(x),BinaryOp(&&,ArrayCell(Id(a),[IntLit(5)]),Id(y))),StringLit(xyz))))]))])])", 181))
    def test_182(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Var x: Int = (x+3)*2/2 == 0 && (x.get().shape()[A[x]] != 0);
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),IntType,BinaryOp(==,BinaryOp(/,BinaryOp(*,BinaryOp(+,Id(x),IntLit(3)),IntLit(2)),IntLit(2)),BinaryOp(&&,IntLit(0),BinaryOp(!=,ArrayCell(CallExpr(CallExpr(Id(x),Id(get),[]),Id(shape),[]),[ArrayCell(Id(A),[Id(x)])]),IntLit(0)))))]))])])", 182))
    def test_183(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Val x: String = !Self.bool && !A[d[x+3]] || Shape::$name() != A.get(i);
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(x),StringType,BinaryOp(!=,BinaryOp(||,BinaryOp(&&,UnaryOp(!,FieldAccess(Self(),Id(bool))),UnaryOp(!,ArrayCell(Id(A),[ArrayCell(Id(d),[BinaryOp(+,Id(x),IntLit(3))])]))),CallExpr(Id(Shape),Id($name),[])),CallExpr(Id(A),Id(get),[Id(i)])))]))])])", 183))
    def test_184(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Val temp: Boolean = 
                !New X(a,b).getCheck() && New Y().get(!a + b);
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(temp),BoolType,BinaryOp(&&,UnaryOp(!,CallExpr(NewExpr(Id(X),[Id(a),Id(b)]),Id(getCheck),[])),CallExpr(NewExpr(Id(Y),[]),Id(get),[BinaryOp(+,UnaryOp(!,Id(a)),Id(b))])))]))])])", 184))
    def test_185(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Var x: Array[Int, 5] = Array(x+3, !getName.X(), -x-5+3, 1);
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),ArrayType(5,IntType),[BinaryOp(+,Id(x),IntLit(3)),UnaryOp(!,CallExpr(Id(getName),Id(X),[])),BinaryOp(+,BinaryOp(-,UnaryOp(-,Id(x)),IntLit(5)),IntLit(3)),IntLit(1)])]))])])", 185))
    def test_186(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                Var x: Array[String, 2] = 
                Array("abc" +. "xyz", x+3 != !(x-5));
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),ArrayType(2,StringType),[BinaryOp(+.,StringLit(abc),StringLit(xyz)),BinaryOp(!=,BinaryOp(+,Id(x),IntLit(3)),UnaryOp(!,BinaryOp(-,Id(x),IntLit(5))))])]))])])", 186))
    def test_187(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                If(Array(1,2,3) == Array(x+3, !A[x[2]])) {
                    Out.println("\\n");
                }
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,[IntLit(1),IntLit(2),IntLit(3)],[BinaryOp(+,Id(x),IntLit(3)),UnaryOp(!,ArrayCell(Id(A),[ArrayCell(Id(x),[IntLit(2)])]))]),Block([Call(Id(Out),Id(println),[StringLit(\\n)])]))]))])])", 187))
    def test_188(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            main() {
                If(Array(Array(1,2,3), Array(4,5,6)) != (Array(1,2,3))) {
                    Break;
                    Out.raise("error");
                }
            }
        }
        """, "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(!=,[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4),IntLit(5),IntLit(6)]],[IntLit(1),IntLit(2),IntLit(3)]),Block([Break,Call(Id(Out),Id(raise),[StringLit(error)])]))]))])])", 188))
    def test_189(self):
        self.assertTrue(TestAST.test("""
        Class Program {
            Val x: Int = (("abc" +. "xyz") ==. "abcxyz") || (x == 4 && !x);
        }
        """, "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(x),IntType,BinaryOp(||,BinaryOp(==.,BinaryOp(+.,StringLit(abc),StringLit(xyz)),StringLit(abcxyz)),BinaryOp(==,Id(x),BinaryOp(&&,IntLit(4),UnaryOp(!,Id(x)))))))])])", 189))
    def test_190(self):
        self.assertTrue(TestAST.test("""
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
        """, "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getName),Static,[],Block([Return(Id(name))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),ClassType(Id(Shape)),NewExpr(Id(Shape),[])),VarDecl(Id(y),ClassType(Id(Shape)),NullLiteral())]))])])", 190))
    def test_191(self):
        self.assertTrue(TestAST.test("""
        Class A { Val v, $x: Int; }
        Class Shape {
            $getName(a,b: A) {
                A::$x = a.v + b.v;
            }
        }
        """, "Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(v),IntType,None)),AttributeDecl(Static,ConstDecl(Id($x),IntType,None))]),ClassDecl(Id(Shape),[MethodDecl(Id($getName),Static,[param(Id(a),ClassType(Id(A))),param(Id(b),ClassType(Id(A)))],Block([AssignStmt(FieldAccess(Id(A),Id($x)),BinaryOp(+,FieldAccess(Id(a),Id(v)),FieldAccess(Id(b),Id(v))))]))])])", 191))
    def test_192(self):
        self.assertTrue(TestAST.test("""
        Class Shape {
            $getName(a,b: Shape; x,y: Rectangle) {
                Return New X() + New Y() - New Z().get();
            }
        }
        """, "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getName),Static,[param(Id(a),ClassType(Id(Shape))),param(Id(b),ClassType(Id(Shape))),param(Id(x),ClassType(Id(Rectangle))),param(Id(y),ClassType(Id(Rectangle)))],Block([Return(BinaryOp(-,BinaryOp(+,NewExpr(Id(X),[]),NewExpr(Id(Y),[])),CallExpr(NewExpr(Id(Z),[]),Id(get),[])))]))])])", 192))
    def test_193(self):
        self.assertTrue(TestAST.test("""
        Class Shape {
            $getName(a: A) {
                A::$x = (A::$x == 0) || (A::$x != 2);
            }
        }
        """, "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getName),Static,[param(Id(a),ClassType(Id(A)))],Block([AssignStmt(FieldAccess(Id(A),Id($x)),BinaryOp(||,BinaryOp(==,FieldAccess(Id(A),Id($x)),IntLit(0)),BinaryOp(!=,FieldAccess(Id(A),Id($x)),IntLit(2))))]))])])", 193))
    def test_194(self):
        self.assertTrue(TestAST.test("""
        Class Shape {
            Val x, $y: Rectangle = Null, Null;
            main() {
                If(x == Null && (Shape::$y != Null)) {
                    Return x;
                }
            }
        }
        """, "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,ConstDecl(Id(x),ClassType(Id(Rectangle)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($y),ClassType(Id(Rectangle)),NullLiteral())),MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(==,Id(x),BinaryOp(&&,NullLiteral(),BinaryOp(!=,FieldAccess(Id(Shape),Id($y)),NullLiteral()))),Block([Return(Id(x))]))]))])])", 194))
    def test_195(self):
        self.assertTrue(TestAST.test("""
        Class Shape {
            $getName(a,b,d: Int; c,f: Shape) {
                (a[2])[2] = 1;
                a[2][2] = 2;
                X.getFoo().getName();
            }
        }
        """, "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getName),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(d),IntType),param(Id(c),ClassType(Id(Shape))),param(Id(f),ClassType(Id(Shape)))],Block([AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(2)]),[IntLit(2)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(2),IntLit(2)]),IntLit(2)),Call(CallExpr(Id(X),Id(getFoo),[]),Id(getName),[])]))])])", 195))
    def test_196(self):
        self.assertTrue(TestAST.test("""
        Class Shape: X {
            _() {
                If(!x && !(x+3)*2) {
                    (Shape::$x == 1).X=3;
                }
            }
        }
        """, "Program([ClassDecl(Id(Shape),Id(X),[MethodDecl(Id(_),Instance,[],Block([If(BinaryOp(&&,UnaryOp(!,Id(x)),BinaryOp(*,UnaryOp(!,BinaryOp(+,Id(x),IntLit(3))),IntLit(2))),Block([AssignStmt(FieldAccess(BinaryOp(==,FieldAccess(Id(Shape),Id($x)),IntLit(1)),Id(X)),IntLit(3))]))]))])])", 196))
    def test_197(self):
        self.assertTrue(TestAST.test("""
        Class Shape {
            main() {
              Shape::$x = a + b;
            }
        }
        """, "Program([ClassDecl(Id(Shape),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(FieldAccess(Id(Shape),Id($x)),BinaryOp(+,Id(a),Id(b)))]))])])", 197))
    def test_198(self):
        self.assertTrue(TestAST.test("""
        Class Shape {
            $getName() {
                Out.print();
            }
        }
        """, "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getName),Static,[],Block([Call(Id(Out),Id(print),[])]))])])", 198))
    def test_199(self):
        self.assertTrue(TestAST.test("""
        Class Shape {
            Val x, y: X ;
            getName() {
                v = x.get() == y.get();
            }
        }
        """, "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,ConstDecl(Id(x),ClassType(Id(X)),None)),AttributeDecl(Instance,ConstDecl(Id(y),ClassType(Id(X)),None)),MethodDecl(Id(getName),Instance,[],Block([AssignStmt(Id(v),BinaryOp(==,CallExpr(Id(x),Id(get),[]),CallExpr(Id(y),Id(get),[])))]))])])", 199))
    def test_200(self):
        self.assertTrue(TestAST.test("""
        Class Shape {
            $getName() {
                Var x: Shape;
                Val y: Star;
                Foreach(Y In 100 .. 200) {
                   
                }
            }
        }
        """, "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getName),Static,[],Block([VarDecl(Id(x),ClassType(Id(Shape)),NullLiteral()),ConstDecl(Id(y),ClassType(Id(Star)),None),For(Id(Y),IntLit(100),IntLit(200),IntLit(1),Block([])])]))])])", 200)) 

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
        expect = "Program([ClassDecl(Id(Pro),Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id(getNumOfShape),Instance,[],Block([For(Id(i),BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),BinaryOp(-,IntLit(3),BinaryOp(/,IntLit(5),IntLit(2))),IntLit(2),Block([Call(Id(System),Id(getName),[IntLit(1),Id(a)]),Call(FieldAccess(FieldAccess(CallExpr(FieldAccess(CallExpr(Id(X),Id(getName),[Id(a)]),Id(get)),Id(foo),[IntLit(1),IntLit(2)]),Id(Call)),Id(by)),Id(reset),[]),If(BinaryOp(==,Id(i),IntLit(3)),Block([]),If(BinaryOp(!=,Id(i),IntLit(1)),Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),FieldAccess(NewExpr(Id(X),[]),Id(field)))),AssignStmt(Id(b),BinaryOp(==.,BinaryOp(+.,StringLit(abc),StringLit(1312)),StringLit(string)))]),Block([Return()])))])])])),MethodDecl(Id(main),Instance,[],Block([Return(NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input,expect,220))