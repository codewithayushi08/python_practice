# -------- Recursion: print numbers --------
def show(n):
    if n == 0:   # base case
        return
    print(n)
    show(n - 1)
    print("END")

show(5)


# -------- Factorial --------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(6))


# -------- Sum of first n natural numbers --------
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))


# -------- Print list using recursion --------
def print_list(items, idx):
    if idx == len(items):
        return
    print(items[idx])
    print_list(items, idx + 1)

fruits = ["mango", "litchi", "apple", "banana"]
print_list(fruits, 0)