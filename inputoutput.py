#WAF TO REPLACE "JAVA" WITH "PYTHON "
#SEARCH IF THE WORD "LEARNING" EXISTS IN THE FILE OR NOT.



with open("practice.txt","w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning file I/O \n")
    f.write("using java \n")
    f.write("I like programming in java.\n")

with open("practice.txt","r") as f:
    data=f.read()

new_data=data.replace("java","python")

with open("practice.txt","w") as f:
    f.write(new_data)

print("replacement done successfully")


with open ("practice.txt","r") as f:
    data=f.read()
if "learning" in data:
    print("word found")
else:
    print("word not found")



##WAF TO FIND IN WHICH LINE OF THE FILE DOES THE WORD LEARNING OCCURS FIRST.
with open("practice.txt","r") as f:
    for line_no, line in enumerate(f,start=1):
        if "learning" in line:
            print("found in line:",line_no)
            break
    else:
            print("word not found")



