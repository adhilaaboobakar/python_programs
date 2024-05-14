# # Q1 :  Write a program to accept 2 numbers and mathematical operators and perform operation accordingly.

# num1=int(input("Enter 1st number :"))
# num2=int(input("Enter 2nd number :"))
# operator = input("Enter operator :")

# if operator == "+":
#     print(num1+num2)
# elif operator =="-":
#     print(num1-num2)
# elif operator =="*":
#     print(num1*num2)
# elif operator =="/":
#     if num2!=0:
#         print(num1/num2)
#     else:
#         print("Division by zero is not possible")
# elif operator =="%":
#     print(num1%num2)
# elif operator=="//":
#     print(num1//num2)
# else:
#     print("Invalid operator")



# Q2 : Take input age of 3 people by user and determine oldest and youngest among them.

# age_1 =int(input("Enter the age of 1st person :"))
# age_2=int(input("Enter the age of 2nd person :"))
# age_3 =int(input("Enter the age of 3rd person : "))

# if age_1>age_2 and age_1>age_3:
#     print(f"{age_1} older")
#     if age_2>age_3:
#         print(f"{age_3} is youngest")
#     else:
#         print(f"{age_2} is youngest")

# elif age_2>age_1 and age_2 and age_3:
#     print(f"{age_2} is older")
#     if age_1>age_3:
#         print(f"{age_3} is youngest")
#     else:
#         print(f"{age_2} is youngest")

# elif age_3>age_1 and age_3>age_2:
#     print(f"{age_3} is older")
#     if age_2>age_1:
#         print(f"{age_1} is youngest")
#     else:
#         print(f"{age_2} is youngest")
# else:
#     print("all ages are same")



# Q3: Take values of length and breadth of a rectangle from user and check if it is square or not.

len=int(input("Enter the length : "))
bre=int(input("Enter the breadth : "))

if len==bre:
    print("it is a square")
else:
    print("It is not a square")



