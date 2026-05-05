# -------- Function to calculate sum --------
def calc_sum(a, b):
    return a + b

result1 = calc_sum(5, 10)
result2 = calc_sum(2, 10)
result3 = calc_sum(12, 17)

print(result1)
print(result2)
print(result3)

# -------- Another example --------
total = calc_sum(178, 2221)
print(total)


# -------- Function to print hello --------
def print_hello():
    print("hello")

for _ in range(5):
    print_hello()


# -------- Built-in print usage --------
print("sai", end=" $")
print("sonakshi")


# -------- Default parameter example --------
def calc_product(a, b=3):
    return a * b

print(calc_product(3))       # uses default b=3
print(calc_product(3, 5))    # overrides default