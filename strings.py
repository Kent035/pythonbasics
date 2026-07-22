#string- a sequence of characters./
first_name="mark"
last_name="john"
print("my first name is",first_name)
#+ concatenation
fullname=first_name +  " "+last_name
print(fullname)
#f-string f""
age=19
print(f"my name is {fullname}  and i am {age} years old")
#string methods upper(),lower() find(),replace()
message="hello world"
print(message.upper())
#capitalize
print(message.capitalize())
#lower()
print(message.lower())
#find()
print(message.find("e")) #returns the index
print(message.replace("world","goodmorning"))
#slicing/substring [start:stop]
course="python"
print(course)
print(course[0:3])# from 0 to 2
print(course[1:])# 1-end
print(course[:4])#0-3
print(course[::2])
#text="fullstack"
text="fullstack"
print(text[0:4])# from 0 to 4
print(text[4:9])
print(text[0:6])
#escape characters \n-newline,\t-tab
print("hello this\n is python")
#\t-tab-adds a tab space
print("name\t:age")
#'-adds a single quote
print('it\`s a nice day')
#\"-adds a double quote
print("she said \"hello\"")
#she said "i love python programming"
print("python is easy `\"mark john\"")
#"python is easy"-mark john
      
