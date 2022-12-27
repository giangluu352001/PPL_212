'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from turtle import rt
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
import copy

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName))
                    
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class StringType(Type):
    
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, o):
        #ast: Program
        #o: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        for x in ast.decl:
            e = self.visit(x, e)
        # generate default constructor
        self.genMETHOD(MethodDecl(Id("<init>"), list(), None, Block(list(), list())), o, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return o

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))

    def visitId(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        sym = next(filter(lambda y: y.name == ast.name, ctxt.sym), False)
        if ctxt.isLeft:
            if type(sym.value) is Index:
                code = self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, frame)
            else:
                code = self.emit.emitPUTSTATIC(sym.value.value + "/" + sym.name, sym.mtype, frame)
        else:
            if type(sym.value) is Index:
                code = self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, frame)
            else:
                code = self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name, sym.mtype, frame)
        typ = sym.mtype
        return code, typ
                
    
    def visitBinaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        rt = e1t
        if type(e1t) is IntType and type(e2t) is FloatType: 
            e1c = e1c + self.emit.emitI2F(frame)
            rt = e2t
        elif type(e2t) is IntType and type(e1t) is FloatType: 
            r2t = r2t + self.emit.emitI2F(frame)
            rt = e1t
        if ast.op in ["+", "-"]:
            code = self.emit.emitADDOP(ast.op, rt, frame)
        elif ast.op in ["*", "/"]:
            code = self.emit.emitMULOP(ast.op, rt, frame)
        elif ast.op == "+.":
            code = self.emit.emitADDOP(ast.op[0], rt, frame)
        elif ast.op == "%":
            code = self.emit.emitMOD(ast.op, rt, frame)
            rt = IntType()
        elif ast.op in [">", "<", ">=", "<=", "!=", "=="]:
            code = self.emit.emitREOP(ast.op, rt, frame)
            rt = BoolType()
        return e1c + e2c + code, rt

    def visitUnaryOp(self, ast, o):
        ctxt = o
        frame = ctxt. frame
        ec, et = self.visit(ast.body, o)
        if ast.op == "-": return ec + self.emit.emitNEGOP(et, frame), et
        elif ast.op == "!": return ec + self.emit.emitNOT(et, frame), et
        
    def visitCallExpr(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym
        return self.call(ast, frame, sym, isExpr = True)

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

    def visitArrayCell(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym
        ec, et = self.visit(ast.arr, Access(frame, sym, True, True))
        ic, it = [self.visit(idx, Access(frame, sym, False, True)) for idx in ast.idx]
        for i in range(len(ic)):
            ec = ec + ic[i] + self.emit.emitALOAD(ec.eleType, frame)
        return ec, ec.eleType

    def visitFieldAccess(self, ast, c):
        pass
    def visitIntLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()
    
    def visitFloatLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value), frame), FloatType()
    
    def visitStringLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()
    
    def visitBooleanLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()

    def visitArrayLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym
        for val in ast.value:
            rc, _ = self.visit(val, Access(frame, sym, True, False))
            self.emit.printout(rc)
            self.emit.emitDUP(frame)

    def visitAssign(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        rc, _ = self.visit(ast.exp, Access(frame, nenv, False, True))
        self.emit.printout(rc)
        lc, _ = self.visit(ast.lhs, Access(frame, nenv, True, True))
        self.emit.printout(lc)

    def visitIf(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        ec, _ = self.visit(ast.expr, Access(frame, nenv, False, True))
        self.emit.printout(ec)
        falseLabel = frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(falseLabel, frame))
        isReturned = self.visit(ast.thenStmt, o)
        if ast.elseStmt:
            nextLabel = frame.getNewLabel()
            self.emit.printout(self.emit.emitGOTO(nextLabel, frame))
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
            isReturned = self.visit(ast.elseStmt, o)
            self.emit.printout(self.emit.emitLABEL(nextLabel, frame))
        else:
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
        return isReturned
        
    def visitFor(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        ec1, _ = self.visit(ast.expr1, Access(frame, nenv, False, True))
        ec2, _ = self.visit(ast.expr2, Access(frame, nenv, False, True))
        lhsWrite, _ = self.visit(ast.id, Access(frame, nenv, True, True))
        lhsRead, _ = self.visit(ast.id, Access(frame, nenv, False, False))
        labelStart = frame.getNewLabel()
        labelEnd = frame.getNewLabel()
        self.emit.printout(ec1)
        self.emit.printout(lhsWrite)
        o.frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelStart, frame))
        self.emit.printout(lhsRead)
        self.emit.printout(ec2)
        up = int(ec1) <= int(ec2) 
        if up: self.emit.printout(self.emit.emitIFICMPGT(labelEnd, frame))
        else:
            self.emit.printout(self.emit.emitIFICMPLT(labelEnd, frame))
        isReturned = self.visit(ast.loop, o)
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        self.emit.printout(lhsRead)
        if ast.expr3:
            ec3, _ = self.visit(ast.expr3, Access(frame, nenv, False, True))
            self.emit.printout(self.emit.emitPUSHICONST(ec3, frame))
        else: self.emit.printout(self.emit.emitPUSHICONST(1, frame))
        self.emit.printout(self.emit.emitADDOP("+" if up else "-", IntType(), frame))
        self.emit.printout(lhsWrite)
        if not isReturned:
            self.emit.printout(self.emit.emitGOTO(labelStart, frame))
        self.emit.printout(self.emit.emitLABEL(labelEnd, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitBreak(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinue(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

    def visitReturn(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        rettype = frame.returnType
        if not type(rettype) is VoidType:
            rc, rt = self.visit(ast.expr, Access(frame, nenv, False, True))
            if type(rettype) is FloatType and type(rt) is IntType:
                rc = rc + self.emit.emitI2F(frame)
            self.emit.printout(rc)
        self.emit.printout(self.emit.emitRETURN(rettype, frame))
        return True
        
    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym
        return self.call(ast, frame, sym, isExpr = False)

    def call(self, ast, frame, sym, isExpr):
        sym = next(filter(lambda x: x.name == ast.method.name, sym), False)
        cname = sym.value.value
        ctype = sym.mtype
        params = ctype.partype
        idx = 0
        for param in ast.param:
            ec, et = self.visit(param, Access(frame, sym, False, True))
        if type(params[idx]) is FloatType and type(et) is IntType:
            ec = ec + self.emit.emitI2F(frame)
        
    def visitVarDecl(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym
        if ast.varInit:
            rc, _ = self.visit(ast.varInit, Access(frame, sym, False, False))
        if frame is None:
            self.emit.printout(self.emit.emitATTRIBUTE(ast.variable.name, ast.varType, False, rc))
            return Symbol(ast.variable.name, ast.varType, CName(self.className))
        else:
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, ast.variable.name, ast.varType, frame.getStartLabel(), frame.getEndLabel()))
            return Symbol(ast.varible.name, ast.varType, Index(idx))

    def visitBlock(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym
        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        for inst in ast.inst: self.visit(inst, o)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
        
    def visitConstDecl(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym
        if ast.value:
            rc, _ = self.visit(ast.value, Access(frame, sym, False, False))
        if frame is None:
            self.emit.printout(self.emit.emitATTRIBUTE(ast.constant.name, ast.constType, True, rc))
            return Symbol(ast.constant.name, ast.constType, CName(self.className))
        else:
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, ast.variable.name, ast.varType, frame.getStartLabel(), frame.getEndLabel()))
            return Symbol(ast.varible.name, ast.varType, Index(idx))
    
    def visitAttributeDecl(self, ast, o):
        c = copy.deepcopy(o)
        c.frame = None
        self.visit(ast.decl, c)
    
    def visitClassDecl(self, ast, o):
        self.className = ast.classname.name
        parentname = ast.parentname.name if ast.parentname else "java.lang.Object"
        self.emit.printout(self.emit.emitPROLOG(self.className, parentname))   
        for mem in ast.memlist: self.visit(mem, o)
        self.emit.emitEPILOG()
    def visitMethodDecl(self, ast, o):
         #ast: FuncDecl
        #o: Any

        subctxt = o
        frame = Frame(ast.method.name, subctxt.frame.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)
        return SubBody(None, [Symbol(ast.name, MType(list(), subctxt.frame.returnType), CName(self.className))] + subctxt.sym)

    
