#count=1
#while count<=5:
   # print("hello")
  #  count +=1
#i=1
##while i<=100000:
 #   print("sonakshi",i)
  #  i +=1


#print numbers from 1 to 5

i=5
while i>=1:
    print(i)
    i-=1
print("loop ended")


#print numbers from 1 to 100
a=1
while a<=100:
    print(a)
    a+=1


#print numbers from 100 to 1
b=100
while b>=1:
    print(b)
    b-=1
print("loop ended")


#print the multiplication table of number n
n=int(input("enter a number:"))
i=1
while i<=10:
    print(n*i)
    i+=1
print("loop ended")


#print the elements of the following list using a loop:
[1,4,9,16,25,36,49,64,81,100]
s=1
while s<=10:
    print(s*s)
    s+=1
print("squares")


#search for a number x in this tuple using loop:
nums=(1,4,9,16,25,36,49,64,81,100)
heroes=("ironman","thor","superman","batsman")
idx=0
while idx<len(heroes):
    print(heroes[idx])  #nums[0],nums[1],nums[2]....
    idx+=1
    

#tuple search x
nums=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i< len(nums):
    if(nums[i]==x):
        print("FOUND at idx ",i)
        break
    else:
        print("finding..")
    i+=1
print("end of loop")
# break and continue
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop")    
#continue


i=0
while i<=5:
    if(i==3):
        i+=1
        continue  #skip
    print(i)
    i+=1

i=1
while i<=10:
    if( i % 2 !=0):
        i+=1
        continue
    print(i) 
    i+=1

p

