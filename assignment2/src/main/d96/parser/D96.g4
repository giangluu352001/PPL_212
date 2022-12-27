// MSSV: 1913186

grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: classname+ EOF;

// 3.0 Fragments
fragment LOWER: [a-z];
fragment UPPER: [A-Z];
fragment LETTER: LOWER | UPPER;
fragment DIGIT: [0-9];
fragment ESCAPE: '\\' [bfnrt'\\] ;
fragment CHAR:  '\'' '"' | ESCAPE | ~[\b\t\r\f\n\\"];
fragment EXP: [Ee] [+-]? DIGIT+;
fragment HEX: '0' [Xx] ('0' | [1-9A-F] [0-9A-F]* ('_' [0-9A-F]+)*);
fragment OCT: '0' ('0' | [1-7] [0-7]* ('_' [0-7]+)*);
fragment BIN: '0' [Bb] ('0' | [1] [01]* ('_' [01]+)*);
fragment DEC: [1-9] DIGIT* ('_' DIGIT+)* | '0';
fragment DOLLAR: '$';

// 6.1 Statements
statement: lhs | ifstatement | forstatement | returnstatement |
invokemethod | continuestatement | breakstatement | vardecl | blockstatement;

// 6.2 Assignment statement
lhs: (scalavar | exp8 indexop+) ASSIGN exp SEMI;
scalavar: ID | exp8 DOT ID | ID TWOCOLON DOLLAR_ID;

// 6.3 If statement
ifstatement: IF LB exp RB blockstatement 
	(ELSEIF LB exp RB blockstatement)* (ELSE blockstatement)?;

//6.4 For/In statement
forstatement: FOREACHTYPE LB scalavar 
INKEY exp DOTDOT exp (BYKEY exp)? RB blockstatement;

// 6.5 Break statement
breakstatement: BREAKTYPE SEMI;

// 6.6 Continue statement
continuestatement: CONTINUETYPE SEMI;

// 6.7 Return statement
returnstatement: RETURNTYPE exp? SEMI;

// 6.8 Method Invocation statement
invokemethod: (exp9 partinvoke* DOT ID paramexp | ID TWOCOLON DOLLAR_ID paramexp) SEMI;
partinvoke: DOT ID paramexp?;

// 6.9 Block statement
blockstatement: LP statement* RP;

// 5.0 Expressions
exp: exp1 (CONCATENATION | STRINGEQUAL) exp1 | exp1;
exp1: exp2 (EQUAL | NOTEQUAL | LESS | GREATER | LESSEQUAL | GREATEREQUAL) exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUB) exp4 | exp4;
exp4: exp4 (MUL | DIV | MOD) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: SUB exp6 | exp7;
exp7: exp7 indexop+ | exp8;
exp8: exp8 DOT ID paramexp? | exp9;
exp9: ID TWOCOLON DOLLAR_ID paramexp? | exp10;
exp10: NEW ID paramexp | operands;

operands: value | SELFTYPE | NULLTYPE | ID | LB exp RB; 

paramexp: LB explist? RB;
indexop: LSB exp RSB;

// class definition 
classname: CLASSTYPE ID (COLON ID)? LP memclass* RP;
memclass: method | attr | construct | destruct;
construct: CONSTRUCTORTYPE LB parameters? RB blockstatement;
destruct: DESTRUCTORTYPE LB RB blockstatement;

// 2.3 Method declaration
method: (DOLLAR_ID | ID) LB parameters? RB blockstatement;
parameters: idlist COLON datatype (SEMI idlist COLON datatype)*;
idlist: ID (COMMA ID)*;

// 2.2 Attribute declaration
attr
locals [lst = []]
@init {$attr::lst = [0,0,0]}
: (VARTYPE | CONSTTYPE) idattr (COMMA {$attr::lst[0] += 1} idattr)*
	 COLON datatype (ASSIGN {$attr::lst[1] = 1} exp ( {$attr::lst[2] < $attr::lst[0]}? COMMA {$attr::lst[2] += 1} exp)*)?
	 ({$attr::lst[0] == $attr::lst[2] and $attr::lst[1] == 1}? SEMI | {$attr::lst[1] == 0}? SEMI);
idattr: DOLLAR_ID | ID;

vardecl
locals [lst = []]
@init {$vardecl::lst = [0,0,0]}
: (VARTYPE | CONSTTYPE) ID (COMMA {$vardecl::lst[0] += 1} ID)*
	 COLON datatype (ASSIGN {$vardecl::lst[1] = 1} exp ( {$vardecl::lst[2] < $vardecl::lst[0]}? COMMA {$vardecl::lst[2] += 1} exp)*)?
	 ({$vardecl::lst[0] == $vardecl::lst[2] and $vardecl::lst[1] == 1}? SEMI | {$vardecl::lst[1] == 0}? SEMI);
 
// 5.6 Member access
explist: exp (COMMA exp)*; 

// 3.3 Identifiers
datatype: INTTYPE | BOOLEANTYPE | FLOATTYPE | arraynested | STRINGTYPE | ID ;

//Create array
arraynested: ARRAYTYPE LSB (arraynested | INTTYPE | BOOLEANTYPE | FLOATTYPE | STRINGTYPE)
 COMMA {self._input.LT(1).text not in ["0", "00", "0x0", "0b0", "0X0", "0B0"]}? INT RSB;

//Create multi-dimensional arrays
multiarrayindex: ARRAYTYPE LB indexlist? RB;
arrayindex: ARRAYTYPE paramexp;
indexlist: arrayindex (COMMA arrayindex)*;

// 3.7 Literals
value: INT | FLOAT | booln | STRING | arrayindex | multiarrayindex;

//Create boolean
booln: TRUETYPE | FALSETYPE;

// Create integer number
INT: (OCT | HEX | BIN | DEC) {
	self.text = self.text.replace("_", "")
};

// Create float number
FLOAT: (DEC DOT DIGIT* EXP? | DEC DOT DIGIT+ EXP? 
| DEC? DOT DIGIT* EXP | DEC EXP) {
	self.text = self.text.replace("_", "")
};

//Create string
STRING: '"' CHAR* '"' {
	self.text = self.text[1:-1]
};

// 3.2 Program comment
COMMENT: '##' .*? '##' -> skip;
 
// 3.4 Keywords
BREAKTYPE: 'Break';
FOREACHTYPE: 'Foreach';
BOOLEANTYPE: 'Boolean';
NULLTYPE: 'Null';
CONTINUETYPE: 'Continue';
TRUETYPE: 'True';
STRINGTYPE: 'String';
IF: 'If';
FALSETYPE: 'False';
ELSEIF: 'Elseif';
ARRAYTYPE: 'Array';
INTTYPE: 'Int';
ELSE: 'Else';
FLOATTYPE: 'Float';
VARTYPE: 'Var';
CONSTTYPE: 'Val';
RETURNTYPE: 'Return';
NEW: 'New';
INKEY: 'In';
BYKEY: 'By';
CLASSTYPE: 'Class';
CONSTRUCTORTYPE: 'Constructor';
DESTRUCTORTYPE: 'Destructor';
SELFTYPE: 'Self';

// 3.5 Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
OR: '||';
AND: '&&';
EQUAL: '==';
NOTEQUAL: '!=';
LESS: '<';
GREATER: '>';
LESSEQUAL: '<=';
GREATEREQUAL: '>=';
ASSIGN: '=';
STRINGEQUAL: '==.';
CONCATENATION: '+.';
DOTDOT: '..';
DOT: '.';

// 3.6 Seperators
LB: '(';
RB: ')';
LP: '{';
RP: '}';
SEMI: ';';
LSB: '[';
RSB: ']';
TWOCOLON: '::';
COLON: ':';
COMMA: ',';

// 3.1 Characters set
DOLLAR_ID: DOLLAR (LETTER | '_' | DIGIT)+;
ID: (LETTER | '_') (LETTER | '_' | DIGIT)*;
WS: [ \t\r\n\f\b]+ -> skip; // skip spaces, tabs, newlines

// error definition
UNCLOSE_STRING: '"' CHAR* ([\b\t\n\f\r\\"] | EOF) {
	if str(self.text)[-1] in ['\b', '\t', '\n', '\f', '\r', '"', '\\']:
		raise UncloseString(str(self.text)[1:-1])
	else:	raise UncloseString(str(self.text)[1:])
};
ILLEGAL_ESCAPE: '"' CHAR* ('\\' ~[btnfr'\\]) { 
	raise IllegalEscape(self.text[1:])
};
ERROR_TOKEN: . {
	raise ErrorToken(self.text)
};
