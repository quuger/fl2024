# Generated from Calculantlr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculantlrParser import CalculantlrParser
else:
    from CalculantlrParser import CalculantlrParser

# This class defines a complete listener for a parse tree produced by CalculantlrParser.
class CalculantlrListener(ParseTreeListener):

    # Enter a parse tree produced by CalculantlrParser#AtomExpr.
    def enterAtomExpr(self, ctx:CalculantlrParser.AtomExprContext):
        pass

    # Exit a parse tree produced by CalculantlrParser#AtomExpr.
    def exitAtomExpr(self, ctx:CalculantlrParser.AtomExprContext):
        pass


    # Enter a parse tree produced by CalculantlrParser#ParenExpr.
    def enterParenExpr(self, ctx:CalculantlrParser.ParenExprContext):
        pass

    # Exit a parse tree produced by CalculantlrParser#ParenExpr.
    def exitParenExpr(self, ctx:CalculantlrParser.ParenExprContext):
        pass


    # Enter a parse tree produced by CalculantlrParser#OpExpr.
    def enterOpExpr(self, ctx:CalculantlrParser.OpExprContext):
        pass

    # Exit a parse tree produced by CalculantlrParser#OpExpr.
    def exitOpExpr(self, ctx:CalculantlrParser.OpExprContext):
        pass



del CalculantlrParser