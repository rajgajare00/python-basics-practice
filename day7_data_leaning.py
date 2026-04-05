# Day 7 - Data Cleaning & Insights
# Raj Gajare | Prime 2.0

import json

# ✅ Part 1 - JSON Data Clean karo
raw_data = [
    {"name": "Raj", "age": 20, "marks": 85, "city": "Nagpur"},
    {"name": "Amit", "age": None, "marks": 92, "city": "Mumbai"},
    {"name": "Priya", "age": 21, "marks": None, "city": "Pune"},
    {"name": "Riya", "age": 22, "marks": 95, "city": None},
    {"name": "Sam", "age": 20, "marks": 78, "city": "Delhi"}
]

print("=== Raw Data ===")
for d in raw_data:
    print(d)

# Missing values clean karo
cleaned = []
for d in raw_data:
    clean_entry = {
        "name": d["name"],
        "age": d["age"] if d["age"] else 21,        # default age
        "marks": d["marks"] if d["marks"] else 0,   # default marks
        "city": d["city"] if d["city"] else "Unknown"
    }
    cleaned.append(clean_entry)

print("\n=== Cleaned Data ===")
for d in cleaned:
    print(d)

# ✅ Part 2 - Meaningful Insights
print("\n=== Insights ===")

# Average marks
avg_marks = sum(d["marks"] for d in cleaned) / len(cleaned)
print(f"Average Marks: {avg_marks:.2f}")

# Topper
topper = max(cleaned, key=lambda x: x["marks"])
print(f"Topper: {topper['name']} with {topper['marks']} marks")

# City wise students
cities = {}
for d in cleaned:
    city = d["city"]
    cities[city] = cities.get(city, 0) + 1
print(f"City Distribution: {cities}")

# Passing students (marks > 80)
passing = [d["name"] for d in cleaned if d["marks"] > 80]
print(f"Passing Students: {passing}")

# JSON file mein save karo
with open("cleaned_data.json", "w") as f:
    json.dump(cleaned, f, indent=4)
print("\nCleaned data saved to cleaned_data.json!")