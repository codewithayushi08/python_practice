#strings and conditional statements
str1="This is a string"
len1=len(str1)
print(len1)
str2='sonakshi'
len2=len(str2)
print(len2)
str3="""this is a string"""
len3=len(str3)
print(len3)
str4="This is a string.\n We are creating it in python" 
print(str4)
len4=len(str4)
print(len4)
str5="sonakshi"
str6="apoorba"
final_str = str5+str6
print(final_str)
lenfinal=len(final_str)
print(lenfinal)
#INDEXING

str="sonakshi apoorba"
ch=str[0]
print(ch)
print(str[3])
print(str[1:4])
print(str[5:12])
print(str[5:])
str="apple"
print(str[-3:-1])
print(str[-5:-2])
str="i am studying python"
print(str.endswith("thon"))
print(str.capitalize())
print(str)
print(str.replace("o","a"))
print(str.replace("python","java script"))
print(str.find("o"))
print(str.find("studying"))
print(str.find("queen"))
print(str.count("am"))



#WAP to input users first name and print its length  
name=input("Enter your first name:")
print("Welcome",name)
len_name=(len(name))
print(len_name)



#WAP tofind occurrence of s in a string
str1="shiridi is sai baba's land."
print(str1.count("s"))

#conditional statements
light="ivory"
if(light=="red"):
   print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look") 
else: print("light is broken")# else only once used without any conditions


num=5
#if(num>2):
 #   print("greater than 2")
#elif(num>3):
   # print("greater than 3")
age=24
if(age>=18):
    print("can vote")#indentations=proper spacing
else:
    print("CANNOT VOTE")



#grade system
marks=float(input("Enter your marks:"))
if(marks >= 90):
    grade="A"
elif(marks>=80 and marks <90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"
print("Grade of student ->",grade)


