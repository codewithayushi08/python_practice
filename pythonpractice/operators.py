print('hello World')
print(2+2)
print("my name is ayushi, my age is 19.")
name="Ayushi" 
age=19
price=25.99
print("my name is:", name)
print("my age is:",age)
print(price)
print(type(name))
print(type(age))
print(type(price))

old=False
a=None
print(type(old))
print(type(a))
a=2
b=5
sum=a+b
diff=a-b
product=a*b
modulo=a/b
divide=a%b
print(a**b)
print(sum)
print(diff)
print(product)
print(modulo)
print(divide)
#arithmetic operators
#relational operators
a=50
b=20
print(a==b) #false
print(a!=b) #true
print(a>=b)
print(a<=b)
#assignment operators
num=10
#num += 10 #10+10 =>20
#num -= 10
#num %= 5
num **=5
print("num",num)
#logical operators
a=50
b=30
print(not(a>b))
print(not False)
print(not True)
val1=True
val2=True
print("and operator:", val1 and val2)
print("OR operator:",val1 or val2)
val3= False
print("and operator:", val1 and val3)
print("OR operator:", val1 or val3)
print("OR operator:", (a==b)or (a>b))
#type conversion
a=2
b=4.25
sum=a+b #2.0+4.25=>6.25
print(sum)
c=int("2")
d=4.25
print(c+d)
e=3.14
e=str(e)
print(type(e))
input("enter your name:")
print("welcome", name)
name=input("enter your age:")
print("you entered",name)
val=input("enter some value:")
print(type(val), val)
name=input("enter name :")
age=input("enter age :")
marks=input("enter marks:")
print("welcome", name)
print("age=",age)
print("marks=", marks)


# program to input2 numbers and print their sum
num1=int(input("enter num 1 :"))
num2=int(input("enter num2: "))
print("sum=", num1+num2)


#WAP to input side of a square & print its area
side=int(input("value of side of square :"))
print("area=",side*side)


#wap to input 2 floating point numbers and print their average
a1=float(input("enter a1 :"))
b1=float(input("enter b1 : "))
print("average=",a1+b1/2)

#wap to input 2 int numbers , a and b.
#print true if a is greater thanor equal to b. if not print else.

a2=int(input("enter a2 : "))
b2=int(input("enter b2: "))
if a2>=b2:
 print(True)
else:
  print(False)


