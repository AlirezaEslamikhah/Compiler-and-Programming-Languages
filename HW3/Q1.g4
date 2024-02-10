grammar Q1;
//lexer
IF: 'if';
WHILE: 'while';
INT: 'int';
BOOL: 'boolean';
ID: LETTER(LETTER|DIGIT)*;
INTTYPE: ('-'?) DIGIT+;
BOOLTYPE: 'True' | 'False';
WS : [ \n\r\t] -> channel(HIDDEN);
RELOP: '<' | '==' | '>';
EQ: '==';
COMMENT : '#' ~[\n\r]+ -> channel(HIDDEN) ;
fragment LETTER: [A-Za-z_];
fragment DIGIT: [0-9];



//parser
start : (statement | compoundst)* EOF;

ifst returns [value_attr = str(), type_attr = str()]:
    IF '(' condition ')' '{' statement+ '}';
whilest returns [value_attr = str(), type_attr = str()]:
    WHILE '(' condition ')' '{' statement* '}';

statement returns [value_attr = str(), type_attr = str()]:
    ifst | assignment | whilest | compoundst  ;

compoundst returns [value_attr = str(), type_attr = str()]:
    '{' (statement*) '}' ;

assignment returns [value_attr = str(), type_attr = str()]:
    INT? ID '=' INTTYPE ';'
    | BOOL? ID '=' BOOLTYPE ';'
    ;

condition returns [value_attr = str(), type_attr = str()]:
    BOOLTYPE
    | ID RELOP ID
    | ID RELOP INTTYPE
    | ID EQ BOOLTYPE
    ;