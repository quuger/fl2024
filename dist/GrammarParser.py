# Generated from Grammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,
        1,1,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,2,4,2,23,8,2,11,2,12,2,24,
        1,3,1,3,1,3,1,3,3,3,31,8,3,1,4,1,4,1,4,1,4,1,4,3,4,38,8,4,1,4,0,
        0,5,0,2,4,6,8,0,0,40,0,10,1,0,0,0,2,13,1,0,0,0,4,22,1,0,0,0,6,26,
        1,0,0,0,8,37,1,0,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,
        18,3,4,2,0,14,15,5,1,0,0,15,17,3,4,2,0,16,14,1,0,0,0,17,20,1,0,0,
        0,18,16,1,0,0,0,18,19,1,0,0,0,19,3,1,0,0,0,20,18,1,0,0,0,21,23,3,
        6,3,0,22,21,1,0,0,0,23,24,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,
        5,1,0,0,0,26,30,3,8,4,0,27,31,5,2,0,0,28,31,5,3,0,0,29,31,5,4,0,
        0,30,27,1,0,0,0,30,28,1,0,0,0,30,29,1,0,0,0,30,31,1,0,0,0,31,7,1,
        0,0,0,32,38,5,7,0,0,33,34,5,5,0,0,34,35,3,2,1,0,35,36,5,6,0,0,36,
        38,1,0,0,0,37,32,1,0,0,0,37,33,1,0,0,0,38,9,1,0,0,0,4,18,24,30,37
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'*'", "'+'", "'?'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "CHAR", "WS" ]

    RULE_regex = 0
    RULE_unionExp = 1
    RULE_concatExp = 2
    RULE_repeatExp = 3
    RULE_atom = 4

    ruleNames =  [ "regex", "unionExp", "concatExp", "repeatExp", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    CHAR=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RegexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unionExp(self):
            return self.getTypedRuleContext(GrammarParser.UnionExpContext,0)


        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_regex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegex" ):
                listener.enterRegex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegex" ):
                listener.exitRegex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegex" ):
                return visitor.visitRegex(self)
            else:
                return visitor.visitChildren(self)




    def regex(self):

        localctx = GrammarParser.RegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_regex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.unionExp()
            self.state = 11
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnionExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_unionExp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OrExprContext(UnionExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.UnionExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def concatExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ConcatExpContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ConcatExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)



    def unionExp(self):

        localctx = GrammarParser.UnionExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_unionExp)
        self._la = 0 # Token type
        try:
            localctx = GrammarParser.OrExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.concatExp()
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 14
                self.match(GrammarParser.T__0)
                self.state = 15
                self.concatExp()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcatExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_concatExp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ConcatExprContext(ConcatExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ConcatExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def repeatExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.RepeatExpContext)
            else:
                return self.getTypedRuleContext(GrammarParser.RepeatExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatExpr" ):
                listener.enterConcatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatExpr" ):
                listener.exitConcatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatExpr" ):
                return visitor.visitConcatExpr(self)
            else:
                return visitor.visitChildren(self)



    def concatExp(self):

        localctx = GrammarParser.ConcatExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_concatExp)
        self._la = 0 # Token type
        try:
            localctx = GrammarParser.ConcatExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self.repeatExp()
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_repeatExp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RepeatExprContext(RepeatExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.RepeatExpContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(GrammarParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeatExpr" ):
                listener.enterRepeatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeatExpr" ):
                listener.exitRepeatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeatExpr" ):
                return visitor.visitRepeatExpr(self)
            else:
                return visitor.visitChildren(self)



    def repeatExp(self):

        localctx = GrammarParser.RepeatExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_repeatExp)
        try:
            localctx = GrammarParser.RepeatExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.atom()
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 27
                localctx.op = self.match(GrammarParser.T__1)
                pass
            elif token in [3]:
                self.state = 28
                localctx.op = self.match(GrammarParser.T__2)
                pass
            elif token in [4]:
                self.state = 29
                localctx.op = self.match(GrammarParser.T__3)
                pass
            elif token in [-1, 1, 5, 6, 7]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CharExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(GrammarParser.CHAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharExpr" ):
                listener.enterCharExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharExpr" ):
                listener.exitCharExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharExpr" ):
                return visitor.visitCharExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unionExp(self):
            return self.getTypedRuleContext(GrammarParser.UnionExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = GrammarParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = GrammarParser.CharExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(GrammarParser.CHAR)
                pass
            elif token in [5]:
                localctx = GrammarParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(GrammarParser.T__4)
                self.state = 34
                self.unionExp()
                self.state = 35
                self.match(GrammarParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





