class A(object):
    def __init__(self):
        self.a = 40
        self.__b = 30




class B(A):
    def __init__(self):
         A.__init__(self)




a = B()
print(B.a)