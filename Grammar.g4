grammar Grammar;

start: expr EOF;

expr:    left=expr '|' right=expr   # orExpr
    |   left=expr right=expr       # concExpr
    |   atom '?'                   # quesExpr
    |   atom '*'                   # starExpr
    |   atom '+'                   # plusExpr
    |   atom                       # atomExpr
    ;
atom: CHAR                         # charExpr
    | '(' expr ')'                 # parExpr
    ;

CHAR: [a-zA-Z];
WS: [\t\r\n]+ -> skip;