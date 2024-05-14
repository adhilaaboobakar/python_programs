# Q1. The original list : [1, 3, 5, 1, 3, 2, 5, 4, 2] (user input)
# Matrix after grouping : [[1, 1], [2, 2], [3, 3], [4], [5, 5]]

user_input=[1,3,5,1,3,2,5,4,2]

user_input.sort()
elements=set()
matrix=[]
for i in user_input:
    if i not in elements:
        if user_input.count(i)>1:
            matrix.append([i,i])
        else:
            matrix.append([i])
        elements.add(i)
print(matrix)






# Q2.	Write a program to calculate the electricity bill. Accept the number of units consumed from the user
# Unit                        Price
# First 100 units      No charge
# Next 100 units     Rs 5 per unit
# After 200 units    Rs 10 per unit
# For example if input unit is 350 then total bill amount is Rs 2000



# input_unit=int(input("Enter the consumed unit : "))

# if input_unit<=100:
#     print("No charge")
# elif input_unit<=200:
#     print(f"total amount= {(input_unit-100)*5}")
# else:
#     print(f"total amount = {100*5+(input_unit-200)*10}")




# Q3. Pattern print 
#       A 
#      A B 
#     A B C 
#    A B C D 
#   A B C D E



# i=65
# for row in range(5):
#     for j in range(5-row-1):
#         print(" ", end="")
#     for k in range(row + 1):
#         print(chr(i+k), end=" ")
#     print("")