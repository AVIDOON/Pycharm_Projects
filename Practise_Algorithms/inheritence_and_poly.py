class Animal():
    def __init__(self):
        print('They have four legs\n')
        print('They can run.')

class Dog(Animal):
    def fetch(self):
        print('Dogs can fetch bones.')
    def bark(self):
        print('Dogs can bark.')
    def fond_of_love(self):
        print('Dogs are fond of love.')

class Cat(Animal):
    def meow(self):
        print('Cats can meow.')
    def fond_of_love(self):
        print('Cats are fond of love.')

if __name__ == '__main__':
        dog = Dog()
        dog.fetch()
        dog.bark()
        dog.fond_of_love()

        cat = Cat()
        cat.meow()
        cat.fond_of_love()