import sys,os
import subprocess
import unittest
from antlr4 import *

for path in ['./test/','./main/d96/parser/','./main/d96/utils/','./main/d96/astgen/','./main/d96/checker/','./main/d96/codegen/']:
	sys.path.append(path)
ANTLR_JAR = os.environ.get('ANTLR_JAR')
TARGET_DIR = '../target'
GENERATE_DIR = 'main/d96/parser'

def main(argv):
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        subprocess.run(["java","-jar",ANTLR_JAR,"-o","../target","-no-listener","-visitor","main/d96/parser/D96.g4"])
    elif argv[0] == 'clean':
        subprocess.run(["rm","-rf",TARGET_DIR + "/*"])
               
    elif argv[0] == 'test':     
        if not os.path.isdir(TARGET_DIR + "/" + GENERATE_DIR):
            subprocess.run(["java","-jar",ANTLR_JAR,"-o",GENERATE_DIR,"-no-listener","-visitor","main/d96/parser/D96.g4"])
        if not (TARGET_DIR + "/" + GENERATE_DIR) in sys.path:
            sys.path.append(TARGET_DIR + "/" + GENERATE_DIR)
        if len(argv) < 2:
            printUsage()
        elif argv[1] == 'LexerSuite':
            from LexerSuite import LexerSuite
            getAndTest(LexerSuite)
        elif argv[1] == 'ParserSuite':
            from ParserSuite import ParserSuite
            getAndTest(ParserSuite)
        else:
            printUsage()
    else:
        printUsage()



def getAndTest(cls): 
    suite = unittest.makeSuite(cls)
    test(suite)

def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())

def printUsage():
    print("py run.py gen")
    print("py run.py test LexerSuite")
    print("py run.py test ParserSuite")

if __name__ == "__main__":
   main(sys.argv[1:])