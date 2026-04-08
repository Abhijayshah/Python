# Episode 1: Python Intro & Interview Roadmap
# Video: Python Tutorial for Interviews (Ep 1)

# --- 1. Variables & Data Types ---
# In Python, we don't need 'let', 'const', or 'int'. Just: name = value

name = "Alex"          # String (Text)
age = 25               # Integer (Whole number)
price = 19.99          # Float (Decimal)
is_student = True      # Boolean (True/False)

print("--- 1. Variables ---")
print(f"Name: {name}, Age: {age}, Price: {price}, Student: {is_student}")

# --- 2. The type() function ---
# Interviewers often ask how to check a variable's type at runtime.

print("\n--- 2. Checking Types ---")
print(f"Type of name: {type(name)}")   # <class 'str'>
print(f"Type of age: {type(age)}")     # <class 'int'>
print(f"Type of price: {type(price)}") # <class 'float'>

# --- 3. Dynamic Typing ---
# This is Python's superpower. A variable can change its type.

print("\n--- 3. Dynamic Typing ---")
data = 10
print(f"Data is {data}, Type: {type(data)}")

data = "Hello"  # Re-assigning to a string
print(f"Data is now '{data}', Type: {type(data)}")

# --- 4. Interview Question: Indentation ---
# This code will run because it's properly indented.

def indentation_demo():
    if True:
        print("\n--- 4. Indentation ---")
        print("This line is inside the 'if' block because of the 4 spaces.")
    print("This line is outside the 'if' block but inside the function.")

indentation_demo()

# Tip for your video:
# Try deleting the spaces before the print() inside the 'if' block
# to show your audience the 'IndentationError'.
