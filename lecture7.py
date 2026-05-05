# -------- Reading a file --------
with open("file_input_output.txt", "r") as f:
    data = f.read()
    print("Full file content:\n", data)

# -------- Reading line by line --------
with open("file_input_output.txt", "r") as f:
    print("\nReading line by line:")
    for line in f:
        print(line.strip())

# -------- Writing to a file (overwrite) --------
with open("file_input_output.txt", "w") as f:
    f.write("I want to learn JavaScript tomorrow. 123")

# -------- Appending to a file --------
with open("file_input_output.txt", "a") as f:
    f.write("\nThen I will move to ReactJS.")