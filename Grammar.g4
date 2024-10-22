grammar Grammar;

start: word EOF;

word: left=expr '|' right=word     # orExpr
    | expr                         # exprExpr
    ;

expr:   left=expr right=expr       # concExpr
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
