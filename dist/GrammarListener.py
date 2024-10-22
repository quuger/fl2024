# Generated from Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#start.
    def enterStart(self, ctx:GrammarParser.StartContext):
        pass

    # Exit a parse tree produced by GrammarParser#start.
    def exitStart(self, ctx:GrammarParser.StartContext):
        pass


    # Enter a parse tree produced by GrammarParser#starExpr.
    def enterStarExpr(self, ctx:GrammarParser.StarExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#starExpr.
    def exitStarExpr(self, ctx:GrammarParser.StarExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#concExpr.
    def enterConcExpr(self, ctx:GrammarParser.ConcExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#concExpr.
    def exitConcExpr(self, ctx:GrammarParser.ConcExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#atomExpr.
    def enterAtomExpr(self, ctx:GrammarParser.AtomExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#atomExpr.
    def exitAtomExpr(self, ctx:GrammarParser.AtomExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#orExpr.
    def enterOrExpr(self, ctx:GrammarParser.OrExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#orExpr.
    def exitOrExpr(self, ctx:GrammarParser.OrExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#quesExpr.
    def enterQuesExpr(self, ctx:GrammarParser.QuesExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#quesExpr.
    def exitQuesExpr(self, ctx:GrammarParser.QuesExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#plusExpr.
    def enterPlusExpr(self, ctx:GrammarParser.PlusExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#plusExpr.
    def exitPlusExpr(self, ctx:GrammarParser.PlusExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#charExpr.
    def enterCharExpr(self, ctx:GrammarParser.CharExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#charExpr.
    def exitCharExpr(self, ctx:GrammarParser.CharExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#parExpr.
    def enterParExpr(self, ctx:GrammarParser.ParExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#parExpr.
    def exitParExpr(self, ctx:GrammarParser.ParExprContext):
        pass



del GrammarParser