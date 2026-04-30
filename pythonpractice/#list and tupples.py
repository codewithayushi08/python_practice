#list and tupples
marks=[94.4,95.2,45.2]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))
student=["karan",95.4,17,"Delhi"]
print(student[0])
#student[0]="arjun"
#print(student)



#list slicing
marks=[87,64,33,95,76]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])


#list methods

#list=["banana ","apple" ,"litchi" ,"mango" ]
#print(list.append(4))
#print(list)
#print(list.sort())
#print(list)
#print(list.sort(reverse=True))
#print(list)

list=["a", "d","e","f","c","b"]
print(list.sort())
print(list)
print(list.sort(reverse=True))
print(list)


list=[2,1,3,1]
list.remove(1)
print(list)
list.pop(2)
print(list)


#TUPLES
tup=(2,1,3,1)
print(type(tup))
print(tup[0])
print(tup[1])
#tup[0]=5#not allowed intuple
tup=(1,2,3,4)
print(tup)
print(type(tup))
print(tup[1:3])

#TUPLE METHODS
tup=(1,2,3,4,5)
print(tup.index(2))
print(tup.count(2))