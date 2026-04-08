# Episode 2: Installing Python & Your First Script
# Video: Python Tutorial (Ep 2): Install Python 3.14 & Fix Common Errors

# --- 1. Your First Script ---
greeting = "Hello, Interviewer!"
print(greeting)

# --- 2. Syntax Error (Grammar) ---
# Uncomment the line below to show your viewers what happens when you miss a quote.
# print("This will fail)

# --- 3. Logic Error (The Silent Killer) ---
# You want to add two numbers, but they are strings.

num1 = "10"
num2 = "5"
result = num1 + num2

print("\n--- 3. Logic Error ---")
print(f"Adding {num1} and {num2} results in: {result}")
print("Wait, that's not 15! It's 105 because they are strings.")

# Fixing the Logic Error with type casting:
correct_result = int(num1) + int(num2)
print(f"Corrected Result (int casting): {correct_result}")

# --- 4. Debugging with print() ---
# Interview Scenario: You have a variable that changes, and you need to find where it goes wrong.

balance = 100
item_price = 50

print("\n--- 4. Debugging with print() ---")
print(f"DEBUG: Starting balance is {balance}")

balance -= item_price
print(f"DEBUG: Balance after purchase: {balance}")

# If this was 0 and it shouldn't be, you'd know exactly which line caused it.
