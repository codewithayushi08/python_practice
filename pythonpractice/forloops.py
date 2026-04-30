nums=[1,2,3,4,5]

for val in nums:
    print(val)


veggies=["potatoes","brinjal","ladyfinger","cucumber"]
for val in veggies:
    print(val)


tup=[1,2,3,4,2,8,9] 
for num in tup:
    print(num)   

str="sai"
for char in str:
    if(char=="a"):
        print("a found")
        break
    print(char)
else:
    print("end")

#practice questions
#print the elements of the following list using a loop
nums=[1,4,9,16,25,36,49,64,81,100]
for val in nums:
    print(val)




#search for a number x in this tuple using loop:
tup=[1,4,9,16,25,36,49,64,81,100]
x=16
i=0
for num in tup:
    if(num==x):
        print("found at idx",i)
        break
    i+=1
    print(num)
else:
    print("not found")


#RANGE
seq=range(10)
for i in seq:
    print(i)
print(seq[1])
print(seq[2])
print(seq[3])
print(range(5))


for i in range(1,100,2):
    print(i)


#using for and range
#print numbers from 1 to 100
for i in range(1,101):
    print(i)


#print numbers from 100 to 1
for i in range (100,0,-1):
    print(i)


#print the multiplication table of a  number n.

n=int(input("enter a number:"))
for i in range(1,11):
    print(n*i)
    

#pass statements
for i in range (5):
    pass


print("some useful work")



#WAP TO FIND SUM OF FIRST N NUMBERS (USING WHILE LOOP)
n=5

sum=0
for i in range(1,n+1):
    print(i)
    sum+=i
print("total sum=",sum)



#wap to find the factorial of first n numbers.(using for)
n=int(input("enter a number:"))
fact=1
i=1
for i in range(1,n+1):
    
    fact*=i
print("the final factorial=",fact)
