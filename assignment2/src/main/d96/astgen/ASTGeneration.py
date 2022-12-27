from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from functools import reduce

class ASTGeneration(D96Visitor):
    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return Program(reduce(lambda prev, curr: prev + self.visit(curr), ctx.classname(), []))

    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return [self.visit(ctx.getChild(0))] if not ctx.vardecl() else list(self.visit(ctx.getChild(0)))

    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        if ctx.scalavar(): 
            scala = self.visit(ctx.scalavar())
            return Assign(scala, self.visit(ctx.exp()))
        else: 
            arr = self.visit(ctx.exp8())
            idx = reduce(lambda prev, curr: prev + self.visit(curr), ctx.indexop(), [])
            idxexp = ArrayCell(arr, idx)
            return Assign(idxexp, self.visit(ctx.exp()))

    # Visit a parse tree produced by D96Parser#scalavar.
    def visitScalavar(self, ctx:D96Parser.ScalavarContext):
        if ctx.getChildCount() == 1: return Id(ctx.ID().getText())
        elif ctx.DOT(): 
            return FieldAccess(self.visit(ctx.exp8()), Id(ctx.ID().getText()))
        return FieldAccess(Id(ctx.ID().getText()), Id(ctx.DOLLAR_ID().getText()))

    # Visit a parse tree produced by D96Parser#ifstatement.
    def visitIfstatement(self, ctx:D96Parser.IfstatementContext):
        explist = list(map(lambda x: self.visit(x), ctx.exp()))
        blocklist = list(map(lambda x: self.visit(x), ctx.blockstatement()))
        if not ctx.ELSE(): blocklist = blocklist + [None]
        return reduce(lambda acc, ele: If(ele[0], ele[1], acc),
            zip(explist[-2::-1], blocklist[-3::-1]),
            If(explist[-1], blocklist[-2], blocklist[-1]))

    # Visit a parse tree produced by D96Parser#forstatement.
    def visitForstatement(self, ctx:D96Parser.ForstatementContext):
        id = self.visit(ctx.scalavar())
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        expr3 = self.visit(ctx.exp(2)) if ctx.exp(2) else IntLiteral(1)
        loop = self.visit(ctx.blockstatement())
        return For(id, expr1, expr2, loop, expr3)

    # Visit a parse tree produced by D96Parser#breakstatement.
    def visitBreakstatement(self, ctx:D96Parser.BreakstatementContext):
        return Break()

    # Visit a parse tree produced by D96Parser#continuestatement.
    def visitContinuestatement(self, ctx:D96Parser.ContinuestatementContext):
        return Continue()

    # Visit a parse tree produced by D96Parser#returnstatement.
    def visitReturnstatement(self, ctx:D96Parser.ReturnstatementContext):
        if ctx.exp(): return Return(self.visit(ctx.exp()))
        return Return()

    # Visit a parse tree produced by D96Parser#invokemethod.
    def visitInvokemethod(self, ctx:D96Parser.InvokemethodContext):
        if ctx.exp9():
            method = Id(ctx.ID().getText())
            param = self.visit(ctx.paramexp())
            if ctx.partinvoke():
                lst = list(map(lambda x: self.visit(x), ctx.partinvoke()))
                first = FieldAccess(self.visit(ctx.exp9()), lst[0][0]) if len(lst[0]) == 1 else \
                CallExpr(self.visit(ctx.exp9()), lst[0][0], lst[0][1])
                obj = reduce(lambda acc, ele: FieldAccess(acc, ele[0]) if len(ele) == 1 else
                CallExpr(acc, ele[0], ele[1]), lst[1:], first)
            else: obj = self.visit(ctx.exp9())
            return CallStmt(obj, method, param)
        else:
            obj = Id(ctx.ID().getText())
            name = Id(ctx.DOLLAR_ID().getText())
            param = self.visit(ctx.paramexp())
            return CallStmt(obj, name, param)

    # Visit a parse tree produced by D96Parser#partinvoke.
    def visitPartinvoke(self, ctx:D96Parser.PartinvokeContext):
        if ctx.paramexp():
            param = self.visit(ctx.paramexp())
            return [Id(ctx.ID().getText())] + [param]
        else: return [Id(ctx.ID().getText())]
    
    # Visit a parse tree produced by D96Parser#blockstatement.
    def visitBlockstatement(self, ctx:D96Parser.BlockstatementContext):
        if ctx.statement(): 
            inst = reduce(lambda prev, curr: prev + self.visit(curr), ctx.statement(), [])
        else: inst = []
        return Block(inst)

    # Visit a parse tree produced by D96Parser#exp.
    def visitExp(self, ctx:D96Parser.ExpContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp1(0))
        left = self.visit(ctx.exp1(0))
        right = self.visit(ctx.exp1(1))
        op = ctx.getChild(1).getText()
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by D96Parser#exp1.
    def visitExp1(self, ctx:D96Parser.Exp1Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp2(0))
        left = self.visit(ctx.exp2(0))
        right = self.visit(ctx.exp2(1))
        op = ctx.getChild(1).getText()
        return BinaryOp(op, left, right)


    # Visit a parse tree produced by D96Parser#exp2.
    def visitExp2(self, ctx:D96Parser.Exp2Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp3())
        left = self.visit(ctx.exp2())
        right = self.visit(ctx.exp3())
        op = ctx.getChild(1).getText()
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by D96Parser#exp3.
    def visitExp3(self, ctx:D96Parser.Exp3Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp4())
        left = self.visit(ctx.exp3())
        right = self.visit(ctx.exp4())
        op = ctx.getChild(1).getText()
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by D96Parser#exp4.
    def visitExp4(self, ctx:D96Parser.Exp4Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp5())
        left = self.visit(ctx.exp4())
        right = self.visit(ctx.exp5())
        op = ctx.getChild(1).getText()
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by D96Parser#exp5.
    def visitExp5(self, ctx:D96Parser.Exp5Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp6())
        body = self.visit(ctx.exp5())
        op = ctx.NOT().getText()
        return UnaryOp(op, body)

    # Visit a parse tree produced by D96Parser#exp6.
    def visitExp6(self, ctx:D96Parser.Exp6Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp7())
        body = self.visit(ctx.exp6())
        op = ctx.SUB().getText()
        return UnaryOp(op, body)

    # Visit a parse tree produced by D96Parser#exp7.
    def visitExp7(self, ctx:D96Parser.Exp7Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp8())
        arr = self.visit(ctx.exp7())
        idx = reduce(lambda prev, curr: prev + self.visit(curr), ctx.indexop(), [])
        return ArrayCell(arr, idx)

    # Visit a parse tree produced by D96Parser#exp8.
    def visitExp8(self, ctx:D96Parser.Exp8Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp9())
        obj = self.visit(ctx.exp8())
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.paramexp()) if ctx.paramexp() else []
        if not ctx.paramexp(): return FieldAccess(obj, name)
        return CallExpr(obj, name, param)

    # Visit a parse tree produced by D96Parser#exp9.
    def visitExp9(self, ctx:D96Parser.Exp9Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp10())
        obj = Id(ctx.ID().getText())
        name = Id(ctx.DOLLAR_ID().getText())
        param = self.visit(ctx.paramexp()) if ctx.paramexp() else []
        if not ctx.paramexp(): return FieldAccess(obj, name)
        return CallExpr(obj, name, param)

    # Visit a parse tree produced by D96Parser#exp10.
    def visitExp10(self, ctx:D96Parser.Exp10Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.operands())
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.paramexp())
        return NewExpr(name, param)

    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        if ctx.value(): return self.visit(ctx.value())
        elif ctx.SELFTYPE(): return SelfLiteral()
        elif ctx.NULLTYPE(): return NullLiteral()
        elif ctx.ID(): return Id(ctx.ID().getText())
        return self.visit(ctx.exp())

    def visitParamexp(self, ctx:D96Parser.ParamexpContext):
        return self.visit(ctx.explist()) if ctx.explist() else []

    # Visit a parse tree produced by D96Parser#indexop.
    def visitIndexop(self, ctx:D96Parser.IndexopContext):
        return [self.visit(ctx.exp())]

    # Visit a parse tree produced by D96Parser#classname.
    def visitClassname(self, ctx:D96Parser.ClassnameContext):
        name = Id(ctx.ID(0).getText())
        parentname = Id(ctx.ID(1).getText()) if ctx.ID(1) else None
        if ctx.memclass():
            memlist = reduce(lambda prev, curr: prev + self.visit(curr), ctx.memclass(), [])
        else: memlist = []
        if name.name == 'Program':
            for v in memlist:
                if isinstance(v, MethodDecl) and v.name.name == 'main' and v.param == []: v.kind = Static()
        return [ClassDecl(name, memlist, parentname)]

    def visitMemclass(self, ctx:D96Parser.MemclassContext):
        return list(self.visit(ctx.getChild(0))) if ctx.attr() else [self.visit(ctx.getChild(0))]

    # Visit a parse tree produced by D96Parser#construct.
    def visitConstruct(self, ctx:D96Parser.ConstructContext):
        param = self.visit(ctx.parameters()) if ctx.parameters() else []
        body = self.visit(ctx.blockstatement())
        return MethodDecl(Instance(), Id('Constructor'), param, body)

    # Visit a parse tree produced by D96Parser#destruct.
    def visitDestruct(self, ctx:D96Parser.DestructContext):
        return MethodDecl(Instance(), Id('Destructor'), [], self.visit(ctx.blockstatement()))

    # Visit a parse tree produced by D96Parser#method.
    def visitMethod(self, ctx:D96Parser.MethodContext):
        if ctx.DOLLAR_ID(): 
            kind = Static()
            name = Id(ctx.DOLLAR_ID().getText())
        else:
            kind = Instance()
            name = Id(ctx.ID().getText())
        param = self.visit(ctx.parameters()) if ctx.parameters() else []
        body = self.visit(ctx.blockstatement())
        return MethodDecl(kind, name, param, body)

    # Visit a parse tree produced by D96Parser#parameters.
    def visitParameters(self, ctx:D96Parser.ParametersContext):
        idlists = list(map(lambda x: self.visit(x) , ctx.idlist()))
        types = list(map(lambda x: self.visit(x) , ctx.datatype()))
        return reduce(lambda acc, ele: acc + list(map(lambda x: 
        VarDecl(x, ele[1], NullLiteral()) if isinstance(ele[1], ClassType) else
        VarDecl(x, ele[1]), ele[0])), zip(idlists, types), [])

    # Visit a parse tree produced by D96Parser#idlist.
    def visitIdlist(self, ctx:D96Parser.IdlistContext):
        return list(map(lambda x: Id(x.getText()), ctx.ID()))

    # Visit a parse tree produced by D96Parser#attr.
    def visitAttr(self, ctx:D96Parser.AttrContext):
        variables = list(map(lambda x: Id(x.getText()), ctx.idattr()))
        type = self.visit(ctx.datatype())
        values = list(map(lambda x: self.visit(x), ctx.exp())) if ctx.exp() else [None]*len(variables)
        if not ctx.exp() and isinstance(type, ClassType) and not ctx.CONSTTYPE():
            values = [NullLiteral()]*len(variables)
        if ctx.VARTYPE():
            decl = list(map(lambda x,y: VarDecl(x, type, y), variables, values))
        else:   decl = list(map(lambda x,y: ConstDecl(x, type, y), variables, values))
        return map(lambda x: AttributeDecl(Static(), x) if ((isinstance(x, VarDecl) and '$' in x.variable.name) or \
        (isinstance(x, ConstDecl) and '$' in x.constant.name)) else AttributeDecl(Instance(), x), decl)

    # Visit a parse tree produced by D96Parser#idattr.
    def visitIdattr(self, ctx:D96Parser.IdattrContext):
        return ctx.getChild(0)

    # Visit a parse tree produced by D96Parser#vardecl.
    def visitVardecl(self, ctx:D96Parser.VardeclContext):
        variables = list(map(lambda x: Id(x.getText()), ctx.ID()))
        type = self.visit(ctx.datatype())
        values = list(map(lambda x: self.visit(x), ctx.exp())) if ctx.exp() else [None]*len(variables)
        if values[0] == None and isinstance(type, ClassType) and not ctx.CONSTTYPE():  values = [NullLiteral()]*len(variables)
        if ctx.VARTYPE():
            return map(lambda x,y: VarDecl(x, type, y), variables, values)
        return map(lambda x,y: ConstDecl(x, type, y), variables, values)

    # Visit a parse tree produced by D96Parser#explist.
    def visitExplist(self, ctx:D96Parser.ExplistContext):
        return list(map(lambda x: self.visit(x), ctx.exp())) 

    # Visit a parse tree produced by D96Parser#datatype.
    def visitDatatype(self, ctx:D96Parser.DatatypeContext):
        if ctx.INTTYPE(): return IntType()
        elif ctx.BOOLEANTYPE(): return BoolType()
        elif ctx.FLOATTYPE(): return FloatType()
        elif ctx.arraynested(): return self.visit(ctx.arraynested())
        elif ctx.STRINGTYPE(): return StringType()
        return ClassType(Id(ctx.ID().getText()))

    # Visit a parse tree produced by D96Parser#arraynested.
    def visitArraynested(self, ctx:D96Parser.ArraynestedContext):
        if ctx.INTTYPE(): eleType = IntType()
        elif ctx.BOOLEANTYPE(): eleType = BoolType()
        elif ctx.FLOATTYPE(): eleType = FloatType()
        elif ctx.arraynested(): eleType = self.visit(ctx.arraynested())
        elif ctx.STRINGTYPE(): eleType = StringType()
        value = ctx.INT().getText()
        if len(value) > 2 and value[0] == '0' and value[1] in ['x', 'X']: 
            size = int(value, 16)
        elif len(value) > 2 and value[0] == '0' and value[1] in ['b', 'B']: 
            size = int(value, 2)
        elif len(value) > 1 and value[0] == '0': 
            size = int(value[:1] + 'o' + value[1:], 8)
        else: size = int(value)
        return ArrayType(size, eleType)

    def visitMultiarrayindex(self, ctx:D96Parser.MultiarrayindexContext):
        if not ctx.indexlist(): return [] 
        return ArrayLiteral(self.visit(ctx.indexlist()))

    # Visit a parse tree produced by D96Parser#arrayindex.
    def visitArrayindex(self, ctx:D96Parser.ArrayindexContext):
        return ArrayLiteral(self.visit(ctx.paramexp()))

    def visitIndexlist(self, ctx:D96Parser.IndexlistContext):
        return list(map(lambda x: self.visit(x), ctx.arrayindex())) 

    # Visit a parse tree produced by D96Parser#value.
    def visitValue(self, ctx:D96Parser.ValueContext):
        if ctx.INT(): 
            value = ctx.INT().getText()
            if len(value) > 2 and value[0] == '0' and value[1] in ['x', 'X']: 
                return IntLiteral(int(value, 16))
            elif len(value) > 2 and value[0] == '0' and value[1] in ['b', 'B']: 
                return IntLiteral(int(value, 2))
            elif len(value) > 1 and value[0] == '0': 
                return IntLiteral(int(value[:1] + 'o' + value[1:], 8))
            return IntLiteral(int(value))
        elif ctx.FLOAT(): return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.booln(): return self.visit(ctx.booln())
        elif ctx.STRING(): return StringLiteral(ctx.STRING().getText())
        elif ctx.arrayindex(): return self.visit(ctx.arrayindex())
        return self.visit(ctx.multiarrayindex())

    # Visit a parse tree produced by D96Parser#booln.
    def visitBooln(self, ctx:D96Parser.BoolnContext):
        return BooleanLiteral(ctx.getChild(0).getText() == 'True')
