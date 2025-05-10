# 1. Using self
class Learner:
    def _init_(self, full_name, score):
        self.full_name = full_name
        self.score = score

learner = Learner("Sana Jameel", 78)
print(learner.full_name)
print(learner.score)
print(f"My name is {learner.full_name} and I scored {learner.score} in Python Programming.")

# 2. Using cls
class Tracker:
    instances = 0
    def _init_(self):
        Tracker.instances += 1

    @classmethod
    def total_created(cls):
        return cls.instances

t1 = Tracker()
t2 = Tracker()
t3 = Tracker()
t4 = Tracker()
print('Total tracker instances created:', Tracker.total_created())

# 3. Public Variables and Methods
class Laptop:
    def _init_(self, brand):
        self.brand = brand

    def boot(self):
        self.status = "Booted"
        print("Laptop is now on")

laptop = Laptop("Dell")
print(laptop.brand)
laptop.boot()
print(f"My laptop is a {laptop.brand} and it is currently {laptop.status}.")
laptop.boot()

# 4. Class Variables and Class Methods
class University:
    name = "National University"

    @classmethod
    def rename(cls, new_name):
        cls.name = new_name

    def display_name(self):
        return self.name

u1 = University()
u2 = University()

University.rename("Tech Valley Institute")

print(u1.display_name())
print(u2.display_name())

# 5. Static Variables and Static Methods
class Calculator:
    @staticmethod
    def multiply(x, y):
        return x * y

print(Calculator.multiply(3, 4))
print(Calculator.multiply(7, 6))
print(Calculator.multiply(2, 9))

# 6. Constructors and Destructors
class Alert:
    def _init_(self, text):
        self.text = text
        print(f"Constructor activated: {self.text}")

alert = Alert("Alert system initialized!")
print("Message:", alert.text)

# 7. Access Modifiers
class Manager:
    def _init_(self, emp_name):
        self.emp_name = emp_name
        self._bonus = 10000
        self.__password = "secret123"

mgr = Manager("Syeda Nameera")
print("Public:", mgr.emp_name)
print("Protected:", mgr._bonus)
print("Private:", mgr.Manager_password)

# 8. The super() Function
class Human:
    def _init_(self, name):
        self.name = name

class Doctor(Human):
    def _init_(self, name, field):
        super()._init_(name)
        self.field = field

doc = Doctor("Dr. Sana", "Cardiology")
print(f'My doctor is {doc.name}, and she specializes in {doc.field}.')

# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"

pet = Dog()
print(pet.sound())

# 10. Instance Methods
class Cat:
    def _init_(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        print(f"{self.name} says Meow!")

cat = Cat("Luna", "gray")
print(f"{cat.name} is a {cat.color} cat.")
cat.meow()

# 11. Class Methods
class Library:
    books_count = 0
    def _init_(self):
        Library.books_count += 1

    @classmethod
    def count_books(cls):
        return f"Total books registered: {cls.books_count}"

for _ in range(7):
    Library()

print(Library.count_books())

# 12. Static Methods
class Converter:
    @staticmethod
    def km_to_miles(km):
        return km * 0.621371

print(f"10 km is equal to {Converter.km_to_miles(10)} miles")

# 13. Composition
class Battery:
    def supply_power(self):
        return "Battery is supplying power"

class Mobile:
    def _init_(self, battery):
        self.battery = battery

    def power_on(self):
        return self.battery.supply_power()

power_unit = Battery()
phone = Mobile(power_unit)
print(phone.power_on())

# 14. Aggregation
class Team:
    def _init_(self, team_name):
        self.team_name = team_name

    def get_team_name(self):
        return self.team_name

class Player:
    def _init_(self, player_name, team):
        self.player_name = player_name
        self.team = team

team = Team("Warriors")
player = Player("Zain", team)
print(f"Player {player.player_name} is in team {player.team.get_team_name()}.")

# 15. Method Resolution Order (MRO)
class X:
    def show(self):
        return "X class"

class Y(X):
    def show(self):
        return "Y class"

class Z(X):
    def show(self):
        return "Z class"

class M(Y, Z):
    def show(self):
        return "M class"

m = M()
print(m.show())

# 16. Function Decorators
def trace(func):
    def wrapper(*args, **kwargs):
        print("Executing function...")
        return func(*args, **kwargs)
    return wrapper

@trace
def greet():
    return "Greetings!"

print(greet())

# 17. Class Decorators
def inject_hello(cls):
    def hello(self):
        return "Hello from class decorator!"
    cls.hello = hello
    return cls

@inject_hello
class Developer:
    def _init_(self, username):
        self.username = username

dev = Developer("syeda.dev")
print(dev.username)
print(dev.hello())

# 18. Property Decorators
class Item:
    def _init_(self, cost):
        self.__cost = cost

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        self.__cost = value

    @cost.deleter
    def cost(self):
        del self.__cost

item = Item(500)
print(item.cost)
item.cost = 750
print(item.cost)
del item.cost
print("Item cost deleted.")

# 19. callable() and _call_()
class Divider:
    def _init_(self, divisor):
        self.divisor = divisor

    def _call_(self, num):
        return num / self.divisor

div = Divider(2)
print(div(10))
print(callable(div))

# 20. Custom Exception
class UnderAgeError(Exception):
    pass

def validate_age(age):
    if age < 21:
        raise UnderAgeError("User must be 21 or older.")
    return "Access granted"

try:
    print(validate_age(17))
except UnderAgeError as e:
    print(f"Error: {e}")

try:
    print(validate_age(25))
except UnderAgeError as e:
    print(f"Error: {e}")

# 21. Make a Custom Class Iterable
class EvenCounter:
    def _init_(self, max_val):
        self.current = 0
        self.max_val = max_val

    def _iter_(self):
        return self

    def _next_(self):
        if self.current > self.max_val:
            raise StopIteration
        val = self.current
        self.current += 2
        return val

print("Even numbers up to 10:")
for num in EvenCounter(10):
    print(num)