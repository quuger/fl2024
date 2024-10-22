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
