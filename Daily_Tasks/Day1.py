# Q1 : Write a program to display "HELLO" if a number entered by user is a multiple of five,otherwise print "Bye"

# num=int(input("enter a number "))

# if num%5==0 and num!=0 :
#     print("HELLO")
# else:
#     print("Bye")


# Q2 : Write a program to check a person in eligible for voting or not

# age=int(input("enter age "))

# if age>=18:
#     print("eligible for voting")
# else:
#     print("not eligible for voting")


# Q3 : Write a program to accept the percentage from user and display the grade

# percentage=int(input("Enter percentage :"))

# if percentage>90 and percentage<=100:
#     print("A Grade")
# elif percentage>80:
#     print("B Grade")
# elif percentage>60:
#     print("C Grade ")
# else:
#     print("D Grade")



# Q4: Write a program to find the largest number out of the three numbers excepted from the user.

n1 = int(input("Enter number1 : "))
n2 = int(input("Enter number2 : "))
n3 = int(input("Enter number3 : "))

if n1>n2 and n1>n3:
    print(f"{n1} is largest")
elif n2>n1 and n2>n3:
    print(f"{n2} is largest")
elif n3>n1 and n3>n2:
    print(f"{n3} is largest")
else:
    print("the entered numbers are equal")
