# Multiple inheritance
class A:
    varA = "I am A"
class B:
    varB = "I am B"
class C(A,B):
    varC = "I am C"

c = C()
print(c.varA)
print(c.varB)
print(C.varC)  