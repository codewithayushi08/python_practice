 # Day 1 - Basics & Operators

# ----------------------
# PRINT & VARIABLES
# ----------------------

print("Hello World")
print(2 + 2)

name = "Ayushi"
age = 19
price = 25.99

print("My name is:", name)
print("My age is:", age)
print(price)

print(type(name))
print(type(age))
print(type(price))

# ----------------------
# DATA TYPES
# ----------------------

old = False
a = None

print(type(old))
print(type(a))

# ----------------------
# OPERATORS
# ----------------------

a = 2
b = 5

print("Power:", a ** b)
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
print("Modulo:", a % b)

# Relational Operators
a = 50
b = 20

print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Assignment Operators
num = 10
num **= 5
print("num:", num)

# Logical Operators
a = 50
b = 30

print(not(a > b))
print(True and True)
print(True or False)

# ----------------------
# TYPE CONVERSION
# ----------------------

a = 2
b = 4.25
print(a + b)

c = int("2")
print(c + b)

e = 3.14
e = str(e)
print(type(e))

# ----------------------
# INPUT
# ----------------------

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Welcome", name)
print("Age:", age)

# ----------------------
# MINI PROGRAMS
# ----------------------

# Sum of two numbers
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print("Sum =", num1 + num2)

# Area of square
side = int(input("Enter side: "))
print("Area =", side * side)

# Average of two numbers
a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
print("Average =", (a1 + b1) / 2)

# Compare two numbers
a2 = int(input("Enter a2: "))
b2 = int(input("Enter b2: "))

if a2 >= b2:
    print(True)
else:
    print(False)
