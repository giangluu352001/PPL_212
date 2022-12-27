grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
program: STRING+;
STRING
 : '"' (ESC | ~ ["\\])* '"' {
	self.text = self.text[1:-1]
};
fragment ESC
 : '\\' (["\\/bfnrt] | UNICODE)
 ;
fragment UNICODE
 : 'u' HEX HEX HEX HEX
 ;
fragment HEX
 : [0-9a-fA-F]
 ;
WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};