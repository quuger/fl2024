# Generated from Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#regex.
    def enterRegex(self, ctx:GrammarParser.RegexContext):
        pass

    # Exit a parse tree produced by GrammarParser#regex.
    def exitRegex(self, ctx:GrammarParser.RegexContext):
        pass


    # Enter a parse tree produced by GrammarParser#orExpr.
    def enterOrExpr(self, ctx:GrammarParser.OrExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#orExpr.
    def exitOrExpr(self, ctx:GrammarParser.OrExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#concatExpr.
    def enterConcatExpr(self, ctx:GrammarParser.ConcatExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#concatExpr.
    def exitConcatExpr(self, ctx:GrammarParser.ConcatExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#repeatExpr.
    def enterRepeatExpr(self, ctx:GrammarParser.RepeatExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#repeatExpr.
    def exitRepeatExpr(self, ctx:GrammarParser.RepeatExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#charExpr.
    def enterCharExpr(self, ctx:GrammarParser.CharExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#charExpr.
    def exitCharExpr(self, ctx:GrammarParser.CharExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#parenExpr.
    def enterParenExpr(self, ctx:GrammarParser.ParenExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#parenExpr.
    def exitParenExpr(self, ctx:GrammarParser.ParenExprContext):
        pass



del GrammarParser