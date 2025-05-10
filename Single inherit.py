class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Inheriting from Animal
    def bark(self):
        print("Dog barks")
    

d = Dog()
d.speak()  # Inherited from Animal
d.bark()
