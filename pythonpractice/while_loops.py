# Day 5 - While Loops

# ----------------------
# BASIC LOOPS
# ----------------------

# Print numbers from 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1
print("Loop ended")

# Print numbers from 1 to 100
num = 1
while num <= 100:
    print(num)
    num += 1

# Print numbers from 100 to 1
num = 100
while num >= 1:
    print(num)
    num -= 1
print("Loop ended")

# ----------------------
# MULTIPLICATION TABLE
# ----------------------

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1

# ----------------------
# LIST USING LOOP
# ----------------------

nums = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1

# ----------------------
# TUPLE LOOP
# ----------------------

heroes = ("ironman", "thor", "superman", "batman")
i = 0
while i < len(heroes):
    print(heroes[i])
    i += 1

# ----------------------
# SEARCH IN TUPLE
# ----------------------

nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0

while i < len(nums):
    if nums[i] == x:
        print("Found at index:", i)
        break
    i += 1

print("End of loop")

# ----------------------
# BREAK EXAMPLE
# ----------------------

i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1

print("End of loop")

# ----------------------
# CONTINUE EXAMPLE
# ----------------------

i = 0
while i <= 5:
    i += 1
    if i == 3:
        continue
    print(i)

# Print even numbers
i = 1
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1
