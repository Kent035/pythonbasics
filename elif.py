"""
elif-used to test for multiple codition
if condition1:
                block of code to be executed if condition1 is true
elif condition2:
                block of code to be executed if condition2 is true
else:
        block of code to be executed if all conditions are false

"""
#a program that asks user for marks themn prints grade
#80-100=A
#70-79=B
#60-69=C
#50-59=D
#<50 FAIL
marks=int(input("Enter your marks to print grade"))
if marks>=80 and marks<=100:
    print("GRADE A")
elif marks>=70 and marks<80:
    print("GRADE B")
elif marks>=60 and marks<70:
    print("GRADE C")
elif marks>=50 and marks<60:
    print("GRADE D")
else:
    print("FAIL")
#a program that asks user for their age and prints the age category
#<18-baby
#18-30=young adult
#30-45-adult
#45-65-mature adult
#>65 -elderly
age=int(input("Enter your age to print the age category"))
if age<18:
    print("baby")
elif age<=18 and age<30:
    print("young adult")
elif age<=30 and age<45:
    print("adult")
elif age<=45 and age<65:
    print("mature adult")   
else:
    print("PASS")
