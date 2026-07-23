#dictionaries are used to store data values in key:value pair
student={
    "name":"Amerson",
    "age":23,
    "course":'MiT'
}
print(student)
print(type(student))
#add key:value pair
student["city"]="nairobi"
print(student)
#accessing items[]
print(student["name"])
print(student["course"])
#change a value
student["name"]="Amerson"
print(student)
#keys()
print(student.keys())
#values()-returns a list of all the values in the dictionary
print(student.values())
#items()-returns a list containg a tuple for each key value pair
print(student.items())
#loop
for x,y in student.items():
    print(x,":",y)