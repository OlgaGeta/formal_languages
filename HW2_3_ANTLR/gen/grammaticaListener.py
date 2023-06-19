# Generated from grammatica.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grammaticaParser import grammaticaParser
else:
    from grammaticaParser import grammaticaParser

# This class defines a complete listener for a parse tree produced by grammaticaParser.
class grammaticaListener(ParseTreeListener):

    # Enter a parse tree produced by grammaticaParser#ddlExpr.
    def enterDdlExpr(self, ctx:grammaticaParser.DdlExprContext):
        pass

    # Exit a parse tree produced by grammaticaParser#ddlExpr.
    def exitDdlExpr(self, ctx:grammaticaParser.DdlExprContext):
        pass


    # Enter a parse tree produced by grammaticaParser#dqlExpr.
    def enterDqlExpr(self, ctx:grammaticaParser.DqlExprContext):
        pass

    # Exit a parse tree produced by grammaticaParser#dqlExpr.
    def exitDqlExpr(self, ctx:grammaticaParser.DqlExprContext):
        pass


    # Enter a parse tree produced by grammaticaParser#sqlExpr.
    def enterSqlExpr(self, ctx:grammaticaParser.SqlExprContext):
        pass

    # Exit a parse tree produced by grammaticaParser#sqlExpr.
    def exitSqlExpr(self, ctx:grammaticaParser.SqlExprContext):
        pass


    # Enter a parse tree produced by grammaticaParser#numberExpr.
    def enterNumberExpr(self, ctx:grammaticaParser.NumberExprContext):
        pass

    # Exit a parse tree produced by grammaticaParser#numberExpr.
    def exitNumberExpr(self, ctx:grammaticaParser.NumberExprContext):
        pass


    # Enter a parse tree produced by grammaticaParser#strExpr.
    def enterStrExpr(self, ctx:grammaticaParser.StrExprContext):
        pass

    # Exit a parse tree produced by grammaticaParser#strExpr.
    def exitStrExpr(self, ctx:grammaticaParser.StrExprContext):
        pass


    # Enter a parse tree produced by grammaticaParser#ddl.
    def enterDdl(self, ctx:grammaticaParser.DdlContext):
        pass

    # Exit a parse tree produced by grammaticaParser#ddl.
    def exitDdl(self, ctx:grammaticaParser.DdlContext):
        pass


    # Enter a parse tree produced by grammaticaParser#create.
    def enterCreate(self, ctx:grammaticaParser.CreateContext):
        pass

    # Exit a parse tree produced by grammaticaParser#create.
    def exitCreate(self, ctx:grammaticaParser.CreateContext):
        pass


    # Enter a parse tree produced by grammaticaParser#drop.
    def enterDrop(self, ctx:grammaticaParser.DropContext):
        pass

    # Exit a parse tree produced by grammaticaParser#drop.
    def exitDrop(self, ctx:grammaticaParser.DropContext):
        pass


    # Enter a parse tree produced by grammaticaParser#alter.
    def enterAlter(self, ctx:grammaticaParser.AlterContext):
        pass

    # Exit a parse tree produced by grammaticaParser#alter.
    def exitAlter(self, ctx:grammaticaParser.AlterContext):
        pass


    # Enter a parse tree produced by grammaticaParser#truncate.
    def enterTruncate(self, ctx:grammaticaParser.TruncateContext):
        pass

    # Exit a parse tree produced by grammaticaParser#truncate.
    def exitTruncate(self, ctx:grammaticaParser.TruncateContext):
        pass


    # Enter a parse tree produced by grammaticaParser#rename.
    def enterRename(self, ctx:grammaticaParser.RenameContext):
        pass

    # Exit a parse tree produced by grammaticaParser#rename.
    def exitRename(self, ctx:grammaticaParser.RenameContext):
        pass


    # Enter a parse tree produced by grammaticaParser#terminal.
    def enterTerminal(self, ctx:grammaticaParser.TerminalContext):
        pass

    # Exit a parse tree produced by grammaticaParser#terminal.
    def exitTerminal(self, ctx:grammaticaParser.TerminalContext):
        pass


    # Enter a parse tree produced by grammaticaParser#dql.
    def enterDql(self, ctx:grammaticaParser.DqlContext):
        pass

    # Exit a parse tree produced by grammaticaParser#dql.
    def exitDql(self, ctx:grammaticaParser.DqlContext):
        pass


    # Enter a parse tree produced by grammaticaParser#select.
    def enterSelect(self, ctx:grammaticaParser.SelectContext):
        pass

    # Exit a parse tree produced by grammaticaParser#select.
    def exitSelect(self, ctx:grammaticaParser.SelectContext):
        pass


    # Enter a parse tree produced by grammaticaParser#sql.
    def enterSql(self, ctx:grammaticaParser.SqlContext):
        pass

    # Exit a parse tree produced by grammaticaParser#sql.
    def exitSql(self, ctx:grammaticaParser.SqlContext):
        pass


    # Enter a parse tree produced by grammaticaParser#insert.
    def enterInsert(self, ctx:grammaticaParser.InsertContext):
        pass

    # Exit a parse tree produced by grammaticaParser#insert.
    def exitInsert(self, ctx:grammaticaParser.InsertContext):
        pass


    # Enter a parse tree produced by grammaticaParser#update.
    def enterUpdate(self, ctx:grammaticaParser.UpdateContext):
        pass

    # Exit a parse tree produced by grammaticaParser#update.
    def exitUpdate(self, ctx:grammaticaParser.UpdateContext):
        pass


    # Enter a parse tree produced by grammaticaParser#delete.
    def enterDelete(self, ctx:grammaticaParser.DeleteContext):
        pass

    # Exit a parse tree produced by grammaticaParser#delete.
    def exitDelete(self, ctx:grammaticaParser.DeleteContext):
        pass


    # Enter a parse tree produced by grammaticaParser#smallterminal.
    def enterSmallterminal(self, ctx:grammaticaParser.SmallterminalContext):
        pass

    # Exit a parse tree produced by grammaticaParser#smallterminal.
    def exitSmallterminal(self, ctx:grammaticaParser.SmallterminalContext):
        pass



del grammaticaParser