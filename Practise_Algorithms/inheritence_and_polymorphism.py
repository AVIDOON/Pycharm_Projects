class Vehicle():
    def __init__(self):
        print('They helps in travelling.')
        print('They can accelerate.')

class Car(Vehicle):
    def design(self):
        print('Cars come in beautiful design.')
    def speed(self):
        print('They can go over speed of 100kmph.')
    def cost(self):
        print('They are costly hence unaffordable.')

class Bus(Vehicle):
    def transport(self):
        print('They are used as a public Transport.')
    def speed(self):
        print('They can go over speed of 100kmph.')

if __name__ == '__main__':
        car = Car()
        car.design()
        car.speed()
        car.cost()

        bus = Bus()
        bus.transport()
        bus.speed()