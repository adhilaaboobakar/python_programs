# Q1. Write a Python program to find the second largest number in a list.




# lst=[3,8,9,45,3,67,2,12]


# sorted_lst=sorted(lst,reverse=True)

# second_larg_num=sorted_lst[1]
# print(second_larg_num)







# Q2. Write a program to filter the dictionary, from a dictionary of people’s heights and you wanted to filter out anyone below a certain height.
# Let’s filter out anyone less than 170cm.





# students_height = {"ramu":168,"raju":172,"radha":171,"akash":165,"pinky":177}

# for k,v in students_height.items():
#     if v<170:
#         print(k)






# 3. Pattern print 
#                             4 4 4 4 4 4 4  
#                             4 3 3 3 3 3 4   
#                             4 3 2 2 2 3 4   
#                             4 3 2 1 2 3 4   
#                             4 3 2 2 2 3 4   
#                             4 3 3 3 3 3 4   
#                             4 4 4 4 4 4 4


for row in range(0,7):
    for col in range(0,7):
        print(max(4-min(row,col,6-row,6-col),1),end=" ")
    print()