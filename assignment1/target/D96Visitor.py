# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalavar.
    def visitScalavar(self, ctx:D96Parser.ScalavarContext):
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


    # Visit a parse tree produced by D96Parser#invokemethod.
    def visitInvokemethod(self, ctx:D96Parser.InvokemethodContext):
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


    # Visit a parse tree produced by D96Parser#exp10.
    def visitExp10(self, ctx:D96Parser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classname.
    def visitClassname(self, ctx:D96Parser.ClassnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#construct.
    def visitConstruct(self, ctx:D96Parser.ConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destruct.
    def visitDestruct(self, ctx:D96Parser.DestructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method.
    def visitMethod(self, ctx:D96Parser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameters.
    def visitParameters(self, ctx:D96Parser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist.
    def visitIdlist(self, ctx:D96Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr.
    def visitAttr(self, ctx:D96Parser.AttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl.
    def visitVardecl(self, ctx:D96Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#explist.
    def visitExplist(self, ctx:D96Parser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#datatype.
    def visitDatatype(self, ctx:D96Parser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arraynested.
    def visitArraynested(self, ctx:D96Parser.ArraynestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayindex.
    def visitArrayindex(self, ctx:D96Parser.ArrayindexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#value.
    def visitValue(self, ctx:D96Parser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#booln.
    def visitBooln(self, ctx:D96Parser.BoolnContext):
        return self.visitChildren(ctx)



del D96Parser