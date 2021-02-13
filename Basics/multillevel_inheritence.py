class A:
    def a(self):
         print("a function is called")


class B(A):
    def b(self):
        print("b function is called")


class C(B):
    def c(self):
        print("c function is called")

c1 = C()
c1.a()
c1.b()
c1.c()


