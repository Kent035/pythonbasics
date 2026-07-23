#list used to store multiple items in a single variable
#list items are ordered,changeable and allow duplicates
#listname=[item1,item2,item3]
students=["jane","kamau","john","edward"]
print(students)
print(type(students))
mynums=[56,87,39,56,88]
print(mynums)
#accessing list item
print(students[0])
print(students[3])
#change list item
students[1]="johnson"
print(students)
#list methods append(),remove(),pop()
#append()-add an item to the end of the list
students.append("cate")
print(students)
#remove()-removes a specific item
students.remove("edward")
print(students)
#sort-sorts alphabettically
mynums.sort()
print(mynums)
#looping thro a list
for x in students:
        print(x)

for y in mynums:
        print(y)
        
                