# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#
#     def display(self):
#         print(self.name)
#         print(self.salary)
#
# emp = Employee("Avinash", 10000)
# emp.display()


class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self._salary = salary

    def display(self):
        print(self.__name)
        print(self._salary)

emp = Employee("Avinash", 10000)
print(emp._salary)
# print(emp.__name)

