info={
    "key":"value",
    "name":"sai",
    "learning":"coding",
    "age":35,
    "is_adult":True,
    "marks":94.4,
    "subjects":["python","c","java"],
    "topics":("dict","set")
}

null_dict={}

print(null_dict)

print(type(info))
info["name"]="ayushi"
info["surname"]="das"
print(info)
print(info["name"])
print(info["topics"])
print(info["subjects"])
print(info["learning"])


#nested dictionaries

student={
    "name":"sonakshi apoorba",
    "subjects":{
        "phy":97,
        "chem":98,
        "maths":99,
        "eng":100,

    }
}
print(student)

print(student.keys())
print(student.values())
print(list(student.keys()))
print(list(student.values()))
print(student.items())
print(len(student))
print(student.get("phy"))
student.update({"sst":99})
print(student)
pairs=list(student.items())
print(pairs[0])

#set
collection={1,2,3,2,"hello","world","world"}
print(collection)
print(type(collection))
print(len(collection))

collection1={} #empty dictionary
collection2=set()
print(type(collection2))
#set methods
collection3=set()
collection3.add(1)
collection3.add("sai")
collection3.add((1,2,3))
collection3.remove(1)
collection3.clear()
print(len(collection3))



collection4={"hello","sai","helloworld","coding","python"}
print(collection4.pop())
print(collection4.pop())
set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))
