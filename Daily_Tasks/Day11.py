# Q1: Write a Python program that print 2 list and common element

lst1=[2,4,7,3,9,5]
lst2=[5,8,9,2,3]
common_elements=[]

for num in lst1:
    if num in lst2:
        common_elements.append(num)
print(common_elements)










# Q2: Write a python program to find the least square number from a list

# lst=[5,4,7,3,8]

# lst.sort()

# sq=lst[0]**2
# print(f"The least square number from the list is: {sq}")










# Q3: Pattern print 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5


# for row in range(1,6):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()