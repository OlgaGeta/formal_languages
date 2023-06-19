# Generated from grammatica.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("w\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\2\5\2&\n\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3-\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\5\fU\n\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\2\2\21\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36\2\2\2q\2%\3\2\2\2\4,\3\2\2\2\6.\3\2")
        buf.write("\2\2\b\64\3\2\2\2\n\67\3\2\2\2\f>\3\2\2\2\16A\3\2\2\2")
        buf.write("\20F\3\2\2\2\22J\3\2\2\2\24L\3\2\2\2\26T\3\2\2\2\30V\3")
        buf.write("\2\2\2\32a\3\2\2\2\34l\3\2\2\2\36t\3\2\2\2 &\5\4\3\2!")
        buf.write("&\5\22\n\2\"&\5\26\f\2#&\7\30\2\2$&\7\27\2\2% \3\2\2\2")
        buf.write("%!\3\2\2\2%\"\3\2\2\2%#\3\2\2\2%$\3\2\2\2&\3\3\2\2\2\'")
        buf.write("-\5\6\4\2(-\5\b\5\2)-\5\n\6\2*-\5\f\7\2+-\5\16\b\2,\'")
        buf.write("\3\2\2\2,(\3\2\2\2,)\3\2\2\2,*\3\2\2\2,+\3\2\2\2-\5\3")
        buf.write("\2\2\2./\7\3\2\2/\60\5\2\2\2\60\61\7\4\2\2\61\62\5\20")
        buf.write("\t\2\62\63\7\5\2\2\63\7\3\2\2\2\64\65\7\6\2\2\65\66\5")
        buf.write("\2\2\2\66\t\3\2\2\2\678\7\7\2\289\5\2\2\29:\7\b\2\2:;")
        buf.write("\7\4\2\2;<\5\20\t\2<=\7\5\2\2=\13\3\2\2\2>?\7\t\2\2?@")
        buf.write("\5\2\2\2@\r\3\2\2\2AB\7\n\2\2BC\5\2\2\2CD\7\13\2\2DE\5")
        buf.write("\2\2\2E\17\3\2\2\2FG\5\2\2\2GH\7\f\2\2HI\5\2\2\2I\21\3")
        buf.write("\2\2\2JK\5\24\13\2K\23\3\2\2\2LM\7\r\2\2MN\5\2\2\2NO\7")
        buf.write("\16\2\2OP\5\2\2\2P\25\3\2\2\2QU\5\30\r\2RU\5\32\16\2S")
        buf.write("U\5\34\17\2TQ\3\2\2\2TR\3\2\2\2TS\3\2\2\2U\27\3\2\2\2")
        buf.write("VW\7\17\2\2WX\7\20\2\2XY\5\2\2\2YZ\7\4\2\2Z[\5\36\20\2")
        buf.write("[\\\7\5\2\2\\]\7\21\2\2]^\7\4\2\2^_\5\36\20\2_`\7\5\2")
        buf.write("\2`\31\3\2\2\2ab\7\22\2\2bc\5\2\2\2cd\7\23\2\2de\5\2\2")
        buf.write("\2ef\7\24\2\2fg\5\2\2\2gh\7\25\2\2hi\5\2\2\2ij\7\24\2")
        buf.write("\2jk\5\2\2\2k\33\3\2\2\2lm\7\26\2\2mn\7\16\2\2no\5\2\2")
        buf.write("\2op\7\25\2\2pq\5\2\2\2qr\7\24\2\2rs\5\2\2\2s\35\3\2\2")
        buf.write("\2tu\5\2\2\2u\37\3\2\2\2\5%,T")
        return buf.getvalue()


