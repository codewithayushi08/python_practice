f=open("file_input_output.txt","r")

data=f.read()
print(data)

line1= f.readline()
print(line1)

line2=f.readline()
print(line2)

line3=f.readline()
print(line3)
f.close()
