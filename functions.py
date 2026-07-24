#function is a block of code that does a specific task
#the code only runs when its called
"""
def functionname():
    body of the function

#calling the function
functionname()
"""
def greetings():
    print("hello!,good morning")

    #calling the function
    greetings()
    greetings()
    greetings()
    #function with parameter
    def hello(first_name):
        print("hi,how are you",first_name)

#calling the function
hello:("Luke")
hello:("mark")
#function with multiple parameters
def opera(name,age,course="mit"):
    print(f"student name is :{name} age:{age} and course:{course}")

#calling the function
opera("milton",23,"mit")
opera("edward",25,"artificial intelligence")
opera("william",21,)
#function that calculates area of a reactangle(l*w)
def areaOfRectangle(l,w):
    area=l*w
    print(f"The area of rectangle with length{l} and width {w} is {l,w}")
#calling the function
areaOfRectangle(10,90)
areaOfRectangle(45,34)
#function that calculates area of a circle .a=3.14*r*r
def areaOfCircle(r):
    area=3.14*r*r
    print(f"the area of circle with radius{r}is {area}")
    #calling the function
areaOfCircle(4)
areaOfCircle(17)
