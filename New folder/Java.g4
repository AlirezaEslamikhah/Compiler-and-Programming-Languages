grammar Java;

start : classDeclaration+ EOF;

classDeclaration : 'class' Identifier '{' NEWLINE* fieldDeclaration NEWLINE* '}' NEWLINE* ;

fieldDeclaration : Identifier Identifier ';';

Identifier: LETTER+;

fragment DIGIT: [0-9];

fragment LETTER: [a-zA-Z];

WS: [ \t\r]+ -> skip;

NEWLINE: '\n' | '\r\n' | '\r';
