class a():
    num = 10

class b(a):
    pass

class c(a):
    num=1

class d(b,c):
    pass

print(d.num)
print(d.mro())


#Another messy example (We can use __dunder methods instead of mro() as well)

class Y():
    pass
class X():
    pass
class Z():
    pass
class A(X,Y):
    pass
class B(Y,Z):
    pass
class M(B,A,Z):
    pass
print(M.mro())
print(M.__mro__)

#uses algorithm depth search

#Wrinting code and inheriting with MRO is possible but not recommended, it is not a good practice
