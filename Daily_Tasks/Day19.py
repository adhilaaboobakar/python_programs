
# # Q1. Write a python program to identify unique triplets whose three elements sum to zero from an array of n integers



# def three_sum(nums):
#     triplets=[]
#     for i in range(0,len(nums)-2):
#         for j in range(i+1,len(nums)-1):
#             for k in range(j+1,len(nums)):
#                 if nums[i]+nums[j]+nums[k]==0:
#                     triplets.append((nums[i],nums[j],nums[k]))
#     return triplets

# nums=[-3,-2,-1,0,1,2,3]
# triplets=three_sum(nums)

# if len(triplets)>0:
#     print("Triplets whose sum is zero: ")
#     for triplet in triplets:
#         print(triplet)
# else:
#     print("No triplets found whose sum is zero")





# Q2:Write a python program to make combinations of 3 digits



from itertools import combinations 

digits=[1,2,3,4,5]

digit_combinations=list(combinations(digits,3))
for combination in digit_combinations:
    print(combination)






# 3. Pattern print 
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *


# rows=5
# for i in range(rows):
#     for j in range(rows - i - 1):
#         print(" ", end="")
#     print("*", end="")
#     for j in range(2 * i - 1):
#         print(" ", end="")
#     if i != 0:
#         print("*", end="")
#     print()


# for i in range(rows - 1, 0, -1):
#     for j in range(rows - i):
#         print(" ", end="")
#     print("*", end="")
#     for j in range(2 * i - 3):
#         print(" ", end="")
#     if i != 1:
#         print("*", end="")
#     print()
