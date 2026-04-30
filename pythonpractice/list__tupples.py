## Day 3- Lists and Tuples

# ----------------------
# LISTS
# ----------------------

marks = [94.4, 95.2, 45.2]
print("Marks:", marks)
print("Type:", type(marks))
print("First mark:", marks[0])
print("Second mark:", marks[1])
print("Length:", len(marks))

student = ["Karan", 95.4, 17, "Delhi"]
print("Student name:", student[0])

# ----------------------
# LIST SLICING
# ----------------------

numbers = [87, 64, 33, 95, 76]
print(numbers[1:4])
print(numbers[:4])
print(numbers[1:])
print(numbers[-3:-1])

# ----------------------
# LIST METHODS
# ----------------------

fruits = ["a", "d", "e", "f", "c", "b"]

fruits.sort()
print("Sorted:", fruits)

fruits.sort(reverse=True)
print("Reverse sorted:", fruits)

nums = [2, 1, 3, 1]
nums.remove(1)
print("After remove:", nums)

nums.pop(2)
print("After pop:", nums)

# ----------------------
# TUPLES
# ----------------------

tup = (2, 1, 3, 1)
print("Tuple:", tup)
print("First element:", tup[0])

# Tuple slicing
tup2 = (1, 2, 3, 4)
print("Sliced tuple:", tup2[1:3])

# ----------------------
# TUPLE METHODS
# ----------------------

tup3 = (1, 2, 3, 4, 5)
print("Index of 2:", tup3.index(2))
print("Count of 2:", tup3.count(2))
