class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

obj = Dog()
cat = Cat()

obj.speak()  # Inherited method
obj.bark()   # Dog's own method

cat.speak()  # Inherited method
cat.meow()   # Cat's own method