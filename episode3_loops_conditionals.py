# Episode 3: Loops & Conditionals
# Video: Python Tutorial (Ep 3): Mastering if/else, for, while & FizzBuzz

# --- 1. The 'if' Statement (Decision Making) ---
score = 85

print("--- 1. if/elif/else ---")
if score >= 90:
    print(f"Score: {score}. Grade: A")
elif score >= 80:
    print(f"Score: {score}. Grade: B")
else:
    print(f"Score: {score}. Keep practicing!")

# --- 2. The 'for' Loop & range() ---
# range(start, stop, step)

print("\n--- 2. for loop & range() ---")
print("Counting by 2s up to 10:")
for i in range(2, 11, 2):
    print(f"i: {i}")

# --- 3. The 'while' Loop ---
print("\n--- 3. while loop ---")
countdown = 5
while countdown > 0:
    print(f"T-minus: {countdown}")
    countdown -= 1  # Crucial! Avoid infinite loops.
print("Blast off!")

# --- 4. The Famous FizzBuzz Challenge ---
# Print numbers 1-20. 
# Divisible by 3 -> Fizz
# Divisible by 5 -> Buzz
# Divisible by both -> FizzBuzz

print("\n--- 4. FizzBuzz Challenge ---")
for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num}: FizzBuzz")
    elif num % 3 == 0:
        print(f"{num}: Fizz")
    elif num % 5 == 0:
        print(f"{num}: Buzz")
    else:
        print(num)

# --- 5. Break & Continue ---
print("\n--- 5. Break & Continue ---")
print("Skip number 2 and stop at number 4:")
for i in range(1, 6):
    if i == 2:
        print("Skipping 2 (continue)")
        continue
    if i == 4:
        print("Stopping at 4 (break)")
        break
    print(f"Current i: {i}")
