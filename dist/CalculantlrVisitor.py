# Generated from Calculantlr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculantlrParser import CalculantlrParser
else:
    from CalculantlrParser import CalculantlrParser

# This class defines a complete generic visitor for a parse tree produced by CalculantlrParser.

class CalculantlrVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculantlrParser#AtomExpr.
    def visitAtomExpr(self, ctx:CalculantlrParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#ParenExpr.
    def visitParenExpr(self, ctx:CalculantlrParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculantlrParser#OpExpr.
    def visitOpExpr(self, ctx:CalculantlrParser.OpExprContext):
        return self.visitChildren(ctx)



del CalculantlrParser