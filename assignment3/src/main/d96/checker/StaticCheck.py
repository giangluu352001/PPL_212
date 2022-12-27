
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from StaticError import *

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype
    def __str__(self):
        mid = ','.join(str(i) for i in self.partype) if self.partype else ""
        return "MType(" + mid + "," + str(self.rettype) + ")"

class Symbol:
    def __init__(self, name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        value = str(self.value[0]) + "," + str(self.value[1]) if self.value else ""
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + "," + value + ")"
class StaticChecker(BaseVisitor):

    global_envi = []
            
    def __init__(self,ast):
        self.ast = ast
    
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)
        
    def visitId(self, ast, c):
        undeclared = self.lookup(ast.name, c[0], lambda x: x.name)
        if not undeclared: raise Undeclared(Identifier(), ast.name)
        if c[-1] == "LHS": return undeclared
        else: return undeclared.mtype.rettype
    
    def visitBinaryOp(self, ast, c):
        if isinstance(c[-1], ConstDecl):
            if not (isinstance(ast.left, Literal) or isinstance(ast.left, FieldAccess)) \
            or not (isinstance(ast.right, Literal) or isinstance(ast.right, FieldAccess)):
                raise IllegalConstantExpression(ast)
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        def checkType(inputType, outputType = None):
            if not isinstance(left, inputType) or not isinstance(right, inputType):
                raise TypeMismatchInExpression(ast)
            elif outputType: return outputType
            elif isinstance(left, IntType) and isinstance(right, FloatType): return FloatType()
            elif isinstance(left, FloatType) and isinstance(right, IntType): return FloatType()
            elif isinstance(left, type(right)): return right
            else: raise TypeMismatchInExpression(ast)
        if ast.op in ["+", "-", "*", "/"]:
            return checkType((IntType, FloatType))
        elif ast.op in ["<", "<=", ">", ">="]:
            return checkType((IntType, FloatType), BoolType())
        elif ast.op == "%": return checkType(IntType, IntType())
        elif ast.op in ["!=", "=="]:
            return checkType((IntType, BoolType), BoolType())
        elif ast.op in ["&&", "||"]: return checkType(BoolType, BoolType())
        elif ast.op == "==.": return checkType(StringType, BoolType())
        elif ast.op == "+.": return checkType(StringType, StringType())

    def visitUnaryOp(self, ast, c):
        if isinstance(c[-1], ConstDecl):
            if not (isinstance(ast.body, Literal) or isinstance(ast.body, FieldAccess)):
                raise IllegalConstantExpression(ast)
        exp = self.visit(ast.body, c)
        if ast.op == "!":
            if isinstance(exp, BoolType): return BoolType()
            raise TypeMismatchInExpression(ast)
        elif ast.op == "-":
            if isinstance(exp, (IntType, FloatType)): return exp
            raise TypeMismatchInExpression(ast)

    def callfunc(self, ast, c, isExpr):
        if isExpr: locallist, allclass, inherit, _= c
        else: locallist, allclass, inherit, _, _= c
        error = TypeMismatchInExpression(ast) if isExpr else TypeMismatchInStatement(ast)
        
        def checkAll(name):
            access = self.lookup(name, allclass, lambda x: x.name) 
            if access:
                if access.mtype.rettype[0]:
                    parent = self.lookup(access.mtype.rettype[0].classname.name, allclass, lambda x: x.name)
                    parentmem = parent.value
                else: parentmem = []
                return checkCallMethod(ast.method.name, access.value + parentmem, paramlist)
            else: raise Undeclared(Class(), ast.obj.name)

        def checkCallMethod(name, lst, paramlist):
            func = self.lookup(name, lst, lambda x: x.name)
            if isinstance(func.mtype.rettype, VoidType) and isExpr: raise error
            elif not isinstance(func.mtype.rettype, VoidType) and not isExpr: raise error
            if func is None:
                raise Undeclared(Method(),ast.method.name)
            elif len(func.mtype.partype) != len(paramlist): raise error
            for i in range(0, len(paramlist)):
                left = func.mtype.partype[i]
                if not self.checkPrimitive(left, paramlist[i]): raise error
            return func.mtype.rettype
        
        paramlist = [self.visit(param, (locallist, allclass, inherit, None)) for param in ast.param]
        if ast.method.name[0] == "$":
            if not isinstance(ast.obj, Id): raise IllegalMemberAccess(ast)
            else: return checkAll(ast.obj.name)
        else:
            obj = self.visit(ast.obj, (locallist, allclass, inherit, ast))
            if not isinstance(obj, ClassType): 
                raise IllegalMemberAccess(ast)
            name = obj.classname.name
            if name == "Self": return checkAll(inherit[1].name)
            else: return checkAll(name)

    def visitCallExpr(self, ast, c): 
        return self.callfunc(ast, c, True)

    def visitNewExpr(self, ast, c):
        instance = self.lookup(ast.classname.name, c[1], lambda x: x.name)
        if instance is None: raise Undeclared(Class(), ast.classname.name)
        paramlist = []
        for param in ast.param:
            paramlist.append(self.visit(param, c))
        if len(paramlist) != len(instance.mtype.partype):
            raise TypeMismatchInExpression(ast)
        for i in range(0, len(paramlist)):
            if not self.checkPrimitive(instance.mtype.partype[i], paramlist[i]):
                raise TypeMismatchInExpression(ast)
        return ClassType(ast.classname)

    def visitArrayCell(self, ast, c):
        arr = self.visit(ast.arr, c)
        if c[-1] == "LHS": rettype = arr.mtype.rettype
        else: rettype = arr
        idxlist = [self.visit(x, c) for x in ast.idx]
        if any(not isinstance(idx, IntType) for idx in idxlist) or not isinstance(rettype, ArrayType):
            raise TypeMismatchInExpression(ast)
        nested = len(idxlist)
        for i in range(nested):
            if not isinstance(rettype, ArrayType): break
            rettype = rettype.eleType
        if c[-1] != "LHS": return rettype 
        else: return Symbol(arr.name, MType(None, rettype), arr.value)

    def visitFieldAccess(self, ast, c):
        locallist, allclass, inherit, isassign = c
        if ast.fieldname.name[0] == "$":
            if not isinstance(ast.obj, Id): raise Undeclared(Class(), ast.obj)
            else: 
                classname = self.lookup(ast.obj.name, allclass, lambda x: x.name)
                if classname:
                    checkfield = self.lookup(ast.fieldname.name, classname.value, lambda x: x.name)
                    if not checkfield: raise Undeclared(Attribute(), ast.fieldname.name)
                    if isassign == "LHS": return checkfield
                    else: return checkfield.mtype.rettype
        else:
            obj = self.visit(ast.obj, (locallist, allclass, inherit, ast))
            if isinstance(ast.obj, Id):
                classname = self.lookup(ast.obj.name, allclass, lambda x: x.name)
                if classname and self.lookup(ast.fieldname.name, classname.value, lambda x: x.name):
                    raise IllegalMemberAccess(ast)
            if not isinstance(obj, ClassType) or not (isinstance(obj, ClassType) \
            and obj.classname.name in ["Self", inherit[-1].name]): raise IllegalMemberAccess(ast)
            undeclared = None
            parent = inherit[0].value if inherit[0] else []
            for x in inherit[1].value + parent:
                if ast.fieldname.name == x.name and x.value and isinstance(x.value[0], Attribute): 
                    undeclared = x
                    break
            if undeclared is None: raise Undeclared(Attribute(), ast.fieldname.name)
            if isassign == "LHS": return undeclared
            else: return undeclared.mtype.rettype

    def visitIntLiteral(self, ast, c): return IntType()
    
    def visitFloatLiteral(self, ast, c): return FloatType()
    
    def visitStringLiteral(self, ast, c): return StringType()
    
    def visitBooleanLiteral(self, ast, c): return BoolType()

    def visitSelfLiteral(self, ast, c): return ClassType(Id("Self"))

    def visitNullLiteral(self, ast, c): return NullLiteral()

    def visitArrayLiteral(self, ast, c):
        size = len(ast.value)
        typ = None
        for i in range(size):
            alltype = self.visit(ast.value[i], c)
            if i == 0: typ = alltype
            else: 
                if not isinstance(alltype, type(typ)): 
                    raise IllegalArrayLiteral(ast)
        return ArrayType(size, typ)

    def visitAssign(self, ast, c):
        locallist, allclass, inherit, _, _ = c
        lhs = self.visit(ast.lhs, (locallist, allclass, inherit, "LHS"))
        if isinstance(lhs.value[-1], Constant): raise CannotAssignToConstant(ast)
        elif isinstance(lhs.mtype.rettype, VoidType): raise TypeMismatchInStatement(ast)
        rhs = self.visit(ast.exp, (locallist, allclass, inherit, ast))
        if not self.checkAllType(lhs, rhs, allclass): raise TypeMismatchInStatement(ast)

    def checkPrimitive(self, left, right):
        if isinstance(left, type(right)) or (isinstance(left, FloatType) \
        and isinstance(right, IntType)): return True
        else: return False

    def checkAllType(self, left, right, allclass):
        if isinstance(left, Symbol):
            if isinstance(left.mtype.partype, ClassType) and \
            self.checkAllType(left.mtype.partype, right, allclass): 
                left.mtype.rettype = right
                return True
            else: return self.checkAllType(left.mtype.rettype, right, allclass)
        elif isinstance(left, ClassType) and isinstance(right, ClassType):
            if left.classname.name == right.classname.name: return True
            else:
                parent = self.lookup(right.classname.name, allclass, lambda x: x.name)
                if parent.mtype.rettype[0] and left.classname.name == \
                parent.mtype.rettype[0].classname.name: return True
        elif isinstance(left, ArrayType) and isinstance(right, ArrayType):
            if right.size == left.size and \
            self.checkAllType(left.eleType, right.eleType, allclass): return True
        else: return self.checkPrimitive(left, right)

    def visitIf(self, ast, c):
        locallist, allclass, inherit, _, _ = c
        exp = self.visit(ast.expr, (locallist, allclass, inherit, None))
        if not isinstance(exp, BoolType):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, c)
        if ast.elseStmt: self.visit(ast.elseStmt, c)

    def visitFor(self, ast, c):
        locallist, allclass, inherit, isinloop, method = c
        id = self.visit(ast.id, (locallist, allclass, inherit, "LHS"))
        expr1 = self.visit(ast.expr1, (locallist, allclass, inherit, None))
        if isinstance(id.value[-1], Constant): raise CannotAssignToConstant(ast.id)
        expr2 = self.visit(ast.expr2, (locallist, allclass, inherit, None))
        expr3 = self.visit(ast.expr3, (locallist, allclass, inherit, None))
        match = isinstance(id.mtype.rettype, IntType) and isinstance(expr1, IntType) \
        and isinstance(expr2, IntType) and isinstance(expr3, IntType)
        if not match: raise TypeMismatchInStatement(ast)
        if isinstance(ast.loop, Expr): self.visit(ast.loop, (locallist, allclass, inherit, None))
        else:
            isinloop = True
            self.visit(ast.loop, (locallist, allclass, inherit, isinloop, method))

    def visitBreak(self, ast, c):
        if not c[-2]: raise MustInLoop(Break()) 

    def visitContinue(self, ast, c):
        if not c[-2]: raise MustInLoop(Continue())

    def visitReturn(self, ast, c):
        locallist, allclass, inherit, _, method = c
        if method.name == "Constructor" and ast.expr is not None: raise TypeMismatchInStatement(ast)
        elif method.mtype.rettype is None:
            if not ast.expr: method.mtype.rettype = VoidType()
            else: method.mtype.rettype = self.visit(ast.expr, (locallist, allclass, inherit, None))
        else:
            if not ast.expr and not isinstance(method.mtype.rettype, VoidType):
                raise TypeMismatchInStatement(ast)
            typ = self.visit(ast.expr, (locallist, allclass, inherit, None))
            if isinstance(method.mtype.rettype, FloatType) and isinstance(typ, (IntType, FloatType)):
                return FloatType()
            elif not isinstance(method.mtype.rettype, type(typ)):
                raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast, c):
        return self.callfunc(ast, c, False)

    def visitVarDecl(self, ast, c):
        memlist, nonlocallist, allclass, inherit, isattr = c
        redeclared = self.lookup(ast.variable.name, c[0], lambda x: x.name)
        if isattr and redeclared: raise Redeclared(Attribute(), redeclared.name)
        elif redeclared: raise Redeclared(Variable(), redeclared.name)
        typ = Attribute() if isattr else Variable()
        if isinstance(ast.varInit, NullLiteral):
            return Symbol(ast.variable.name, MType(ast.varType, NullLiteral()), (typ, None))
        elif ast.varInit is not None:
            checkInit = self.visit(ast.varInit, (memlist + nonlocallist, allclass, inherit, ast))
            if not self.checkAllType(ast.varType, checkInit, allclass): raise TypeMismatchInStatement(ast)
        return Symbol(ast.variable.name, MType(None, ast.varType), (typ, None))

    def visitBlock(self, ast, c):
        nonlocallist, allclass, inherit, isinloop, method = c
        locallist = []
        for inst in ast.inst:
            if isinstance(inst, VarDecl):
                locallist.append(self.visit(inst, (locallist, nonlocallist, allclass, inherit, False)))
            elif isinstance(inst, ConstDecl):
                locallist.append(self.visit(inst, (locallist, nonlocallist, allclass, inherit, False)))
            elif isinstance(inst, Expr):
                self.visit(inst, (locallist + nonlocallist, allclass, inherit, None))
            else:
                self.visit(inst, (locallist + nonlocallist, allclass, inherit, isinloop, method))

    def visitConstDecl(self, ast, c):
        memlist, nonlocallist, allclass, inherit, isattr = c
        redeclared = self.lookup(ast.constant.name, c[0], lambda x: x.name)
        if isattr and redeclared: raise Redeclared(Attribute(), redeclared.name)
        elif redeclared: raise Redeclared(Variable(), redeclared.name)
        typ = Attribute() if isattr else Constant()
        if ast.value is not None:
            checkInit = self.visit(ast.value, (memlist + nonlocallist, allclass, inherit, ast))
            if not self.checkAllType(ast.constType, checkInit, allclass): raise TypeMismatchInConstant(ast)
        else: raise IllegalConstantExpression(ast)
        return Symbol(ast.constant.name, MType(None, ast.constType), (typ, Constant()))

    def visitClassDecl(self, ast, c):
        member = []
        parent = None
        if ast.parentname:
            undeclaredParent = self.lookup(ast.parentname.name, c, lambda x: x.name)
            if undeclaredParent is None: raise Undeclared(Class(), ast.parentname.name)
            parent = undeclaredParent
            addclass = Symbol(ast.classname.name, MType((), (ClassType(ast.parentname), ClassType(ast.classname))))
        else: addclass = Symbol(ast.classname.name, MType((), (None, ClassType(ast.classname))))
        addclass.value = member
        c.append(addclass)
        for mem in ast.memlist:
            if isinstance(mem, AttributeDecl):
                member.append(self.visit(mem.decl, (member, [], c, (parent, addclass), True)))
            else:
                self.visit(mem, (member, c, (parent, addclass)))

    def visitMethodDecl(self, ast, c):
        memclass, allclass, inherit = c
        method = self.lookup(ast.name.name, memclass, lambda x: x.name)
        if method: raise Redeclared(Method(), method.name)
        paramlist = []
        locallist = []
        partype = []
        for param in ast.param:
            if param.variable.name in paramlist: 
                raise Redeclared(Parameter(), param.variable.name)
            else: 
                paramlist.append(param.variable.name)
                locallist.append(Symbol(param.variable.name, MType(None, param.varType)))
                partype.append(param.varType)
        method = Symbol(ast.name.name, MType(partype, None))
        memclass.append(method)
        isinloop = False
        for stmt in ast.body.inst:
            if isinstance(stmt, VarDecl):
                locallist.append(self.visit(stmt, (locallist, [], allclass, inherit, False)))
            elif isinstance(stmt, ConstDecl):
                locallist.append(self.visit(stmt, (locallist, [], allclass, inherit, False)))
            elif isinstance(stmt, Expr):
                self.visit(stmt, (locallist, allclass, inherit, stmt))
            else:
                self.visit(stmt, (locallist, allclass, inherit, isinloop, method))
        if method.name == "Constructor": inherit[1].mtype.partype = partype

    def visitProgram(self, ast, c):
        for decl in ast.decl:
            redeclaredClass = self.lookup(decl.classname.name, c, lambda x: x.name)
            if redeclaredClass: raise Redeclared(Class(), redeclaredClass.name)
            self.visit(decl, c)
        entryclass = self.lookup("Program", c, lambda x: x.name)
        mainentry = self.lookup("main", entryclass.value, lambda x: x.name)
        entry = mainentry and not mainentry.mtype.partype and isinstance(mainentry.mtype.rettype, VoidType)
        if not entry: raise NoEntryPoint()



    

