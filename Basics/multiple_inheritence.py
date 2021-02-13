class A(object):
   def __init__(self):
        super(A,self).__init__()
        print("a function is called")


class B(object):
    def __init__(self):
        super(B, self).__init__()
        print("b function is called")


class C(B,A):
    def __init__(self):
        super(C, self).__init__()
        print("c function is called")

C()


