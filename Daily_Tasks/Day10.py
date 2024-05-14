# # # Q1:  Write a Python program that ask users to enter a number and keep asking the users to enter a correct number, until the number with in the range that we given
# lower_limit = int(input("Enter the starting limit "))
# upper_limit = int(input("Enter the ending limit "))

# while (True):
#     num = int(input("Enter a number: "))

#     if lower_limit <= num <= upper_limit:
#         print(f"You entered a valid number: {num}")
#         break
#     else:
#         print("Invalid input. Please enter a valid number within the specified range.")
  
    






# Q2: Write a python program to list the even numbers from the range that given by the user and delete the multiplication of 5 from the list

# start = int(input("Enter the starting number of the range: "))
# end = int(input("Enter the ending number of the range: "))


# evens=[ num for num in range(start,end+1) if num%2==0]
# mul_fives=[num for num in evens if num%5!=0]

# print(f"evens list : {evens}")
# print(f"list without multiples of 5: {mul_fives}")









# Q3: Pattern print 
#      * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     *


for row in range(1,6):
    for col in range(row,6):
        print(end=" ")
    for col in range(row):
        print("*",end=" ")
    print("")
for row in range(1,6):
    for col in range(0,row):
        print(end=" ")
    for col in range(6,row,-1):
        print("*",end=" ")
    print()
    
