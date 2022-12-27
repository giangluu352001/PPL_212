import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_190_string(self):
        ## test 
        input = """
        "Hello
        "
        """
        expect = "Unclosed String: Hello"
        number = 190
        self.assertTrue(TestLexer.test(input, expect, number))