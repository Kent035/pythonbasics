"""
if statement specifies a block of code to be executed if condition is true
if condition:
              block of code to be executed if condition is true
"""
x=5
if x<10:
    print(f"{x} is less than 10")

    """
    if..else
    if condition:
                    block of code to be executed if condition is true
    else:
            block of code to be executed if condition is false
    """

    #a program that checks if a user is elegible to vote
    age=12
    if age>=18:
        print("hey,you are eligible to vote!!")
    else:
        print("sorry,you are not eligible to vote")
    #a program that asks user for age and checks if they can drive
    user_age=int(input("enter your age"))
    if user_age>=18:
                print("you can drive")
    else:
          print("you cannot drive")
          #a program that asks user for number and checks if 
          # the number is even or odd..hintevennum%2==0
    computer=70
    if computer>=100:
          print("computer is working is 100")
    else:
          print("not working well its 70")
    even=10
    if even<=7:
          print("when a number is even it ends with 2,6,8,10,12")
    else:
          print("when a number is not even it ends with 3,7,13")