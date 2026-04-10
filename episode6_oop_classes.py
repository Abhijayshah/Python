# Episode 6: Object-Oriented Programming (OOP) - Classes & Objects
# Video: Python OOP Tutorial (Ep 6): Classes, Objects, __init__, self & Inheritance Explained

# --- 1. Defining a Class (The Blueprint) ---
class Car:
    # Class attribute: shared by all instances of Car
    wheels = 4

    def __init__(self, make, model, year):
        # Instance attributes: unique to each Car object
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False # Default state

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.make} {self.model}'s engine started.")
        else:
            print(f"The {self.make} {self.model}'s engine is already running.")

    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.make} {self.model}'s engine stopped.")
        else:
            print(f"The {self.make} {self.model}'s engine is already off.")

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}, Running: {self.is_running}, Wheels: {Car.wheels}")

# --- 2. Creating Objects (Building Houses) ---
print("--- 2. Creating Objects ---")
my_car = Car("Toyota", "Camry", 2020)
your_car = Car("Honda", "Civic", 2022)

my_car.display_info()
your_car.display_info()

my_car.start_engine()
my_car.display_info()
my_car.stop_engine()
my_car.display_info()

# --- 3. Inheritance (Building on Existing Blueprints) ---
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        # Call the constructor of the parent class (Car)
        super().__init__(make, model, year) 
        self.battery_size = battery_size # New attribute for ElectricCar

    def charge(self):
        print(f"The {self.make} {self.model} is charging its {self.battery_size}kWh battery.")

    # Method Overriding: Changing the behavior of a parent method
    def display_info(self):
        super().display_info() # Call parent's display_info first
        print(f"  Battery: {self.battery_size}kWh")

print("\n--- 3. Inheritance ---")
my_ev = ElectricCar("Tesla", "Model 3", 2023, 75)
my_ev.display_info()
my_ev.start_engine()
my_ev.charge()
my_ev.stop_engine()

# Demonstrate class attribute
print(f"\nAll cars have {Car.wheels} wheels.")
print(f"My EV also has {my_ev.wheels} wheels (inherited).")
