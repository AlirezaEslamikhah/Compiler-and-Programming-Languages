grammar AssignmentStatement;

start returns [value_attr = str(), type_attr = str()]:
      prog NEWLINE* EOF ;

prog returns [value_attr = str(), type_attr = str()]:
      'program' ID NEWLINE* declaration? NEWLINE+ compoundst;

declaration returns [value_attr = str(), type_attr = str()]:
      'var' NEWLINE* (variable_declaration NEWLINE*)+ ;

variable_declaration returns [value_attr = str(), type_attr = str()]:
      ID ':' type ;

type returns [value_attr = str(), type_attr = str()]:
      'float' | 'int' | 'string';

compoundst  returns [value_attr = str(), type_attr = str()]:
      'begin' NEWLINE* (statement NEWLINE+)+ 'end' ;

statement  returns [value_attr = str(), type_attr = str()]:
//      ifst | assign | compoundst ;
      ifst | assign | compoundst | forst | whilest | switchst;

// added forst
forst returns [value_attr = str(), type_attr = str()]:
    'for' ID ':=' expr 'to' expr 'do' NEWLINE* statement ;

// added whilest
whilest returns [value_attr = str(), type_attr = str()]:
    'while' cond 'do' NEWLINE* statement ;

// added switchst
switchst returns [value_attr = str(), type_attr = str()]: // Added switchst
    'switch' expr 'case' (number | ID) ':' NEWLINE* statement
     ('case' (number | ID) ':' NEWLINE* statement)*
     'default' ':' NEWLINE* statement 'endsw';


ifst  returns [value_attr = str(), type_attr = str()]:
      'if' cond 'then' NEWLINE* statement NEWLINE*
       ('else' NEWLINE* statement)? ;

cond  returns [value_attr = str(), type_attr = str()]:
      expr '>' expr ;
//      expr ('>' | '<' | '==' | '!=' | '<=' | '>=') expr;

assign returns [value_attr = str(), type_attr = str()]:
      ID ':=' expr ;

expr returns [value_attr = str(), type_attr = str()]:
     expr '+' term        #expr_term_plus
    | expr '-' term      #expr_term_minus
    | expr RELOP term    #expr_term_relop
    | term               #term4
    ;

term returns [value_attr = str(), type_attr = str()]:
    term '*' factor      #term_fact_mutiply
    | term '/' factor    #term_fact_divide
    | factor             #factor3
    ;

factor returns [value_attr = str(), type_attr = str()]:
    '(' expr ')'      #fact_expr
    | ID              #fact_id
    | number          #fact_number
    | array           #fact_array
    ;

number returns [value_attr = str(), type_attr = str()]:
    FLOAT             #number_float
    | INT             #number_int
    ;

array returns [value_attr = str(), type_attr = str()]:
    INT_ARRAY        #array_int
    | FLOAT_ARRAY    #array_float
    | STRING_ARRAY   #array_string
    ;


/* Lexical Rules */
INT     : DIGIT+ ;

FLOAT:
    DIGIT+ '.' DIGIT*
    | '.' DIGIT+ ;

String:
        '"' (ESC|.)*? '"' ;
ID:
    LETTER(LETTER|DIGIT)* ;

ARRAY_TYPE:
    ID '[' INT ']';

INT_ARRAY:
    '[' INT (',' INT)* ']';

FLOAT_ARRAY:
    '[' FLOAT (',' FLOAT)* ']';

STRING_ARRAY:
    '[' String (',' String)* ']';


fragment
        DIGIT: [0-9] ;
fragment
        LETTER: [a-zA-Z] ;
fragment
        ESC: '\\"' | '\\\\' ;
//In ANTLR, fragment is a keyword used to define lexer rules that contribute to the creation of other lexer rules but cannot be matched directly themselves. Fragments are reusable lexer rules that can be referenced within other lexer rules.
//
//When a rule is marked as a fragment, it means that this rule is a part of other rules but won't create tokens by themselves. They are helpful for organizing and reusing common patterns in lexer rules without generating tokens independently.
//
//For instance, in the provided grammar, you can see the fragment keyword being used in rules like DIGIT, LETTER, and ESC. These rules define patterns for digits, letters, and escape sequences within strings, but they won't generate tokens directly. Instead, they are used within other lexer rules to match and construct tokens.
//
//These fragments are utilized within other lexer rules like INT, ID, and String to define the patterns for integers, identifiers, and strings respectively.

WS: [ \t\r]+ -> skip ;
NEWLINE: '\n' | '\r\n';
RELOP: '<=' | '<' ;