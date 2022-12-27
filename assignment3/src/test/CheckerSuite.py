import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        input = """
        Class Shape {
            Var h, $x: Int;
            Var k: String;
            hi(){
                Return 5;
            }
        }
        Class Rectangle: Shape{
            Val k: Int = 1 + 2;
        }
        Class Program: Shape{
            Val k: Int = 1;
            Var x: Int;
            Var class: Shape;
            Constructor(a:Int) {
                Self.x = a;
                Return;
            }
            getName(u: Int;w:Int) {
                Var b: Shape;
                b = New Shape();
                ##b = New Program(1);##
                Self.class = b;
                Self.x = Self.class.hi() + 1 + b::$x + Shape.h;
                Return;
                {
                    Var giang: Int = 5 + b.h;
                    Var arr: Array[Float, 5];
                    ##arr = Array(giang + 1, u*w, 4*giang/w , 100, 20 + 12 + w);##
                    giang = 5*u + w;
                    ##Return giang + 2;##
                }
            }
            $hello() {
                Return 100;
            }
            main() {
                Var check: String = "hehe";
                Var isBool: Boolean = True;
                Var x,y: Int = 1, 3;
                If (Self.h >= Self.k) {
                    Var arr: Array[Array[Array[Int, 3], 3], 2] = Array (
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
                    Var a: Int = 1 + Program::$hello();
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
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,400))
        