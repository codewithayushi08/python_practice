def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum
calc_sum(5,10)


#3a=5,b=10

#sum=a+b
#print(sum)
#more lines of code
calc_sum(2,10)
#a=2,b=10
#sum=a+b
#print(sum)


#more lines of code
calc_sum(12,17)
#a=12,b=17
#sum=a+b
#print(sum)

#function definition
def calc_sum(a,b):#parameters
    return a+b
sum= calc_sum(178,2221) #function call,arguments(a,b)
print(sum)


def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()
print_hello()
output=print_hello()
print(output)


#types of functions

#built in functions

print("sai", end=" $") #sep=" "
print("sonakshi") #end = " \n"


#user defined functions


#default parameters
def cal_prod(a,b=3):
    print(a*b)
    return a*b
cal_prod(3)