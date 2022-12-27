from functools import reduce

class ASTGenerator(CSELVisitor):
    def visitProgram(self, ctx:CSELParser.ProgramContext):
        return Program(reduce(lambda prev, curr: prev + self.visit(curr), ctx.decl(), []))
        
    def visitCseltype(self, ctx:CSELParser.CseltypeContext):
        if ctx.INT(): return IntType()
        elif ctx.FLOAT(): return FloatType()
        return BooleanType()

    def visitDecl(self, ctx:CSELParser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl()) + self.visit(ctx.decltail())
        elif ctx.constdecl():
            return self.visit(ctx.constdecl()) + self.visit(ctx.decltail())
        return self.visit(ctx.funcdecl()) + self.visit(ctx.decltail())

    def visitDecltail(self, ctx:CSELParser.DecltailContext):
        if ctx.getChildCount() == 0: return []
        elif ctx.vardecl():
            return self.visit(ctx.vardecl()) + self.visit(ctx.decltail())
        elif ctx.constdecl():
            return self.visit(ctx.constdecl()) + self.visit(ctx.decltail())
        return [self.visit(ctx.funcdecl())] + self.visit(ctx.decltail())

    def visitVardecl(self, ctx:CSELParser.VardeclContext):
        return self.visit(ctx.single_vardecls())

    def visitSingle_vardecls(self, ctx:CSELParser.Single_vardeclsContext):
        return [self.visit(ctx.single_vardecl())] + self.visit(ctx.single_vardecltail())
        
    def visitSingle_vardecl(self, ctx:CSELParser.Single_vardeclContext):
        return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.cseltype()))

    def visitSingle_vardecltail(self, ctx:CSELParser.Single_vardecltailContext):
        if ctx.getChildCount() == 0: return []
        return [self.visit(ctx.single_vardecl())] + self.visit(ctx.single_vardecltail())
        

    def visitConstdecl(self, ctx:CSELParser.ConstdeclContext):
        return [self.visit(ctx.single_constdecl())]

    def visitSingle_constdecl(self, ctx:CSELParser.Single_constdeclContext):
        return ConstDecl(Id(ctx.ID().getText()), self.visit(ctx.cseltype()), self.visit(ctx.expr()))
        
    def visitExpr(self, ctx:CSELParser.ExprContext):
        if ctx.INTLIT():
            return IntLit(int(ctx.INTLIT().getText()))
        elif ctx.BOOLEANLIT():
            return BooleanLit(ctx.BOOLEANLIT().getText() == 'True')
        return FloatLit(float(ctx.FLOATLIT().getText()))

    def visitFuncdecl(self, ctx:CSELParser.FuncdeclContext):
        return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.paramlist()))

    def visitParamlist(self, ctx:CSELParser.ParamlistContext):
        if ctx.getChildCount() == 0: return []
        return self.visit(ctx.single_vardecls())
        