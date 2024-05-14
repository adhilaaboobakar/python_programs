# Q1 : Write a python program that seperate positive and negative numbers from a list.

# num_list=[4,6,7,8,-8,-3,-2,9]

# positive_nums=[]
# negative_nums=[]

# for num in num_list:
#     if num>=0:
#         positive_nums.append(num)
#     else:
#         negative_nums.append(num)

# print(f"positive numbers : {positive_nums}")
# print(f" negative numbers : {negative_nums}")









# Q2 : Write a python program to reverse the tuple.

my_tuple=(10,20,30,"haii",50,70,"hello")
# rev=reversed(my_tuple)
# print(f"reversed tuple : {tuple(rev)}")

my_list=list(my_tuple)
my_list.reverse()
print(tuple(my_list))












# Q3: Pattern print

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4 
# 5


# for row in range(1,6):
#     for coloumn in range(row,6):
#         print(row,end="\t")
#     print()