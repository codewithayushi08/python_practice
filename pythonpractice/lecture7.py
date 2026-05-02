## Reading a file 
#data=f.read() # reads entire file
# data= f.readline()  # reads one line at time

f=open("file_input_output.txt","rt")

data=f.read()
print(data)

line1= f.readline()
print(line1)

line2=f.readline()
print(line2)

line3=f.readline()
print(line3)
f.close()

## Writing to a file
# f.open("demo.txt","w")
# f.write("this is a new line")#overwrites the entire line

#f.open("demotxt","a")
# f.write("this is a new line") #adds to the file


f=open("file_input_output.txt","w")
f.write("I want to learn java script tomorrow.123")
f.close()

f=open("file_input_output.txt","a")
f.write("\nThen i will move to reactjs.")
f.close()
