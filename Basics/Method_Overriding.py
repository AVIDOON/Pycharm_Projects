# Overriding my_method function
class Parent:
    def my_method(self):
        print("Calling Parent Class Method")

class Child(Parent):
    def my_method(self):
        print("Calling Child Class Method")

c1 = Child()
c1.my_method()