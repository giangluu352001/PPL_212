
"""
 * @author nhphung
"""
from tabnanny import check
from AST import * 
from Visitor import *
from StaticError import *

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype
class Symbol:
    def __init__(self, name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
class StaticChecker(BaseVisitor):

    global_envi = []
            
    def __init__(self,ast):
        self.ast = ast
    
    def gettype(self, symbol):
        return symbol.mtype.rettype
    
    def lookup(self,name, lst, typ, func):
        for x in lst:
            if typ is None:
                if name == func(x): return x
            else:
                if isinstance(typ, Attribute):
                    if name == func(x) and x.value and isinstance(x.value[0], Attribute): return x
                elif isinstance(typ, Method):
                    if name == func(x) and x.mtype.partype is not None: return x
                else: 
                    if name == func(x) and x.value and not isinstance(x.value[0], (Attribute, Method)): return x
        return None

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)
        
    def visitId(self, ast, c):
        undeclared = self.lookup(ast.name, c[0], ast, lambda x: x.name)
        if not undeclared: raise Undeclared(Identifier(), ast.name)
        return undeclared
    
    def visitBinaryOp(self, ast, c):
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        def checkType(inputType, outputType = None):
            if not isinstance(self.gettype(left), inputType) or not isinstance(self.gettype(right), inputType):
                raise TypeMismatchInExpression(ast)
            elif outputType: return Symbol("", MType(None, outputType))
            elif isinstance(self.gettype(left), IntType) and isinstance(self.gettype(right), FloatType): return right
            elif isinstance(self.gettype(left), FloatType) and isinstance(self.gettype(right), IntType): return left
            elif isinstance(self.gettype(left), type(self.gettype(right))): return right
            else: raise TypeMismatchInExpression(ast)
        if ast.op in ["+", "-", "*", "/"]:
            sym = checkType((IntType, FloatType))
        elif ast.op in ["<", "<=", ">", ">="]:
            sym = checkType((IntType, FloatType), BoolType())
        elif ast.op == "%": sym = checkType(IntType, IntType())
        elif ast.op in ["!=", "=="]:
            sym = checkType((IntType, BoolType), BoolType())
        elif ast.op in ["&&", "||"]: sym = checkType(BoolType, BoolType())
        elif ast.op == "==.": sym = checkType(StringType, BoolType())
        elif ast.op == "+.": sym = checkType(StringType, StringType())
        if isinstance(c[-2], (ConstDecl, Return)):
            if left.value and isinstance(left.value[1], Constant) and \
            right.value and isinstance(right.value[1], Constant):
                return Symbol("", MType(None, sym.mtype.rettype), (None, Constant()))
            else: return Symbol("", MType(None, sym.mtype.rettype), (None, None))
        return sym

    def visitUnaryOp(self, ast, c):
        exp = self.visit(ast.body, c)
        if ast.op == "!":
            if isinstance(self.gettype(exp), BoolType): return exp
            raise TypeMismatchInExpression(ast)
        elif ast.op == "-":
            if isinstance(self.gettype(exp), (IntType, FloatType)): return exp
            raise TypeMismatchInExpression(ast)
            
    def callfunc(self, ast, c, isExpr):
        if isExpr: locallist, allclass, currentclass, _, method = c
        else: locallist, allclass, currentclass, _, method = c
        error = TypeMismatchInExpression(ast) if isExpr else TypeMismatchInStatement(ast)
        
        def checkAll(name, type):
            access = self.lookup(name, allclass, None, lambda x: x.name) 
            if access:
                return checkCallMethod(ast.method.name, access.value, paramlist)
            else: 
                if type: raise Undeclared(Class(), ast.obj.name)
                else: return False

        def checkCallMethod(name, lst, paramlist):
            func = self.lookup(name, lst, Method(), lambda x: x.name)
            if func is None:
                raise Undeclared(Method(), ast.method.name)
            if isinstance(func.mtype.rettype, VoidType) and isExpr: raise error
            elif not isinstance(func.mtype.rettype, VoidType) and not isExpr: raise error
            elif len(func.mtype.partype) != len(paramlist): raise error
            for i in range(0, len(paramlist)):
                left = func.mtype.partype[i]
                if not self.checkAllType(left, paramlist[i], allclass): raise error
            return func
        
        paramlist = [self.gettype(self.visit(param, (locallist, allclass, \
        currentclass, None, method))) for param in ast.param]
        if ast.method.name[0] == "$":
            check = checkAll(ast.obj.name, False)
            if not check:
                var = self.lookup(ast.obj.name, locallist, None, lambda x: x.name)
                if var is None: raise Undeclared(Class(), ast.obj.name)
                elif isinstance(var, ClassType):
                    attr = self.lookup(ast.method.name, var.value, Attribute(), lambda x: x.name)
                    if attr: raise IllegalMemberAccess(ast)
                else: raise TypeMismatchInExpression(ast)
            else: return check
        else:
            if isinstance(ast.obj, Id):
                undeclared = self.lookup(ast.obj.name, allclass, None, lambda x: x.name)
                if undeclared:
                    attr = self.lookup(ast.method.name, undeclared.value, Method(), lambda x: x.name)
                    if attr: raise IllegalMemberAccess(ast)
            obj = self.visit(ast.obj, c)
            if not isinstance(self.gettype(obj), ClassType): raise TypeMismatchInExpression(ast)
            name = self.gettype(obj).classname.name
            if name == "Self": check = checkAll(currentclass.name, True)
            else: check = checkAll(name, True)
            if isinstance(c[-2], (Return, ConstDecl)):
                if obj.value and isinstance(obj.value[1], Constant) \
                and check.value and isinstance(check.value[1], Constant): return check
                else: return Symbol("", MType(None, check.mtype.rettype), (None, None))
            return check

    def visitCallExpr(self, ast, c):
        if isinstance(c[-1], Symbol) and "$" in c[-1].name and isinstance(ast.obj, SelfLiteral): 
            raise IllegalMemberAccess(ast)
        return self.callfunc(ast, c, True)

    def visitNewExpr(self, ast, c):
        instance = self.lookup(ast.classname.name, c[1], None, lambda x: x.name)
        if instance is None: raise Undeclared(Class(), ast.classname.name)
        paramlist = []
        for param in ast.param:
            paramlist.append(self.gettype(self.visit(param, c)))
        if len(paramlist) != len(instance.mtype.partype):
            raise TypeMismatchInExpression(ast)
        for i in range(0, len(paramlist)):
            if not self.checkPrimitive(instance.mtype.partype[i], paramlist[i]):
                raise TypeMismatchInExpression(ast)
        return Symbol(ast.classname.name, MType(None, ClassType(ast.classname)), (None, Constant()))

    def visitArrayCell(self, ast, c):
        arr = self.visit(ast.arr, c)
        rettype = self.gettype(arr)
        idxlist = [self.visit(x, c) for x in ast.idx]
        if any(not isinstance(self.gettype(idx), IntType) for idx in idxlist) or not isinstance(rettype, ArrayType):
            raise TypeMismatchInExpression(ast)
        nested = len(idxlist)
        for _ in range(nested):
            if not isinstance(rettype, ArrayType):
                rettype = None
                break
            rettype = rettype.eleType
        if isinstance(c[-2], (ConstDecl, Return)):
            if any(idx.value and not isinstance(idx.value[1], Constant) for idx in idxlist):
                return Symbol("", MType(None, rettype), (None, None))
        return Symbol(arr.name, MType(None, rettype), arr.value)

    def visitFieldAccess(self, ast, c):
        locallist, allclass, currentclass, _, method = c
        if isinstance(method, Symbol) and "$" in method.name and isinstance(ast.obj, SelfLiteral): 
            raise IllegalMemberAccess(ast)
        if ast.fieldname.name[0] == "$":
                classname = self.lookup(ast.obj.name, allclass, None, lambda x: x.name)
                if classname is None: 
                    obj = self.lookup(ast.obj.name, locallist, Id(""), lambda x: x.name)
                    if obj is None: raise Undeclared(Class(), ast.obj.name)
                    elif isinstance(self.gettype(obj), ClassType):
                        undeclared = self.lookup(self.gettype(obj).classname.name, allclass, None, lambda x: x.name)
                        attr = self.lookup(ast.fieldname.name, undeclared.value, Attribute(), lambda x: x.name)
                        if attr: raise IllegalMemberAccess(ast)
                    else: raise TypeMismatchInExpression(ast)
                elif classname:
                    checkfield = self.lookup(ast.fieldname.name, classname.value, Attribute(), lambda x: x.name)
                    if not checkfield: raise Undeclared(Attribute(), ast.fieldname.name)
                    return checkfield
        else:
            if isinstance(ast.obj, Id):
                classname = self.lookup(ast.obj.name, allclass, None, lambda x: x.name)
                if classname:
                    undeclared = self.lookup(ast.fieldname.name, classname.value, Attribute(), lambda x: x.name)
                    if undeclared: raise IllegalMemberAccess(ast)
            obj = self.visit(ast.obj, c)
            name = self.gettype(obj).classname.name
            if not isinstance(self.gettype(obj), ClassType): raise Undeclared(Identifier(), ast.obj)
            if name == "Self": checkclass = currentclass
            else: checkclass = self.lookup(name, allclass, None, lambda x: x.name)
            if checkclass is None: raise Undeclared(Class(), name)
            undeclared = self.lookup(ast.fieldname.name, checkclass.value, Attribute(), lambda x: x.name)
            if undeclared is None: raise Undeclared(Attribute(), ast.fieldname.name)
            if isinstance(c[-2], (Return, ConstDecl)):
                if obj.value and isinstance(obj.value[1], Constant) \
                and isinstance(undeclared.value[1], Constant): return undeclared
                else: return Symbol("", MType(None, undeclared.mtype.rettype), (None, None))
            return undeclared
    
    def visitIntLiteral(self, ast, c): return Symbol("", MType(None, IntType()), (None, Constant()))
    
    def visitFloatLiteral(self, ast, c): return Symbol("", MType(None, FloatType()), (None, Constant()))
    
    def visitStringLiteral(self, ast, c): return Symbol("", MType(None, StringType()), (None, Constant()))
    
    def visitBooleanLiteral(self, ast, c): return Symbol("", MType(None, BoolType()), (None, Constant()))

    def visitSelfLiteral(self, ast, c): return Symbol("", MType(None, ClassType(Id("Self"))), (None, Constant()))

    def visitArrayLiteral(self, ast, c):
        size = len(ast.value)
        typ = None
        for i in range(size):
            alltype = self.gettype(self.visit(ast.value[i], c))
            if i == 0: typ = alltype
            else:
                if (isinstance(alltype, ArrayType) and alltype.size == typ.size \
                and isinstance(alltype.eleType, type(typ.eleType))) \
                or (not isinstance(alltype, ArrayType) and isinstance(alltype, type(typ))): continue
                else: raise IllegalArrayLiteral(ast)
        return Symbol("", MType(None, ArrayType(size, typ)), (None, Constant()))

    def visitAssign(self, ast, c):
        locallist, allclass, currentclass, _, method = c
        lhs = self.visit(ast.lhs, (locallist, allclass, currentclass, None, method))
        if lhs.value and isinstance(lhs.value[-1], Constant): raise CannotAssignToConstant(ast)
        elif isinstance(lhs.mtype.rettype, VoidType): raise TypeMismatchInStatement(ast)
        rhs = self.visit(ast.exp, (locallist, allclass, currentclass, ast, method))
        if not self.checkAllType(self.gettype(lhs), self.gettype(rhs), allclass): raise TypeMismatchInStatement(ast)

    def checkPrimitive(self, left, right):
        if isinstance(left, type(right)) or (isinstance(left, FloatType) \
        and isinstance(right, IntType)): return True
        else: return False

    def checkAllType(self, left, right, allclass):
        if isinstance(left, ClassType) and isinstance(right, ClassType):
            if left.classname.name == right.classname.name: return True
        elif isinstance(left, ArrayType) and isinstance(right, ArrayType):
            if right.size == left.size and \
            self.checkAllType(left.eleType, right.eleType, allclass): return True
        else: return self.checkPrimitive(left, right)

    def visitIf(self, ast, c):
        if len(c) == 5: 
            locallist, allclass, currentclass, isinloop, method = c
            isif = None
        else: locallist, allclass, currentclass, isinloop, method, isif = c
        exp = self.visit(ast.expr, (locallist, allclass, currentclass, None, method))
        if not isinstance(self.gettype(exp), BoolType):
            if isinstance(isif, If): return True
            else: raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, (locallist, allclass, currentclass, isinloop, method))
        if ast.elseStmt: 
            if isinstance(ast.elseStmt, If):
                allIf = isif if isinstance(isif, If) else ast
                if self.visit(ast.elseStmt, (locallist, allclass, currentclass, isinloop, method, allIf)):
                    raise TypeMismatchInStatement(allIf)
            else: self.visit(ast.elseStmt, (locallist, allclass, currentclass, isinloop, method))

    def visitFor(self, ast, c):
        locallist, allclass, currentclass, isinloop, method = c
        id = self.visit(ast.id, (locallist, allclass, currentclass, None, method))
        expr1 = self.visit(ast.expr1, (locallist, allclass, currentclass, None, method))
        if id.value and isinstance(id.value[-1], Constant): raise CannotAssignToConstant(Assign(ast.id, ast.expr1))
        expr2 = self.visit(ast.expr2, (locallist, allclass, currentclass, None, method))
        expr3 = self.visit(ast.expr3, (locallist, allclass, currentclass, None, method))
        match = isinstance(self.gettype(id), IntType) and isinstance(self.gettype(expr1), IntType) \
        and isinstance(self.gettype(expr2), IntType) and isinstance(self.gettype(expr3), IntType)
        if not match: raise TypeMismatchInStatement(ast)
        if isinstance(ast.loop, Expr): self.visit(ast.loop, (locallist, allclass, currentclass, None))
        else:
            isinloop = True
            self.visit(ast.loop, (locallist, allclass, currentclass, isinloop, method))

    def visitBreak(self, ast, c):
        if not c[-2]: raise MustInLoop(Break()) 

    def visitContinue(self, ast, c):
        if not c[-2]: raise MustInLoop(Continue())

    def visitReturn(self, ast, c):
        locallist, allclass, currentclass, _, method = c
        if (method.name == "Constructor" and ast.expr is not None) \
        or method.name == "Destructor": raise TypeMismatchInStatement(ast)
        elif method.name == "main" and self.gettype(currentclass).classname.name == "Program" and \
            method.mtype.partype == [] and ast.expr is not None: raise TypeMismatchInStatement(ast)
        elif method.mtype.rettype is None:
            if not ast.expr: method.mtype.rettype = VoidType()
            else: 
                sym = self.visit(ast.expr, (locallist, allclass, currentclass, ast, method))
                method.mtype.rettype = self.gettype(sym)
                method.value = sym.value
        else:
            if not ast.expr and not isinstance(method.mtype.rettype, VoidType):
                raise TypeMismatchInStatement(ast)
            typ = self.visit(ast.expr, (locallist, allclass, currentclass, None, method))
            if not self.checkAllType(method.mtype.rettype, typ, allclass):
                raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast, c):
        return self.callfunc(ast, c, False)

    def visitVarDecl(self, ast, c):
        memlist, nonlocallist, allclass, currentclass, isattr = c
        if isinstance(isattr, Attribute):
            redeclared = self.lookup(ast.variable.name, c[0], Attribute(), lambda x: x.name)
            if redeclared: raise Redeclared(Attribute(), redeclared.name)
        else: redeclared = self.lookup(ast.variable.name, c[0], None, lambda x: x.name)
        if redeclared: raise Redeclared(Variable(), redeclared.name)
        typ = Attribute() if isinstance(isattr, Attribute) else Variable()
        if isinstance(ast.varType, ClassType):
            undeclared = self.lookup(ast.varType.classname.name, allclass, None, lambda x: x.name)
            if not undeclared: raise Undeclared(Class(), ast.varType.classname.name)
        if isinstance(ast.varInit, NullLiteral) and isinstance(ast.varType, ClassType):
            return Symbol(ast.variable.name, MType(None, ast.varType), (typ, None))
        elif ast.varInit is not None:
            checkInit = self.visit(ast.varInit, (memlist + nonlocallist, allclass, currentclass, ast, isattr))
            if not self.checkAllType(ast.varType, self.gettype(checkInit), allclass): raise TypeMismatchInStatement(ast)
        return Symbol(ast.variable.name, MType(None, ast.varType), (typ, None))

    def visitBlock(self, ast, c):
        nonlocallist, allclass, currentclass, isinloop, method = c
        locallist = []
        for inst in ast.inst:
            if isinstance(inst, VarDecl):
                locallist.append(self.visit(inst, (locallist, nonlocallist, allclass, currentclass, method)))
            elif isinstance(inst, ConstDecl):
                locallist.append(self.visit(inst, (locallist, nonlocallist, allclass, currentclass, method)))
            elif isinstance(inst, Expr):
                self.visit(inst, (locallist + nonlocallist, allclass, currentclass, method))
            else:
                self.visit(inst, (locallist + nonlocallist, allclass, currentclass, isinloop, method))

    def visitConstDecl(self, ast, c):
        memlist, nonlocallist, allclass, currentclass, isattr = c
        if isinstance(isattr, Attribute):
            redeclared = self.lookup(ast.constant.name, c[0], Attribute(), lambda x: x.name)
            if redeclared: raise Redeclared(Attribute(), redeclared.name)
        else: redeclared = self.lookup(ast.constant.name, c[0], None, lambda x: x.name)
        if redeclared: raise Redeclared(Variable(), redeclared.name)
        typ = Attribute() if isinstance(isattr, Attribute) else Constant()
        if isinstance(ast.constType, ClassType):
            undeclared = self.lookup(ast.constType.classname.name, allclass, None, lambda x: x.name)
            if not undeclared: raise Undeclared(Class(), ast.constType.classname.name)
        if ast.value is not None:
            checkInit = self.visit(ast.value, (memlist + nonlocallist, allclass, currentclass, ast, isattr))
            if checkInit.value and not isinstance(checkInit.value[1], Constant): raise IllegalConstantExpression(ast.value)
            elif not self.checkAllType(ast.constType, self.gettype(checkInit), allclass): raise TypeMismatchInConstant(ast)
        else: raise IllegalConstantExpression(None)
        return Symbol(ast.constant.name, MType(None, ast.constType), (typ, Constant()))

    def visitClassDecl(self, ast, c):
        member = []
        if ast.parentname:
            undeclaredParent = self.lookup(ast.parentname.name, c, None, lambda x: x.name)
            if undeclaredParent is None: raise Undeclared(Class(), ast.parentname.name)
        addclass = Symbol(ast.classname.name, MType((), ClassType(ast.classname)))
        addclass.value = member
        c.append(addclass)
        for mem in ast.memlist:
            if isinstance(mem, AttributeDecl):
                member.append(self.visit(mem.decl, (member, [], c, addclass, Attribute())))
            else:
                self.visit(mem, (member, c, addclass))

    def visitMethodDecl(self, ast, c):
        memclass, allclass, currentclass = c
        method = self.lookup(ast.name.name, memclass, Method(), lambda x: x.name)
        if method: 
            if method.name in ["Constructor", "Destructor"]: raise Redeclared(SpecialMethod(), method.name)
            else: raise Redeclared(Method(), method.name)
        paramlist = []
        locallist = []
        partype = []
        for param in ast.param:
            if param.variable.name in paramlist: 
                raise Redeclared(Parameter(), param.variable.name)
            else: 
                paramlist.append(param.variable.name)
                locallist.append(Symbol(param.variable.name, MType(None, param.varType), (Parameter(), None)))
                partype.append(param.varType)
        method = Symbol(ast.name.name, MType(partype, None), (Method(), None))
        memclass.append(method)
        isinloop = False
        for stmt in ast.body.inst:
            if isinstance(stmt, VarDecl):
                locallist.append(self.visit(stmt, (locallist, [], allclass, currentclass, method)))
            elif isinstance(stmt, ConstDecl):
                locallist.append(self.visit(stmt, (locallist, [], allclass, currentclass, method)))
            elif isinstance(stmt, Expr):
                self.visit(stmt, (locallist, allclass, currentclass, stmt, method))
            else:
                self.visit(stmt, (locallist, allclass, currentclass, isinloop, method))
        if method.mtype.rettype is None: method.mtype.rettype = VoidType()
        if method.name == "Constructor": currentclass.mtype.partype = partype

    def visitProgram(self, ast, c):
        c = []
        for decl in ast.decl:
            redeclaredClass = self.lookup(decl.classname.name, c, None, lambda x: x.name)
            if redeclaredClass: raise Redeclared(Class(), redeclaredClass.name)
            self.visit(decl, c)
        entry = None
        entryclass = self.lookup("Program", c, None, lambda x: x.name)
        if entryclass:
            mainentry = self.lookup("main", entryclass.value, Method(), lambda x: x.name)
            entry = mainentry and not mainentry.mtype.partype and isinstance(mainentry.mtype.rettype, VoidType)
        if not entry: raise NoEntryPoint()



    