class grammaticaParser ( Parser ):

    grammarFileName = "grammatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CREATE'", "'('", "')'", "'DROP'", "'ALTER'", 
                     "'ADD'", "'TRUNCATE'", "'RENAME'", "'TO'", "':'", "'SELECT'", 
                     "'FROM'", "'INSERT'", "'INTO'", "'VALUES'", "'UPDATE'", 
                     "'SET'", "'='", "'WHERE'", "'DELETE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STR", "INT", "WS" ]

    RULE_expr = 0
    RULE_ddl = 1
    RULE_create = 2
    RULE_drop = 3
    RULE_alter = 4
    RULE_truncate = 5
    RULE_rename = 6
    RULE_terminal = 7
    RULE_dql = 8
    RULE_select = 9
    RULE_sql = 10
    RULE_insert = 11
    RULE_update = 12
    RULE_delete = 13
    RULE_smallterminal = 14

    ruleNames =  [ "expr", "ddl", "create", "drop", "alter", "truncate", 
                   "rename", "terminal", "dql", "select", "sql", "insert", 
                   "update", "delete", "smallterminal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    STR=21
    INT=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammaticaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SqlExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sql(self):
            return self.getTypedRuleContext(grammaticaParser.SqlContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqlExpr" ):
                listener.enterSqlExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqlExpr" ):
                listener.exitSqlExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqlExpr" ):
                return visitor.visitSqlExpr(self)
            else:
                return visitor.visitChildren(self)


    class StrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammaticaParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def STR(self):
            return self.getToken(grammaticaParser.STR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrExpr" ):
                listener.enterStrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrExpr" ):
                listener.exitStrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrExpr" ):
                return visitor.visitStrExpr(self)
            else:
                return visitor.visitChildren(self)


    class DqlExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def dql(self):
            return self.getTypedRuleContext(grammaticaParser.DqlContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDqlExpr" ):
                listener.enterDqlExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDqlExpr" ):
                listener.exitDqlExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDqlExpr" ):
                return visitor.visitDqlExpr(self)
            else:
                return visitor.visitChildren(self)


    class DdlExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ddl(self):
            return self.getTypedRuleContext(grammaticaParser.DdlContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDdlExpr" ):
                listener.enterDdlExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDdlExpr" ):
                listener.exitDdlExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDdlExpr" ):
                return visitor.visitDdlExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a grammaticaParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(grammaticaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = grammaticaParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammaticaParser.T__0, grammaticaParser.T__3, grammaticaParser.T__4, grammaticaParser.T__6, grammaticaParser.T__7]:
                localctx = grammaticaParser.DdlExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.ddl()
                pass
            elif token in [grammaticaParser.T__10]:
                localctx = grammaticaParser.DqlExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.dql()
                pass
            elif token in [grammaticaParser.T__12, grammaticaParser.T__15, grammaticaParser.T__19]:
                localctx = grammaticaParser.SqlExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.sql()
                pass
            elif token in [grammaticaParser.INT]:
                localctx = grammaticaParser.NumberExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                localctx.atom = self.match(grammaticaParser.INT)
                pass
            elif token in [grammaticaParser.STR]:
                localctx = grammaticaParser.StrExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                localctx.atom = self.match(grammaticaParser.STR)
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


    class DdlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create(self):
            return self.getTypedRuleContext(grammaticaParser.CreateContext,0)


        def drop(self):
            return self.getTypedRuleContext(grammaticaParser.DropContext,0)


        def alter(self):
            return self.getTypedRuleContext(grammaticaParser.AlterContext,0)


        def truncate(self):
            return self.getTypedRuleContext(grammaticaParser.TruncateContext,0)


        def rename(self):
            return self.getTypedRuleContext(grammaticaParser.RenameContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_ddl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDdl" ):
                listener.enterDdl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDdl" ):
                listener.exitDdl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDdl" ):
                return visitor.visitDdl(self)
            else:
                return visitor.visitChildren(self)




    def ddl(self):

        localctx = grammaticaParser.DdlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ddl)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammaticaParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.create()
                pass
            elif token in [grammaticaParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.drop()
                pass
            elif token in [grammaticaParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.alter()
                pass
            elif token in [grammaticaParser.T__6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.truncate()
                pass
            elif token in [grammaticaParser.T__7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                self.rename()
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


    class CreateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # ExprContext
            self.pair = None # TerminalContext

        def expr(self):
            return self.getTypedRuleContext(grammaticaParser.ExprContext,0)


        def terminal(self):
            return self.getTypedRuleContext(grammaticaParser.TerminalContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate" ):
                listener.enterCreate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate" ):
                listener.exitCreate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreate" ):
                return visitor.visitCreate(self)
            else:
                return visitor.visitChildren(self)




    def create(self):

        localctx = grammaticaParser.CreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(grammaticaParser.T__0)
            self.state = 45
            localctx.name = self.expr()
            self.state = 46
            self.match(grammaticaParser.T__1)
            self.state = 47
            localctx.pair = self.terminal()
            self.state = 48
            self.match(grammaticaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(grammaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_drop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrop" ):
                listener.enterDrop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrop" ):
                listener.exitDrop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrop" ):
                return visitor.visitDrop(self)
            else:
                return visitor.visitChildren(self)




    def drop(self):

        localctx = grammaticaParser.DropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_drop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(grammaticaParser.T__3)
            self.state = 51
            localctx.name = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # ExprContext
            self.pair = None # TerminalContext

        def expr(self):
            return self.getTypedRuleContext(grammaticaParser.ExprContext,0)


        def terminal(self):
            return self.getTypedRuleContext(grammaticaParser.TerminalContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_alter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlter" ):
                listener.enterAlter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlter" ):
                listener.exitAlter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlter" ):
                return visitor.visitAlter(self)
            else:
                return visitor.visitChildren(self)




    def alter(self):

        localctx = grammaticaParser.AlterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_alter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(grammaticaParser.T__4)
            self.state = 54
            localctx.name = self.expr()
            self.state = 55
            self.match(grammaticaParser.T__5)
            self.state = 56
            self.match(grammaticaParser.T__1)
            self.state = 57
            localctx.pair = self.terminal()
            self.state = 58
            self.match(grammaticaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TruncateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(grammaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_truncate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTruncate" ):
                listener.enterTruncate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTruncate" ):
                listener.exitTruncate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTruncate" ):
                return visitor.visitTruncate(self)
            else:
                return visitor.visitChildren(self)




    def truncate(self):

        localctx = grammaticaParser.TruncateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_truncate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(grammaticaParser.T__6)
            self.state = 61
            localctx.name = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RenameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.oldname = None # ExprContext
            self.newname = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammaticaParser.ExprContext,i)


        def getRuleIndex(self):
            return grammaticaParser.RULE_rename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRename" ):
                listener.enterRename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRename" ):
                listener.exitRename(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRename" ):
                return visitor.visitRename(self)
            else:
                return visitor.visitChildren(self)




    def rename(self):

        localctx = grammaticaParser.RenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(grammaticaParser.T__7)
            self.state = 64
            localctx.oldname = self.expr()
            self.state = 65
            self.match(grammaticaParser.T__8)
            self.state = 66
            localctx.newname = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExprContext
            self.value = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammaticaParser.ExprContext,i)


        def getRuleIndex(self):
            return grammaticaParser.RULE_terminal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal" ):
                listener.enterTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal" ):
                listener.exitTerminal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal" ):
                return visitor.visitTerminal(self)
            else:
                return visitor.visitChildren(self)




    def terminal(self):

        localctx = grammaticaParser.TerminalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_terminal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            localctx.key = self.expr()
            self.state = 69
            self.match(grammaticaParser.T__9)
            self.state = 70
            localctx.value = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DqlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select(self):
            return self.getTypedRuleContext(grammaticaParser.SelectContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_dql

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDql" ):
                listener.enterDql(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDql" ):
                listener.exitDql(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDql" ):
                return visitor.visitDql(self)
            else:
                return visitor.visitChildren(self)




    def dql(self):

        localctx = grammaticaParser.DqlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dql)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.select()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.key = None # ExprContext
            self.name = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammaticaParser.ExprContext,i)


        def getRuleIndex(self):
            return grammaticaParser.RULE_select

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect" ):
                listener.enterSelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect" ):
                listener.exitSelect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect" ):
                return visitor.visitSelect(self)
            else:
                return visitor.visitChildren(self)




    def select(self):

        localctx = grammaticaParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_select)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(grammaticaParser.T__10)
            self.state = 75
            localctx.key = self.expr()
            self.state = 76
            self.match(grammaticaParser.T__11)
            self.state = 77
            localctx.name = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SqlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def insert(self):
            return self.getTypedRuleContext(grammaticaParser.InsertContext,0)


        def update(self):
            return self.getTypedRuleContext(grammaticaParser.UpdateContext,0)


        def delete(self):
            return self.getTypedRuleContext(grammaticaParser.DeleteContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_sql

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql" ):
                listener.enterSql(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql" ):
                listener.exitSql(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSql" ):
                return visitor.visitSql(self)
            else:
                return visitor.visitChildren(self)




    def sql(self):

        localctx = grammaticaParser.SqlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_sql)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammaticaParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.insert()
                pass
            elif token in [grammaticaParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.update()
                pass
            elif token in [grammaticaParser.T__19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.delete()
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


    class InsertContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # ExprContext
            self.key = None # SmallterminalContext
            self.value = None # SmallterminalContext

        def expr(self):
            return self.getTypedRuleContext(grammaticaParser.ExprContext,0)


        def smallterminal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammaticaParser.SmallterminalContext)
            else:
                return self.getTypedRuleContext(grammaticaParser.SmallterminalContext,i)


        def getRuleIndex(self):
            return grammaticaParser.RULE_insert

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert" ):
                listener.enterInsert(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert" ):
                listener.exitInsert(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsert" ):
                return visitor.visitInsert(self)
            else:
                return visitor.visitChildren(self)




    def insert(self):

        localctx = grammaticaParser.InsertContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_insert)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(grammaticaParser.T__12)
            self.state = 85
            self.match(grammaticaParser.T__13)
            self.state = 86
            localctx.name = self.expr()
            self.state = 87
            self.match(grammaticaParser.T__1)
            self.state = 88
            localctx.key = self.smallterminal()
            self.state = 89
            self.match(grammaticaParser.T__2)
            self.state = 90
            self.match(grammaticaParser.T__14)
            self.state = 91
            self.match(grammaticaParser.T__1)
            self.state = 92
            localctx.value = self.smallterminal()
            self.state = 93
            self.match(grammaticaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # ExprContext
            self.key1 = None # ExprContext
            self.key1value = None # ExprContext
            self.key2 = None # ExprContext
            self.key2value = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammaticaParser.ExprContext,i)


        def getRuleIndex(self):
            return grammaticaParser.RULE_update

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdate" ):
                listener.enterUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdate" ):
                listener.exitUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = grammaticaParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(grammaticaParser.T__15)
            self.state = 96
            localctx.name = self.expr()
            self.state = 97
            self.match(grammaticaParser.T__16)
            self.state = 98
            localctx.key1 = self.expr()
            self.state = 99
            self.match(grammaticaParser.T__17)
            self.state = 100
            localctx.key1value = self.expr()
            self.state = 101
            self.match(grammaticaParser.T__18)
            self.state = 102
            localctx.key2 = self.expr()
            self.state = 103
            self.match(grammaticaParser.T__17)
            self.state = 104
            localctx.key2value = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # ExprContext
            self.key = None # ExprContext
            self.value = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammaticaParser.ExprContext,i)


        def getRuleIndex(self):
            return grammaticaParser.RULE_delete

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete" ):
                listener.enterDelete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete" ):
                listener.exitDelete(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelete" ):
                return visitor.visitDelete(self)
            else:
                return visitor.visitChildren(self)




    def delete(self):

        localctx = grammaticaParser.DeleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(grammaticaParser.T__19)
            self.state = 107
            self.match(grammaticaParser.T__11)
            self.state = 108
            localctx.name = self.expr()
            self.state = 109
            self.match(grammaticaParser.T__18)
            self.state = 110
            localctx.key = self.expr()
            self.state = 111
            self.match(grammaticaParser.T__17)
            self.state = 112
            localctx.value = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SmallterminalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(grammaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return grammaticaParser.RULE_smallterminal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSmallterminal" ):
                listener.enterSmallterminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSmallterminal" ):
                listener.exitSmallterminal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSmallterminal" ):
                return visitor.visitSmallterminal(self)
            else:
                return visitor.visitChildren(self)




    def smallterminal(self):

        localctx = grammaticaParser.SmallterminalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_smallterminal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            localctx.value = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





