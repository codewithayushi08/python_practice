#RECURSION
#recursive function
def show(n):
    if(n==-1):#base case
     return
     
    print(n)
    show(n-1)
    print("END")

show(5) #5,4=n-1,3=n-2,2=n-3,1=n-4


def fact(n):
   if(n==1 or n==0):
      return 1
   return fact(n-1)*n
print(fact(6))



#WRITE A RECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS
def sum(n):
   if( n==0):
      return 0
   return n+sum(n-1)
print(sum(5))


#WRITE A RECURSIVE FUNCTION TO PRINT ALL ELEMENTS IN A LIST.
#HINT:USE LIST AND INDEX AS PARAMETERS
def print_list(list,idx):
   if(idx==len(list)):
      return
   print(list[idx])
   print_list(list,idx+1)

fruits=["mango","litchi","apple","banana"]
print_list(fruits,0)

