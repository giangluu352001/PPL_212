; HelloWorld.j

; Generated by ClassFileAnalyzer (Can)
; Analyzer and Disassembler for Java class files
; (Jasmin syntax 2, http://jasmin.sourceforge.net)
;
; ClassFileAnalyzer, version 0.7.0 


.bytecode 52.0
.source HelloWorld.java
.class public HelloWorld
.super java/lang/Object

.field x I

.method public <init>()V
  .limit stack 2
  .limit locals 1
  .line 3
  0: aload_0
  1: invokespecial java/lang/Object/<init>()V
  .line 4
  4: aload_0
  5: bipush 10
  7: putfield HelloWorld/x I
  10: return
.end method

.method public main([Ljava/lang/String;)V
  .limit stack 2
  .limit locals 2
  .line 7
  0: getstatic java/lang/System/out Ljava/io/PrintStream;
  3: aload_0
  4: getfield HelloWorld/x I
  7: invokevirtual java/io/PrintStream/println(I)V
  .line 8
  10: aload_0
  11: bipush 100
  13: putfield HelloWorld/x I
  .line 9
  16: return
.end method

