# Episode 4: Data Structures (Lists, Tuples, Dicts, Sets)
# Video: Python Data Structures (Ep 4): Lists, Tuples, Dictionaries & Sets Explained

# --- 1. Lists (Ordered, Changeable, Allows Duplicates) ---
fruits = ["apple", "banana", "cherry"]
fruits.append("date")      # Add to end
fruits[0] = "avocado"      # Change an item

print("--- 1. Lists ---")
print(f"Fruits: {fruits}")
print(f"Number of fruits: {len(fruits)}")


# --- 2. Tuples (Ordered, Unchangeable, Allows Duplicates) ---
# Used for data that should NOT change.
coordinates = (10.0, 20.0)

print("\n--- 2. Tuples ---")
print(f"Coordinates: {coordinates}")
# coordinates[0] = 15.0  # This would raise a TypeError!

# --- 3. Dictionaries (Key-Value Pairs, Ordered, Changeable) ---
# Perfect for fast lookups.
user = {
    "name": "Alex",
    "age": 25,
    "role": "Developer"
}

print("\n--- 3. Dictionaries ---")
print(f"User Name: {user['name']}")
user["age"] = 26  # Update a value
print(f"Updated User: {user}")

# --- 4. Sets (Unordered, No Duplicates) ---
# Great for unique collections.
id_list = [101, 102, 101, 103, 102]
unique_ids = set(id_list)

print("\n--- 4. Sets ---")
print(f"Original IDs (List): {id_list}")
print(f"Unique IDs (Set): {unique_ids}")

# --- 5. Summary Check (Interview Style) ---
print("\n--- 5. Comparison Check ---")
print(f"Is List ordered? Yes. Is Tuple ordered? Yes. Is Set ordered? No.")
print(f"Can List change? Yes. Can Tuple change? No. Can Set change? Yes.")
