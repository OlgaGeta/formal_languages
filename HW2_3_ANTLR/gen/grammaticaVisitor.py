# Generated from grammatica.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grammaticaParser import grammaticaParser
else:
    from grammaticaParser import grammaticaParser

# This class defines a complete generic visitor for a parse tree produced by grammaticaParser.

class grammaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammaticaParser#ddlExpr.
    def visitDdlExpr(self, ctx:grammaticaParser.DdlExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#dqlExpr.
    def visitDqlExpr(self, ctx:grammaticaParser.DqlExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#sqlExpr.
    def visitSqlExpr(self, ctx:grammaticaParser.SqlExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#numberExpr.
    def visitNumberExpr(self, ctx:grammaticaParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#strExpr.
    def visitStrExpr(self, ctx:grammaticaParser.StrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#ddl.
    def visitDdl(self, ctx:grammaticaParser.DdlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#create.
    def visitCreate(self, ctx:grammaticaParser.CreateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#drop.
    def visitDrop(self, ctx:grammaticaParser.DropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#alter.
    def visitAlter(self, ctx:grammaticaParser.AlterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#truncate.
    def visitTruncate(self, ctx:grammaticaParser.TruncateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#rename.
    def visitRename(self, ctx:grammaticaParser.RenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#terminal.
    def visitTerminal(self, ctx:grammaticaParser.TerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#dql.
    def visitDql(self, ctx:grammaticaParser.DqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#select.
    def visitSelect(self, ctx:grammaticaParser.SelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#sql.
    def visitSql(self, ctx:grammaticaParser.SqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#insert.
    def visitInsert(self, ctx:grammaticaParser.InsertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#update.
    def visitUpdate(self, ctx:grammaticaParser.UpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#delete.
    def visitDelete(self, ctx:grammaticaParser.DeleteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammaticaParser#smallterminal.
    def visitSmallterminal(self, ctx:grammaticaParser.SmallterminalContext):
        return self.visitChildren(ctx)



del grammaticaParser