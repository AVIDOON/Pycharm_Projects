class Student:
    "I am writing about the properties of vehicle"
    student_no = 0

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
        self.student_no += 1

    def printProperties(self):
        print("Name of the Student is : " , self.name)
        print("Id of the Student is : ", self.id)
        print("Age of the Student is : " , self.age)
        print(Student.__doc__) # Class documentation string or none, if undefined


car = Student('Avinash',1,21)
car.printProperties()
print(hasattr(car,'id'))
print(getattr(car,'id'))
setattr(car,'id',101)
print(getattr(car,'id'))
delattr(car,'id')
print(getattr(car,'id'))
