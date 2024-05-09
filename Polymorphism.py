class Animal:
    def sound(self):
        print("Animaal will walk fastly")
class Dog(Animal):
    def sound(self):
        print("Dog will bark loudly")
class Bird(Animal):
    def sound(self):
        print("Birds will sings")
d = Bird()
d.sound()
