# Episode 5: File Handling (TXT, CSV, JSON)
# Video: Python File Handling (Ep 5): Reading & Writing Files Explained

import csv
import json
import os

# --- 1. Working with TXT Files (The 'with' Statement) ---
print("--- 1. TXT Files ---")
with open("test.txt", "w") as f:
    f.write("Hello, World! This is Python File Handling.\n")
    f.write("Always use the 'with' statement for safer code.")

with open("test.txt", "r") as f:
    content = f.read()
    print(f"File content: {content}")

# --- 2. Working with CSVs (The csv module) ---
print("\n--- 2. CSV Files ---")
csv_file = "sample_data.csv"

# Reading a CSV file
if os.path.exists(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        # Skip header if needed: next(reader)
        for row in reader:
            print(f"Row: {row}")

# Writing to a CSV file
with open("output.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Score"])
    writer.writerow(["Alex", 95])
    writer.writerow(["Sarah", 100])

print("New CSV 'output.csv' has been created.")

# --- 3. Working with JSON (The json module) ---
print("\n--- 3. JSON Files ---")
json_file = "sample_data.json"

# Reading a JSON file into a Python Dictionary
if os.path.exists(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
        print(f"JSON Data: {data}")
        print(f"First user name: {data['users'][0]['name']}")

# Writing a Dictionary to a JSON file
user_profile = {"username": "dev_alex", "status": "active", "points": 500}
with open("user_profile.json", "w") as file:
    json.dump(user_profile, file, indent=4)

print("New JSON 'user_profile.json' has been created.")

# --- 4. Interview Tip: Appending vs Writing ---
print("\n--- 4. Appending to Files ---")
with open("log.txt", "a") as f:
    f.write("Log Entry: New user logged in.\n")

print("Appended a new line to 'log.txt'. Check it out!")
