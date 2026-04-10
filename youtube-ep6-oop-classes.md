# 🎥 YouTube Video 6: Object-Oriented Programming (OOP) - Classes & Objects

## [0:00] Hook
**Say this:**
> "If you want to build complex applications, work with frameworks like Django, or understand how real-world software is structured, you *must* understand Object-Oriented Programming. Today, we're diving into the core of OOP: Classes and Objects. This is where Python goes from simple scripts to powerful systems."

## [1:00] Part 1: What is OOP? (The Analogy)
**Say this:**
> "Think of a **Class** as a blueprint for a house. It defines what a house *has* (number of rooms, color) and what it *can do* (open door, turn on lights). An **Object** is an actual house built from that blueprint. You can have many houses (objects) from one blueprint (class)."

## [3:00] Part 2: Defining a Class (The Blueprint)
*(On screen: Code editor)*

**Say this:**
> "In Python, we define a class using the `class` keyword. We'll create a `Car` class."

```python
class Car:
    # Class attribute (shared by all cars)
    wheels = 4

    def __init__(self, make, model, year):
        # Instance attributes (unique to each car object)
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print(f"The {self.make} {self.model}'s engine started.")

    def stop_engine(self):
        self.is_running = False
        print(f"The {self.make} {self.model}'s engine stopped.")

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}, Running: {self.is_running}")
```

## [6:00] Part 3: `__init__` and `self` (The Constructor & The Instance)
**Say this:**
> "The `__init__` method is special. It's the **constructor**, called automatically when you create a new object. It sets up the initial state of your object. And `self`? It's just a reference to the *current object* you're working with. Every method needs it to access the object's attributes."

## [8:00] Part 4: Creating Objects (Building Houses)
**Say this:**
> "Now, let's create some cars from our `Car` blueprint!"

```python
my_car = Car("Toyota", "Camry", 2020)
your_car = Car("Honda", "Civic", 2022)

my_car.display_info()
your_car.display_info()

my_car.start_engine()
my_car.display_info()
```

## [10:00] Part 5: Inheritance (Building on Existing Blueprints)
**Say this:**
> "Inheritance is about reusability. Why build a new blueprint from scratch if you can extend an existing one? Let's create an `ElectricCar` that inherits from `Car`."

```python
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year) # Call parent's constructor
        self.battery_size = battery_size

    def charge(self):
        print(f"The {self.make} {self.model} is charging its {self.battery_size}kWh battery.")

    # Method Overriding (changing parent's behavior)
    def display_info(self):
        super().display_info() # Call parent's display_info
        print(f"  Battery: {self.battery_size}kWh")

my_ev = ElectricCar("Tesla", "Model 3", 2023, 75)
my_ev.display_info()
my_ev.start_engine()
my_ev.charge()
```

## [13:00] Outro & Call to Action
**Say this:**
> "You've just taken a huge leap in your Python journey! Understanding Classes, Objects, `__init__`, `self`, and Inheritance is fundamental for any serious Python developer.
> In Episode 7, we'll continue our OOP journey with **Encapsulation, Polymorphism, and Abstraction**—the other pillars of OOP.

> **Homework:** Create a `Dog` class with `name` and `breed` attributes, and a `bark()` method. Then create a `GoldenRetriever` class that inherits from `Dog`.

> Subscribe and hit the bell so you don't miss the next OOP deep dive!"

---

# 📝 Cheat Sheet for your Video Description

**Title:** Python OOP Tutorial (Ep 6): Classes, Objects, __init__, self & Inheritance Explained

**Description:**
> Unlock the power of Object-Oriented Programming in Python! Episode 6 covers the core concepts of OOP: Classes, Objects, the __init__ constructor, the 'self' keyword, and how to use Inheritance for code reusability. Essential for Backend Devs and anyone building complex applications.
> 
> 🎯 **In this episode:**
> 0:00 - Why OOP is crucial for serious Python development
> 1:00 - Classes vs. Objects: The blueprint and the house
> 3:00 - Defining your first Class: The 'Car' example
> 6:00 - Understanding `__init__` and the `self` keyword
> 8:00 - Creating and interacting with Objects
> 10:00 - Inheritance: Building new classes from existing ones
> 
> 🔗 **Next Episode:** OOP Part 2: Encapsulation, Polymorphism & Abstraction.
> 
> #PythonOOP #PythonClasses #PythonTutorial #BackendDevelopment #LearnPython
