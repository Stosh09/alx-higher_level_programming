class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, How are you', self.name)


p = Person('Stosh')
p.say_hi()
