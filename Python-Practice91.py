# 85_python_oop_advanced.py
# Advanced OOP - 10 practical programs/features
from abc import ABC, abstractmethod

class Student:
    college = "RK University"
    def __init__(self, name): self.name = name
    @classmethod
    def change_college(cls, name): cls.college = name

s = Student("Prashant")
Student.change_college("Engineering College")
print("1. Class method:", s.college)

class Calculator:
    @staticmethod
    def add(a, b): return a + b
print("2. Static method:", Calculator.add(10, 20))

class Temperature:
    def __init__(self, celsius): self._celsius = celsius
    @property
    def celsius(self): return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15: raise ValueError("Below absolute zero")
        self._celsius = value

t = Temperature(25); t.celsius = 30
print("3. Property:", t.celsius)

class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return 3.14159 * self.radius ** 2

print("4. Abstract class:", round(Circle(5).area(), 2))

class Camera:
    def click(self): return "Photo captured"
class GPS:
    def locate(self): return "Location found"
class Smartphone(Camera, GPS): pass
phone = Smartphone()
print("5. Multiple inheritance:", phone.click(), "|", phone.locate())

class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, other): return Point(self.x + other.x, self.y + other.y)
    def __repr__(self): return f"Point({self.x}, {self.y})"
print("6. Operator overloading:", Point(2, 3) + Point(4, 5))

class Product:
    def __init__(self, code): self.code = code
    def __eq__(self, other):
        return isinstance(other, Product) and self.code == other.code
print("7. Custom equality:", Product("P101") == Product("P101"))

class Engine:
    def start(self): return "Engine started"
class Car:
    def __init__(self): self.engine = Engine()
    def start(self): return self.engine.start()
print("8. Composition:", Car().start())

class BankAccount:
    def __init__(self, balance): self.__balance = balance
    def deposit(self, amount):
        if amount > 0: self.__balance += amount
    def get_balance(self): return self.__balance
account = BankAccount(1000); account.deposit(500)
print("9. Encapsulation:", account.get_balance())

class User:
    def __init__(self, name, age): self.name, self.age = name, age
    def __repr__(self): return f"User(name={self.name!r}, age={self.age})"
print("10. Object representation:", User("Prashant", 20))
