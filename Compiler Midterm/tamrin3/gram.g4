grammar gram;

start : (statement | compoundst)* EOF;





ifst returns [value_attr = str(), type_attr = str()]:
    IF '(' cond ')' '{' statement+ '}'
    ;
whilest returns [value_attr = str(), type_attr = str()]:
    WHILE '(' cond ')' '{' statement* '}';

statement returns [value_attr = str(), type_attr = str()]:
    ifst | assignment | whilest | compoundst | define ;

compoundst returns [value_attr = str(), type_attr = str()]:
    '{' (statement*) '}' ;



define returns [value_attr = str(), type_attr = str()]:
    (INT | BOOL) ID SC;
assignment returns [value_attr = str(), type_attr = str()]:
    INT? ID '=' INTTYPE SC
    | BOOL? ID '=' BOOLTYPE SC
    ;

cond returns [value_attr = str(), type_attr = str()]:
    BOOLTYPE
    | ID RELOP ID
    | ID RELOP INTTYPE
    | INTTYPE RELOP ID
    | INTTYPE RELOP INTTYPE
    | ID EQ BOOLTYPE
    ;


IF: 'if';
WHILE: 'while';
INT: 'int';
BOOL: 'boolean';
ID: LETTER(LETTER|DIGIT)*;



INTTYPE: ('-'?) DIGIT+;
BOOLTYPE: 'True' | 'False';
SC : ';';
WS : [ \n\r\t] -> channel(HIDDEN);
RELOP: '<' | '==' | '>';
EQ: '==';
COMMENT : '#' ~[\n\r]+ -> channel(HIDDEN) ;
fragment LETTER: [A-Za-z_];
fragment DIGIT: [0-9];
