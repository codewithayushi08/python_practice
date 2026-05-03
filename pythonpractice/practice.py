#WAP TO CHECK IF A NUMBER ENTERED BY THE USER IS ODD OR EVEN
number=float(input("Enter number:"))
if(number%2==0):
    print("even")
else:
    print("odd")
#WAP TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY USER
a=int(input("Enter number1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))
if (a>b and a>c):
 print("a is greatest")
elif(b>a and b>c):
   print("b is greatest")
else:
   print("c is greatest")
#WAP TO CHECK IF A NUMBER IS MULTIPLE OF 7 OR NOT
d=int(input("Enter number:"))
if(d%7==0):
   print("multiple of 7")
else:
   print("not multiple of 7")

#WAP TO FIND SMALLEST OF 3 NUMBERS
num1=int(input("Enter num1="))
num2=int(input("Enter num2="))
num3=int(input("Enter num3="))
smallest=num1

if num2<smallest:
   smallest=num2

if num3<smallest:
   smallest=num3

print("smallest number is:",smallest)

#WAP TO CHECK LEAP YEAR
def is_leap_year(year):
   if(year % 4 == 0 and year % 100!=0) or (year %400==0):
    return True
   else:
      return False
year=int(input("Enter year:"))
print(is_leap_year(year))

#WAP TO CHECK POSITIVE/NEGATIVE/ZERO
number=int(input("Enter a number:"))
if number>0:
   print("positive number")
elif number<0:
   print("negative number")
else:
   print("zero")



#WAP TO PRINT NUMBERS FROM 1 TO N
n=int(input("Enter value of n:"))
for i in range(1,n+1):
   print(i)


#WAP TO FIND FACTORIAL OF A NUMBER
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)


#WAP TO CHECK PALINDROME NUMBER
num=input("Enter a number:")
if num==num[::-1]:
   print("palindrome")
else:
   print("not palindrome")
   

    
    


    
