import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        input = """Class X {
            Val a: Int = 5;
        }"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))