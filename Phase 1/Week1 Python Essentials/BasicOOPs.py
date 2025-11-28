# creating class and objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
# creating an object of the Dog class
my_dog = Dog("Buddy", 3)
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
print(my_dog.bark())

# Inheritance example
class Animal:
    def speak(self):
        return "Animal sound"
class Cat(Animal):
    def speak(self):
        return "Meow"
my_cat = Cat()
print(f"My cat says: {my_cat.speak()}")

# Encapsulation example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(f"Current balance: {account.get_balance()}")

# Polymorphism example
# Define a class 'Cat' with a method 'speak'
class Cat:
    def speak(self):
        return "Meow"  # Returns the sound a cat makes

# Define a class 'Dog' with a method 'speak'
class Dog:
    def speak(self):
        return "Woof"  # Returns the sound a dog makes

# Create a list containing objects of both classes
animals = [Cat(), Dog()]

# Loop through each animal object in the list
for animal in animals:
    # Call the 'speak' method on each object
    # This demonstrates polymorphism — both classes have the same method name but different behaviors
    print(animal.speak())

# Output:
# Meow
# Woof

# Abstraction example
from abc import ABC, abstractmethod 
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
rect = Rectangle(5, 10)
print(f"Area of rectangle: {rect.area()}")

# static and class methods
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b
print(f"Addition: {MathOperations.add(5, 3)}")
print(f"Multiplication: {MathOperations.multiply(5, 3)}")

# Exploring special methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
print(p3)
print(f"String representation: {p3}")
