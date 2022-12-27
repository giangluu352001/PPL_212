from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

class ASTGeneration(D96Visitor):
    def visitProgram(self,ctx:D96Parser.ProgramContext):
        return Program([FuncDecl(Id("main"),
                        [],
                        self.visit(ctx.mptype()),
                        Block([],[self.visit(ctx.body())] if ctx.body() else []))])

    def visitMptype(self,ctx:D96Parser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        else:
            return VoidType()

    def visitBody(self,ctx:D96Parser.BodyContext):
        return self.visit(ctx.funcall())
  
  	
    def visitFuncall(self,ctx:D96Parser.FuncallContext):
        return CallExpr(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self,ctx:D96Parser.ExpContext):
        if (ctx.funcall()):
            return self.visit(ctx.funcall())
        else:
            return IntLiteral(int(ctx.INTLIT().getText()))
    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameters.
    def visitParameters(self, ctx:D96Parser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method.
    def visitMethod(self, ctx:D96Parser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ifstatement.
    def visitIfstatement(self, ctx:D96Parser.IfstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forstatement.
    def visitForstatement(self, ctx:D96Parser.ForstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#breakstatement.
    def visitBreakstatement(self, ctx:D96Parser.BreakstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continuestatement.
    def visitContinuestatement(self, ctx:D96Parser.ContinuestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#returnstatement.
    def visitReturnstatement(self, ctx:D96Parser.ReturnstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#blockstatement.
    def visitBlockstatement(self, ctx:D96Parser.BlockstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp.
    def visitExp(self, ctx:D96Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp1.
    def visitExp1(self, ctx:D96Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp2.
    def visitExp2(self, ctx:D96Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp3.
    def visitExp3(self, ctx:D96Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp4.
    def visitExp4(self, ctx:D96Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp5.
    def visitExp5(self, ctx:D96Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp6.
    def visitExp6(self, ctx:D96Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp7.
    def visitExp7(self, ctx:D96Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp8.
    def visitExp8(self, ctx:D96Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp9.
    def visitExp9(self, ctx:D96Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element.
    def visitElement(self, ctx:D96Parser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index.
    def visitIndex(self, ctx:D96Parser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#explist.
    def visitExplist(self, ctx:D96Parser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#getattribute.
    def visitGetattribute(self, ctx:D96Parser.GetattributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#getstaticatrr.
    def visitGetstaticatrr(self, ctx:D96Parser.GetstaticatrrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#funcall.
    def visitFuncall(self, ctx:D96Parser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#funcallstatic.
    def visitFuncallstatic(self, ctx:D96Parser.FuncallstaticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#createobject.
    def visitCreateobject(self, ctx:D96Parser.CreateobjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classname.
    def visitClassname(self, ctx:D96Parser.ClassnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructorname.
    def visitConstructorname(self, ctx:D96Parser.ConstructornameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructorname.
    def visitDestructorname(self, ctx:D96Parser.DestructornameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute.
    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#datatype.
    def visitDatatype(self, ctx:D96Parser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arraynested.
    def visitArraynested(self, ctx:D96Parser.ArraynestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array.
    def visitArray(self, ctx:D96Parser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multiarrayindex.
    def visitMultiarrayindex(self, ctx:D96Parser.MultiarrayindexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayindex.
    def visitArrayindex(self, ctx:D96Parser.ArrayindexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#value.
    def visitValue(self, ctx:D96Parser.ValueContext):
        return self.visitChildren(ctx)

