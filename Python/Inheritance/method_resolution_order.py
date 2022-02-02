class A:
    pass
class B:
    pass
class C:
    pass
class X(A,B):
    pass
class Y(B,C):
    pass
class P(X,Y):
    pass

print(A.mro())
print(B.mro())
print(C.mro())
print(X.mro())
print(Y.mro())
print(P.mro())
