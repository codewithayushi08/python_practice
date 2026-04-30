# Day 4- Dictionaries and Sets

# ----------------------
# DICTIONARY BASICS
# ----------------------

info = {
    "key": "value",
    "name": "sai",
    "learning": "coding",
    "age": 35,
    "is_adult": True,
    "marks": 94.4,
    "subjects": ["python", "c", "java"],
    "topics": ("dict", "set")
}

print("Type:", type(info))

# Modify dictionary
info["name"] = "ayushi"
info["surname"] = "das"

print("Updated info:", info)
print("Name:", info["name"])
print("Subjects:", info["subjects"])

# ----------------------
# NESTED DICTIONARY
# ----------------------

student = {
    "name": "sonakshi apoorba",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "maths": 99,
        "eng": 100
    }
}

print("Student:", student)

# Access nested value
print("Physics marks:", student["subjects"]["phy"])

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Length:", len(student))

student.update({"sst": 99})
print("After update:", student)

pairs = list(student.items())
print("First pair:", pairs[0])

# ----------------------
# SETS
# ----------------------

collection = {1, 2, 3, 2, "hello", "world", "world"}
print("Set:", collection)
print("Length:", len(collection))

# Empty set
empty_set = set()
print("Type:", type(empty_set))

# Set methods
collection3 = set()
collection3.add(1)
collection3.add("sai")
collection3.add((1, 2, 3))

collection3.remove(1)
print("After remove:", collection3)

collection3.clear()
print("After clear:", collection3)

# Pop
collection4 = {"hello", "sai", "helloworld", "coding", "python"}
print("Popped:", collection4.pop())
print("Remaining:", collection4)

# Union & Intersection
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
