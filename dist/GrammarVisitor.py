# Generated from Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#regex.
    def visitRegex(self, ctx:GrammarParser.RegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#orExpr.
    def visitOrExpr(self, ctx:GrammarParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#concatExpr.
    def visitConcatExpr(self, ctx:GrammarParser.ConcatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#repeatExpr.
    def visitRepeatExpr(self, ctx:GrammarParser.RepeatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#charExpr.
    def visitCharExpr(self, ctx:GrammarParser.CharExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#parenExpr.
    def visitParenExpr(self, ctx:GrammarParser.ParenExprContext):
        return self.visitChildren(ctx)



del GrammarParser