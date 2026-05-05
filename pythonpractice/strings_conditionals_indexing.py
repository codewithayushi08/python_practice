## Day 2- Strings and Conditional Statements

# ----------------------
# STRINGS BASICS
# ----------------------

str1 = "This is a string"
print("Length:", len(str1))

str2 = "sonakshi"
print("Length:", len(str2))

str3 = """this is a string"""
print("Length:", len(str3))

str4 = "This is a string.\nWe are creating it in python"
print(str4)
print("Length:", len(str4))

# ----------------------
# STRING OPERATIONS
# ----------------------

first = "sonakshi"
second = "apoorba"

final_str = first + second
print("Concatenated:", final_str)
print("Length:", len(final_str))

# ----------------------
# INDEXING & SLICING
# ----------------------

text = "sonakshi apoorba"

print(text[0])
print(text[3])
print(text[1:4])
print(text[5:12])
print(text[5:])

text2 = "apple"
print(text2[-3:-1])
print(text2[-5:-2])

# ----------------------
# STRING METHODS
# ----------------------

sentence = "i am studying python"

print(sentence.endswith("thon"))
print(sentence.capitalize())
print(sentence.replace("o", "a"))
print(sentence.replace("python", "java script"))
print(sentence.find("o"))
print(sentence.find("studying"))
print(sentence.find("queen"))
print(sentence.count("am"))

# ----------------------
# MINI PROGRAMS
# ----------------------

# Input name and print length
name = input("Enter your first name: ")
print("Welcome", name)
print("Length:", len(name))

# Count occurrence of 's'
line = "shiridi is sai baba's land."
print("Count of s:", line.count("s"))

# ----------------------
# CONDITIONAL STATEMENTS
# ----------------------

light = "ivory"

if light == "red":
    print("Stop")
elif light == "green":
    print("Go")
elif light == "yellow":
    print("Look")
else:
    print("Light is broken")

# Voting eligibility
age = 24

if age >= 18:
    print("Can vote")
else:
    print("Cannot vote")

# ----------------------
# GRADE SYSTEM
# ----------------------

marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)
