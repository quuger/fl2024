grammar Grammar;

regex: unionExp EOF;

unionExp
    : concatExp ('|' concatExp)*    # orExpr
    ;

concatExp
    : repeatExp+                    # concatExpr
    ;

repeatExp
: atom (op='*' | op='+' | op='?')?           # repeatExpr
    ;

atom
    : CHAR                          # charExpr
    | '(' unionExp ')'              # parenExpr
    ;

CHAR: [a-zA-Z0-9];

WS: [ \t\r\n]+ -> skip;


//    0 split 1 5
//    1 split 2 4
//    2 char a
//    3 jmp 1
//    4 jmp 8
//    5 split 6 8
//    6 char b
//    7 jmp 5
//    8 split 0 9
//    9 match