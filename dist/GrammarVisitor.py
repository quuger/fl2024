# Generated from Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#start.
    def visitStart(self, ctx:GrammarParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#starExpr.
    def visitStarExpr(self, ctx:GrammarParser.StarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#concExpr.
    def visitConcExpr(self, ctx:GrammarParser.ConcExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#atomExpr.
    def visitAtomExpr(self, ctx:GrammarParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#orExpr.
    def visitOrExpr(self, ctx:GrammarParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#quesExpr.
    def visitQuesExpr(self, ctx:GrammarParser.QuesExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#plusExpr.
    def visitPlusExpr(self, ctx:GrammarParser.PlusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#charExpr.
    def visitCharExpr(self, ctx:GrammarParser.CharExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#parExpr.
    def visitParExpr(self, ctx:GrammarParser.ParExprContext):
        return self.visitChildren(ctx)



del GrammarParser