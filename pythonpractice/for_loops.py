



## DAY 6- for loops and range

# ----------------------
# BASIC FOR LOOPS
# ----------------------

nums = [1, 2, 3, 4, 5]
for val in nums:
    print(val)

veggies = ["potatoes", "brinjal", "ladyfinger", "cucumber"]
for val in veggies:
    print(val)

tup = (1, 2, 3, 4, 2, 8, 9)
for num in tup:
    print(num)

# ----------------------
# STRING LOOP
# ----------------------

text = "sai"
for char in text:
    if char == "a":
        print("a found")
        break
    print(char)
else:
    print("end")

# ----------------------
# PRACTICE: PRINT LIST
# ----------------------

nums = [1,4,9,16,25,36,49,64,81,100]
for val in nums:
    print(val)

# ----------------------
# SEARCH IN TUPLE
# ----------------------

tup = (1,4,9,16,25,36,49,64,81,100)
x = 16

for idx, num in enumerate(tup):
    if num == x:
        print("Found at index:", idx)
        break
else:
    print("Not found")

# ----------------------
# RANGE
# ----------------------

for i in range(10):
    print(i)

print(range(5))

for i in range(1, 100, 2):
    print(i)

# ----------------------
# NUMBER PRINTING
# ----------------------

# 1 to 100
for i in range(1, 101):
    print(i)

# 100 to 1
for i in range(100, 0, -1):
    print(i)

# ----------------------
# MULTIPLICATION TABLE
# ----------------------

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n * i)

# ----------------------
# PASS STATEMENT
# ----------------------

for i in range(5):
    pass

print("Some useful work")

# ----------------------
# SUM OF FIRST N NUMBERS
# ----------------------

n = 5
total = 0

for i in range(1, n + 1):
    total += i

print("Total sum =", total)

# ----------------------
# FACTORIAL
# ----------------------

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)
