class Parent:
    'This is a parent Class'
    parAttribute = 100

    def __init__(self):
        print('Calling Parent Class Constructor.')

    def parFunction1(self):
        print("Another Parent function is Called.")

    def parFunction2(self,attr):
        self.parAttribute = attr

    def getAttr(self):
        print(self.parAttribute)


class Child(Parent):
    'This is a child Class'

    def __init__(self):
        print("Calling Child Class Constructor.")

    def childFunction1(self):
        print("Another Child function is Called.")


c1 = Child()
p1 = Parent()
c1.parFunction1()
c1.parFunction2(100)
c1.getAttr()
print(issubclass(Child,Parent))
print(isinstance(p1,Child))
