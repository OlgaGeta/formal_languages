from typing import List

from antlr4 import *
from gen.grammaticaLexer import grammaticaLexer
from gen.grammaticaParser import grammaticaParser
from gen.grammaticaVisitor import grammaticaVisitor

class MyVisitor(grammaticaVisitor):

    def visitNumberExpr(self, ctx):
        value = ctx.getText()
        return int(value)

    def visitStrExpr(self, ctx):
        value = ctx.getText()
        return str(value)

    def visitTerminal(self, ctx):
        key = self.visit(ctx.key)
        value = self.visit(ctx.value)
        return (key, value)

    def visitCreate(self, ctx):
        key, value = self.visit(ctx.pair)
        newdict = {key:value}
        db[self.visit(ctx.name)] = [newdict]
        return db

    def visitDrop(self, ctx):
        db.pop(self.visit(ctx.name))
        return db

    def visitAlter(self, ctx):
        key, value = self.visit(ctx.pair)
        newdict = {key:value}
        db[self.visit(ctx.name)].append(newdict)
        return db

    def visitTruncate(self, ctx):
        if self.visit(ctx.name) in db:
            db[self.visit(ctx.name)] = []
        else:
            pass
        return db

    def visitRename(self, ctx):
        db[self.visit(ctx.newname)] = db[self.visit(ctx.oldname)]
        db.pop(self.visit(ctx.oldname))
        return db

    def visitSelect(self, ctx):
        name = self.visit(ctx.name)
        key = self.visit(ctx.key)
        result = []
        for x in db[name]:
            if x[key]:
                result.append(x[key])
        return result

    def visitInsert(self, ctx):
        key = self.visit(ctx.key)
        value = self.visit(ctx.value)
        newdict = {key:value}
        db[self.visit(ctx.name)].append(newdict)
        return db

    def visitUpdate(self, ctx):
        key1 = self.visit(ctx.key1)
        key1value = self.visit(ctx.key1value)
        key2 = self.visit(ctx.key2)
        key2value = self.visit(ctx.key2value)
        for x in db[self.visit(ctx.name)]:
            if x[key2] == key2value:
                x[key1] = key1value
        return db

    def visitDelete(self, ctx):
        key = self.visit(ctx.key)
        value = self.visit(ctx.value)
        for x in db[self.visit(ctx.name)]:
            if x[key] == value:
                db[self.visit(ctx.name)].remove(x)
        return db

if __name__ == "__main__":
    # данные будут храниться в словаре
    db = {}
    while True:
        data = InputStream(input("> "))
        lexer = grammaticaLexer(data)
        stream = CommonTokenStream(lexer)
        parser = grammaticaParser(stream)
        tree = parser.expr()
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)
